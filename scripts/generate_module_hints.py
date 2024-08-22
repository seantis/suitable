#!/usr/bin/env python3

"""
This auto-generates method signatures, including a custom `RunnerResults`
return type for each all of the installed Ansible modules. It also generates
a docstring for each method.
"""
from __future__ import annotations

import ansible.modules  # type:ignore[import-untyped]
import os
import re
import yaml

from importlib import import_module
from io import StringIO
from pkgutil import walk_packages
from typing import Any

version_hint_above = (2, 8)
reference_re = re.compile(r'(?<!\S)([A-Z])\(([^)]+)\)')
modules_py = StringIO()
modules_pyi = StringIO()
type_map = {
    'string': 'str',
    'raw': 'str',
    'str': 'str',
    'int': 'int',
    'bool': 'bool',
    # NOTE: Technically you can construct a `PathLike` that will not work
    #       but since pretty much all of them convert to str just fine
    #       we accept it anyways
    'path': 'StrPath',
    # FIXME: We don't support complex parameter types
    'list': 'NotSupported',
    'dict': 'NotSupported',
}


def version(version: str) -> tuple[int, ...]:
    return tuple(
        int(part) if part.isnumeric() else 0
        for part in str(version).split('.')
    )


def write_function_parameter_list(options: dict[str, Any] | None) -> None:
    if options is None:
        modules_pyi.write('self')
        return
    elif not options:
        modules_pyi.write('self, arg: str, /')
        return

    modules_pyi.write(
        '\n'
        '        self,\n'
        '        *,\n'
    )
    for name, meta in options.items():
        if name == 'async':
            name = 'async_'
        # if the type is not set it appears to always be str
        type_name = type_map.get(meta.get('type', 'string'), 'Incomplete')
        if print_default := (
            type_name not in ('NotSupported', 'Incomplete')
            and 'default' in meta
            and (default := meta['default']) is not None
        ):
            if type_name == 'bool':
                default = True if default in ('yes', True) else False

            default_type = type(default).__name__
            if default_type == 'str' and ' ' in default:
                # likely a description
                print_default = False
            elif type_name != 'StrPath' and type_name != default_type:
                if default_type == 'str':
                    # likely a description
                    print_default = False
                else:
                    type_name = f'{default_type} | {type_name}'

        if (
            type_name == 'str'
            and 'choices' in meta
            # this means we need to support arbitrary strings
            and '*regex*' not in (raw_choices := meta['choices'])
        ):
            choices = ', '.join(repr(choice) for choice in raw_choices)
            type_name = f'Literal[{choices}]'
        modules_pyi.write(
            f'        {name}: {type_name}'
        )
        if print_default:
            modules_pyi.write(f' = {default!r}')
        elif meta.get('required', 'no') in ('no', False):
            modules_pyi.write(' = ...')
        modules_pyi.write(',\n')
    modules_pyi.write('    ')


def write_function_signature(options: dict[str, Any] | None) -> None:
    has_free_form = options and options.pop(
        'free_form',
        options.pop('free-form', False)
    )

    # we need overloads for both variants, we put the one with all
    # the parameter names first, for better language server support
    if has_free_form and options:
        modules_pyi.write('    @overload\n')
        write_function_signature(options)
        options = {}
        modules_pyi.write('    @overload\n')

    modules_pyi.write(f'    def {module_name}(')
    write_function_parameter_list(options)
    # TODO: use generated return type
    modules_pyi.write(') -> RunnerResults: ...\n')


exceeded_line_limit: bool = False
referenced_urls: list[str] = []


def write_docstring_line(content: str, level: int = 0) -> None:
    # the ansible docs have their own reference format, we replace
    # these with backticked statements and for M we reference the
    # generated method it should reference
    def replace(match: re.Match[str]) -> str:
        mode = match.group(1)
        value = match.group(2)

        # normalize references to boolean values
        if value == 'yes':
            value = True
        elif value == 'no':
            value = False

        if mode == 'M':
            # module -> method link
            return f':meth:`{value}`'
        elif mode == 'L':
            # link
            label, href = value.split(',')
            referenced_urls.append(href)
            return f'`{label}`__'
        elif mode == 'B':
            # bold
            return f'**{value}**'
        elif mode == 'I':
            # italic
            return f'*{value}*'
        elif mode == 'U':
            # url
            url = value
            referenced_urls.append(url)
            return '`here__'
        elif mode in 'ROCV':
            return f'`{value}`'
        else:
            raise ValueError(f'Unknown reference mode {mode}')
    content = reference_re.sub(replace, content).replace('\\', '\\\\')

    global exceeded_line_limit
    indent_len = level * 4 + 8
    indent = ' ' * indent_len
    max_chars_per_line = 79 - indent_len
    start = 0
    end = max_chars_per_line
    while len(content) - start > max_chars_per_line:
        end = content.rfind(' ', start, end)
        if end < 0:
            exceeded_line_limit = True
            end = content.find(' ', start + max_chars_per_line)
        modules_py.write(f'{indent}{content[start:end]}\n')
        start = end + 1
        end = start + max_chars_per_line
    modules_py.write(f'{indent}{content[start:]}\n')


def write_function_docstring(options: dict[str, Any] | None) -> None:
    global exceeded_line_limit
    description = docs['short_description']
    # ansible docs are inconsistent about using periods
    if description[-1] != '.':
        description = f'{description}.'
    write_docstring_line(description)
    if version(version_added := docs['version_added']) > version_hint_above:
        modules_py.write(
            f'\n        Minimum Ansible version: {version_added}\n'
        )

    if options:
        modules_py.write('\n')

    # free form parameters should have already been popped off the options
    # so we don't need to special case them
    for name, meta in (options or {}).items():
        modules_py.write(f'         :param {name}:\n')
        for line in meta['description']:
            # lines are not consistently terminated
            if line[-1] != '.':
                line += '.'
            write_docstring_line(line, level=1)

        version_added = meta.get('version_added')
        if version_added and version(version_added) > version_hint_above:
            modules_py.write(
                f'            Minimum Ansible version: {version_added}\n'
            )

    # insert anonymous references for the urls
    for url in referenced_urls:
        if len(url) > 68:
            exceeded_line_limit = True
        modules_py.write(f'        __ {url}\n')

    if referenced_urls:
        modules_py.write('\n')
        referenced_urls.clear()


modules_py.write('''"""
This is an auto-generated file. Please don't manually edit.

Instead call `scripts/generate_module_hints.py`
"""


class AnsibleModules:
''')
modules_pyi.write('''
# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from _typeshed import StrPath
from suitable.runner_results import RunnerResults
from suitable.types import Incomplete
from typing import Literal, overload
from typing_extensions import Never as NotSupported


class AnsibleModules:
'''[1:])
seen: set[str] = set()
for info in walk_packages(ansible.modules.__path__, 'ansible.modules.'):
    if info.ispkg:
        continue

    try:
        module = import_module(info.name)
        _, module_name = info.name.rsplit('.', 1)
    except ImportError:
        print(f'Failed to import module {info.name}')

    if not hasattr(module, 'DOCUMENTATION'):
        continue

    if not hasattr(module, 'RETURN'):
        continue

    if module_name in seen:
        continue

    seen.add(module_name)

    docs = yaml.safe_load(module.DOCUMENTATION)
    # TODO: Generate return type
    # returns = yaml.safe_load(module.RETURN)

    write_function_signature(options := docs.get('options', None))
    modules_py.write(
        f'\n    def {module_name}(self, *args, **kwargs):\n'
        '        """\n'
    )
    write_function_docstring(options)
    if exceeded_line_limit:
        exceeded_line_limit = False
        modules_py.write('        """  # noqa: E501\n')
    else:
        modules_py.write('        """\n')
    modules_py.write(f'        raise AttributeError({module_name!r})\n')

here = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(here, '..', 'src', 'suitable')
with open(os.path.join(target_dir, '_modules.py'), 'w') as fp:
    fp.write(modules_py.getvalue())
with open(os.path.join(target_dir, '_modules.pyi'), 'w') as fp:
    fp.write(modules_pyi.getvalue())
