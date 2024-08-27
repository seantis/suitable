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
from suitable.runner_results import RunnerResults
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

version_hint_above = (2, 8)
reference_re = re.compile(r'([MLBIUROCVE])\(([^)]+)\)')
modules_py = StringIO()
modules_header_py = StringIO()
types_py = StringIO()
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


def write_function_parameter_list(
    options: dict[str, Any] | bool | None,
    is_overload: bool
) -> None:
    if options is None:
        modules_py.write('self')
        return
    elif options is True:
        modules_py.write('self, *args: Any, **kwargs: Any')
        return
    elif not options:
        modules_py.write('self, arg: str, /')
        return

    modules_py.write(
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
            # NOTE: This is just a heuristic, we may need to adjust this
            if len(choices) > 40:
                choices = '\n'.join(
                    f'            {choice!r},' for choice in raw_choices
                )
                choices = f'\n{choices}\n        '
            type_name = f'Literal[{choices}]'
        modules_py.write(
            f'        {name}: {type_name}'
        )
        if print_default:
            modules_py.write(f' = {default!r}')
        elif meta.get('required', 'no') in ('no', False):
            modules_py.write(' = _Unknown')
        modules_py.write(',\n')
    modules_py.write('    ')


def write_function_signature(
    options: dict[str, Any] | bool | None,
    is_overload: bool = False
) -> None:

    has_free_form = isinstance(options, dict) and options.pop(
        'free_form',
        options.pop('free-form', False)
    )

    # we need overloads for both variants, we put the one with all
    # the parameter names first, for better language server support
    if has_free_form and options:
        modules_py.write('    @overload\n')
        write_function_signature(options, is_overload=True)
        modules_py.write('\n    @overload\n')
        write_function_signature({}, is_overload=True)
        options = True
        modules_py.write('\n')

    modules_py.write(f'    def {module_name}(')
    write_function_parameter_list(options, is_overload)
    modules_py.write(f') -> {return_type_name}:')
    modules_py.write(' ...\n' if is_overload else '\n')


exceeded_line_limit: bool = False


def split_docstring_lines(
    content: str,
    level: int = 0
) -> Generator[str, None, None]:

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
            if end < 0:
                end = len(content)
        yield f'{indent}{content[start:end]}\n'
        start = end + 1
        end = start + max_chars_per_line
    yield f'{indent}{content[start:]}\n'


def prepare_docstring_line(content: str) -> str:
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
            return f'`{label} <{href}>`__'
        elif mode == 'B':
            # bold
            return f'**{value}**'
        elif mode == 'I':
            # italic
            return f'*{value}*'
        elif mode == 'U':
            # url
            # NOTE: The Ansible docs reference an old class name
            url = value.replace('re.MatchObject', 're.Match')
            fragment_idx = url.find('#')
            if fragment_idx > 0:
                name = url[fragment_idx + 1:]
            else:
                name = 'reference'
            return f'`{name} <{url}>`__'
        elif mode in 'ROCVE':
            if isinstance(value, str):
                # NOTE: Values are already escaped, so we need
                #       to unescape so we don't double escape
                value = value.replace('\\\\', '\\')
            return f'`{value}`'
        else:
            raise ValueError(f'Unknown reference mode {mode}')

    return reference_re.sub(replace, content).replace('\\', '\\\\')


def write_docstring_line(content: str, level: int = 0) -> None:
    content = prepare_docstring_line(content)
    for line in split_docstring_lines(content, level):
        modules_py.write(line)


def write_function_docstring(options: dict[str, Any] | None) -> None:
    global exceeded_line_limit
    description = docs['short_description'].strip()
    # ansible docs are inconsistent about using periods
    if description[-1] != '.':
        description = f'{description}.'
    write_docstring_line(description)
    if version(added := docs['version_added']) > version_hint_above:
        modules_py.write(
            f'\n        .. note:: Requires ansible-core >= {added}\n'
        )

    if options:
        modules_py.write('\n')

    # free form parameters should have already been popped off the options
    # so we don't need to special case them
    for name, meta in (options or {}).items():
        modules_py.write(f'        :param {name}:\n')
        for line in meta['description']:
            line = line.strip()
            if not line:
                continue

            # lines are not consistently terminated
            if line[-1] != '.':
                line += '.'
            write_docstring_line(line, level=1)

        added = meta.get('version_added')
        if added and version(added) > version_hint_above:
            modules_py.write(
                f'            Requires ansible-core >= {added}\n'
            )


def write_return_type(returns: dict[str, Any] | None) -> None:
    assert RunnerResults.__doc__
    types_py.write(
        '\n\n@type_check_only\n'
        f'class {return_type_name}(RunnerResults):\n'
        f'    """{RunnerResults.__doc__[:-4]}'
    )
    if not returns:
        _, comment = module.RETURN.strip(' \n\t').split('#', 1)
        comment = comment.lstrip()
        if comment:
            if not comment.endswith('.'):
                comment += '.'
        else:
            comment = (
                'The return values for this module were not '
                'documented when these types were auto-generated, '
                'this could mean there are no return values.'
            )
        for line in split_docstring_lines(comment, -1):
            types_py.write(line)
        types_py.write('\n    """\n')
        return

    types_py.write('    """\n')
    for name, meta in returns.items():
        return_type = meta['type']
        if return_type == 'list':
            return_type += '[Incomplete]'
        elif return_type == 'dict':
            return_type += '[str, Incomplete]'
        if len(name) + len(return_type) > 33:
            # signature doesn't fit on one line
            types_py.write(
                f'\n    def {name}(\n'
                '        self,\n'
                '        server: str | None = None\n'
                f'    ) -> {return_type}:\n'
            )
        else:
            types_py.write(
                f'\n    def {name}(self, server: str | None = None)'
                f' -> {return_type}:\n'
            )
        types_py.write('        """\n')
        description_paragraphs = meta['description']
        if isinstance(description_paragraphs, str):
            description_paragraphs = [description_paragraphs]

        first = True
        for paragraph in description_paragraphs:
            if first:
                first = False
            else:
                types_py.write('\n')

            if not paragraph.endswith('.'):
                paragraph += '.'
            paragraph = prepare_docstring_line(paragraph)
            for line in split_docstring_lines(paragraph):
                types_py.write(line)

        condition = prepare_docstring_line(meta['returned'])
        if condition.startswith('When') or condition.startswith('when'):
            condition = condition[5:]
        types_py.write('\n')
        for line in split_docstring_lines(f'Returned when: {condition}'):
            types_py.write(line)

        added = meta.get('version_added')
        if added and version(added) > version_hint_above:
            types_py.write(
                f'\n        .. note:: Requires ansible-core >= {added}\n'
            )

        if exceeded_line_limit:
            types_py.write('        """  # noqa: E501\n')
        else:
            types_py.write('        """\n')
        types_py.write(
            f'        return self.acquire(server, \'{name}\')\n'
        )


modules_header_py.write('''\
# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from typing import overload, Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath
    from suitable._module_types import (
''')
modules_py.write('''\
    )
    from suitable.types import Incomplete
    from typing_extensions import Never as NotSupported


# HACK: Get Sphinx to display the default values we don't
#       know as `...` and also avoid mypy errors.
_Unknown: Any = type('...', (object,), {'__repr__': lambda s: '...'})()


class AnsibleModules:
''')
types_py.write('''\
# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from suitable.runner_results import RunnerResults
from suitable.types import Incomplete
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import type_check_only
else:
    def type_check_only(f):
        return f
''')
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
    returns = yaml.safe_load(module.RETURN)
    return_type_name = ''.join(p.title() for p in module_name.split('_'))
    return_type_name += 'Results'
    modules_header_py.write(f'        {return_type_name},\n')
    write_return_type(returns)
    modules_py.write('\n')
    write_function_signature(options := docs.get('options', None))
    modules_py.write(
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
    fp.write(modules_header_py.getvalue())
    fp.write(modules_py.getvalue())
with open(os.path.join(target_dir, '_module_types.py'), 'w') as fp:
    fp.write(types_py.getvalue())
