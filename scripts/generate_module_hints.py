#!/usr/bin/env python3

"""
This auto-generates method signatures, including a custom `RunnerResults`
return type for each all of the installed Ansible modules. It also generates
a docstring for each method.
"""
from __future__ import annotations

import os
import re

from ansible import constants as C  # type:ignore
from ansible.plugins.loader import fragment_loader  # type:ignore
from ansible.plugins.loader import init_plugin_loader
from ansible.plugins.loader import module_loader
from ansible.plugins.list import list_plugins  # type:ignore[import-untyped]
from ansible.utils.plugin_docs import get_plugin_docs  # type:ignore
from io import StringIO
from suitable.runner_results import RunnerResults
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

# Turn off deprecation warnings
C.DEPRECATION_WARNINGS = False
# Make sure we can load all the collection plugins we want to
init_plugin_loader([])
core_version_hint_above = (2, 13)
ansible_version_hint_above = (6, )
reference_re = re.compile(r'([MLBIUROCVEP]|RV)\(([^)]+)\)')
meth_module_re = re.compile(r'(:meth:`[^`]*`\s+)module')
modules_py = StringIO()
modules_header_py = StringIO()
types_py = StringIO()
type_map = {
    'string': 'str',
    'raw': 'str',
    'str': 'str',
    'int': 'int',
    'float': 'float',
    'bool': 'bool',
    # NOTE: Technically you can construct a `PathLike` that will not work
    #       but since pretty much all of them convert to str just fine
    #       we accept it anyways
    'path': 'StrPath',
    'list': 'Sequence',
    'dict': 'Mapping',
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
            type_name not in ('Mapping', 'Sequence', 'Incomplete')
            and 'default' in meta
            and (default := meta['default']) is not None
        ):
            if type_name == 'bool':
                default = True if default in ('yes', True) else False

            default_type = type(default).__name__
            if default_type == 'AnsibleUnicode':
                default_type = 'str'
            elif default_type == 'AnsibleSequence':
                default_type = 'str'
                # we don't want to render this
                default = ' '

            if default_type == 'str' and ' ' in default:
                # likely a description
                print_default = False
            elif type_name != 'StrPath' and type_name != default_type:
                if default_type == 'str':
                    # likely a description
                    print_default = False
                else:
                    type_name = f'{default_type} | {type_name}'

        if type_name == 'Sequence':
            element_type = type_map.get(meta.get('elements', ''), 'Incomplete')
            if element_type == 'Mapping':
                element_type = 'Mapping[str, Incomplete]'
            type_name = f'{type_name}[{element_type}]'
            # NOTE: Technically Ansible will turn scalar values into
            #       1-element lists automatically, so we could accept
            #       `sequence | scalar`, but that probably defeats the
            #       purpose of static typing. I'd rather be a little bit
            #       more strict here. There's already plenty of other
            #       argument types where Ansible is more forgiviing.

        elif type_name == 'Mapping':
            type_name = 'Mapping[str, Incomplete]'

        elif (
            type_name == 'str'
            and 'choices' in meta
            # this means we need to support arbitrary strings
            and '*regex*' not in (raw_choices := meta['choices'])
        ):
            choices = ', '.join(repr(choice) for choice in raw_choices)
            # NOTE: This is just a heuristic, we may need to adjust this
            if len(choices) > 35:
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

    name = 'assert_' if module_name == 'assert' else module_name
    modules_py.write(f'    def {name}(')
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

        line = content[start:end].replace('\u00a0', ' ')
        yield f'{indent}{line}\n'
        start = end + 1
        end = start + max_chars_per_line

    #  so we don't emit an empty extra line in some edge-cases
    if start < len(content):
        line = content[start:].replace('\u00a0', ' ')
        yield f'{indent}{line}\n'


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
            value = value.rsplit('.', 1)[-1]
            value = value.replace(' ', '\u00a0')
            return f':meth:`{value}`'
        elif mode == 'P':
            # plugin
            type_idx = value.find('#')
            if type_idx > 0:
                value = value[:type_idx]

            value = value.replace(' ', '\u00a0')
            return f'``{value}``'
        # be generous about accepting either as either
        elif mode in 'UL':
            if ',' in value:
                # link
                label, href = value.rsplit(',', 1)
                label = label.replace(' ', '\u00a0')
                return f'`{label} <{href.strip()}>`__'
            else:
                # url
                # NOTE: The Ansible docs reference an old class name
                url = value.replace('re.MatchObject', 're.Match')
                fragment_idx = url.find('#')
                if fragment_idx > 0:
                    name = url[fragment_idx + 1:].replace(' ', '\u00a0')
                else:
                    name = 'reference'
                return f'`{name}\u00a0<{url}>`__'
        elif mode == 'B':
            # bold
            return f'**{value}**'
        elif mode == 'I':
            # italic
            return f'*{value}*'
        elif mode == 'R':
            # sphinx reference
            name, _ = value.split(',')
            name = name.replace(' ', '\u00a0')
            return f'``{name}``'
        elif mode in ('O', 'C', 'V', 'RV', 'E'):
            if isinstance(value, str):
                # NOTE: Values are already escaped, so we need to unescape
                #       so we don't double escape.
                #       We also replace spaces with non-breaking spaces
                #       so our line-splitter can't split there.
                value = value.replace('\\\\', '\\').replace(' ', '\u00a0')
            return f'``{value}``'
        else:
            raise ValueError(f'Unknown reference mode {mode}')

    return meth_module_re.sub(
        lambda match: match.group(1) + 'method',
        reference_re.sub(
            replace,
            # remove any raw sphinx references
            content.replace(':ref:', '')
        )
    ).replace('\\', '\\\\')


def write_docstring_line(content: str, level: int = 0) -> None:
    content = prepare_docstring_line(content)
    for line in split_docstring_lines(content, level):
        modules_py.write(line)


def write_function_docstring(options: dict[str, Any] | None) -> None:
    global exceeded_line_limit
    description = docs['short_description'].replace('\n', ' ').strip(' \t')
    # ansible docs are inconsistent about using periods
    if description[-1] != '.':
        description = f'{description}.'
    write_docstring_line(description)

    # for some reason these modules are missing from the documentation
    # so we can't link to the ansible documentation
    if module_name in ('yum', 'include'):
        ref = f'`{collection}`'
    else:
        ref = (
            f':ref:`{collection} <ansible_collections.'
            f'{collection}.{module_name}_module>`'
        )
        if len(ref) > 67:
            exceeded_line_limit = True
        modules_py.write(
            '\n        .. seealso::\n'
            f'            {ref}\n'
        )

    if version(added := docs.get('version_added', 0)) > version_hint_above:
        modules_py.write(
            f'\n        .. note:: Requires {version_hint_package} >= {added}\n'
        )

    if conflicts := docs.get('conflicts'):
        modules_py.write(
            '\n'
            '        .. warning::\n'
        )
        nb_ref = ref.replace(' ', '\u00a0')
        warning = (
            'The documentation is referring to the module '
            f'from {nb_ref}, there are however other collections '
            'with the same module name, so depending on your '
            'environment you may be getting one of those instead.'
        )
        for line in split_docstring_lines(warning, 1):
            modules_py.write(line)
        modules_py.write('\n            Conflicting collections:\n\n')
        for conflict in sorted(conflicts[1:]):
            reference = (
                f'            * :ref:`{conflict} '
                f'<ansible_collections.{conflict}.{module_name}_module>`\n'
            )
            if len(reference) > 79:
                exceeded_line_limit = True
            modules_py.write(reference)

    if options:
        modules_py.write('\n')

    # free form parameters should have already been popped off the options
    # so we don't need to special case them
    for name, meta in (options or {}).items():
        modules_py.write(f'        :param {name}:\n')
        description = meta['description']
        if isinstance(description, str):
            description = [description]
        for line in description:
            line = line.replace('\n', ' ').replace('  ', ' ').strip(' \t')
            if not line:
                continue

            # lines are not consistently terminated
            if line[-1] != '.':
                line += '.'
            write_docstring_line(line, level=1)

        added = meta.get('version_added')
        if added and version(added) > version_hint_above:
            modules_py.write(
                f'            Requires {version_hint_package} >= {added}\n'
            )


def write_return_type(returns: dict[str, Any] | None) -> None:
    assert RunnerResults.__doc__
    types_py.write(
        '\n\n@type_check_only\n'
        f'class {return_type_name}(RunnerResults):\n'
        f'    """{RunnerResults.__doc__[:-4]}'
    )
    if not returns:
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
        elif return_type == 'complex':
            # TODO: This seems to be more or less an alias to dict
            #       but it contains a schema for the contents. If it
            #       is always dict, then try to merge this with dict
            #       and generate a TypedDict using `contains`.
            return_type = 'Incomplete'
        suffix = '  # type:ignore[override]' if name == 'values' else ''
        if len(name) + len(return_type) + len(suffix) > 33:
            # signature doesn't fit on one line
            types_py.write(
                f'\n    def {name}({suffix}\n'
                '        self,\n'
                '        server: str | None = None\n'
                f'    ) -> {return_type}:\n'
            )
        else:
            types_py.write(
                f'\n    def {name}(self, server: str | None = None)'
                f' -> {return_type}:{suffix}\n'
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

        condition = prepare_docstring_line(
            meta.get('returned', 'unspecified')
        )
        if condition.startswith('When') or condition.startswith('when'):
            condition = condition[5:]
        types_py.write('\n')
        for line in split_docstring_lines(f'Returned when: {condition}'):
            types_py.write(line)

        added = meta.get('version_added')
        if added and version(added) > version_hint_above:
            types_py.write(
                f'\n        .. note:: Requires {version_hint_package} '
                f'>= {added}\n'
            )

        global exceeded_line_limit
        if exceeded_line_limit:
            types_py.write('        """  # noqa: E501\n')
            exceeded_line_limit = False
        else:
            types_py.write('        """\n')
        types_py.write(
            f'        return self.acquire(server, \'{name}\')\n'
        )


modules: dict[str, tuple[str, dict[str, Any], dict[str, Any]]] = {}
for _context in module_loader._get_paths_with_context():
    for plugin in list_plugins('module', [
        # TODO: Do we want to add more collections?
        'ansible.builtin',
        'ansible.netcommon',
        'ansible.posix',
        'ansible.utils',
        'ansible.windows'
    ]):
        collection, name = plugin.rsplit('.', 1)
        if name in modules:
            continue

        try:
            doc, _, returns, _ = get_plugin_docs(
                plugin,
                'module',
                module_loader,
                fragment_loader,
                False
            )
        except Exception:
            print(f'Failed to load {plugin}')
            continue

        modules[name] = (collection, doc, returns)


# we go through all the plugins a second time to collect conflicts
# even amont modules we don't have documentation for
for _context in module_loader._get_paths_with_context():
    for plugin in list_plugins('module'):
        collection, name = plugin.rsplit('.', 1)
        if name not in modules:
            # no conflict
            continue

        conflict, doc, _ = modules[name]
        if conflict == collection:
            # not an actual conflict
            continue

        conflicts = doc.setdefault('conflicts', [conflict])
        if collection not in conflicts:
            conflicts.append(collection)


modules_header_py.write('''\
# This is an auto-generated file. Please don't manually edit.
# Instead call `scripts/generate_module_hints.py`

from __future__ import annotations

from typing import overload, Any, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath
    from collections.abc import Mapping, Sequence
    from suitable._module_types import (
''')
modules_py.write('''\
    )
    from suitable.types import Incomplete


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
current_collection = ''
version_hint_above: tuple[int, ...]
for module_name, (collection, docs, returns) in sorted(
    modules.items(),
    key=lambda i: (i[1][0], i[0])
):
    if collection == 'ansible.builtin':
        version_hint_above = core_version_hint_above
        version_hint_package = 'ansible-core'
    else:
        version_hint_above = ansible_version_hint_above
        version_hint_package = 'ansible'

    if current_collection != collection:
        modules_py.write('\n    #\n')
        types_py.write('\n\n#\n')
        if current_collection:
            modules_py.write(f'    # {current_collection} end\n')
            types_py.write(f'# {current_collection} end\n')
        modules_py.write(
            f'    # {collection} start\n'
            '    #\n'
        )
        types_py.write(
            f'# {collection} start\n'
            '#\n'
        )
        current_collection = collection
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
