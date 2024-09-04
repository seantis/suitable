from __future__ import annotations

import logging
import os

from ansible import __version__, constants  # type:ignore[import-untyped]
from ansible.plugins.loader import module_loader  # type:ignore[import-untyped]
from ansible.plugins.loader import strategy_loader
from contextlib import contextmanager
from packaging.version import Version
from suitable._modules import AnsibleModules
from suitable.errors import UnreachableError, ModuleError
from suitable.module_runner import ModuleRunner
from suitable.utils import options_as_class
from suitable.inventory import Inventory
from typing import Any, NoReturn, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import StrPath
    from collections.abc import Callable, Generator, Iterable, Sequence
    from suitable.runner_results import RunnerResults
    from suitable.types import Incomplete, ResultData, Verbosity


VERBOSITY: dict[Verbosity, int] = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARN,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


class Api(AnsibleModules):
    """
    Provides all available ansible modules as local functions::

        api = Api('personal.server.dev')
        api.sync(src='/Users/denis/.zshrc', dest='/home/denis/.zshrc')

    """

    def __init__(
        self,
        servers: str | list[str] | dict[str, dict[str, Any]],
        ignore_unreachable: bool = False,
        ignore_errors: bool = False,
        host_key_checking: bool = True,
        sudo: bool = False,
        dry_run: bool = False,
        verbosity: Verbosity = 'info',
        environment: dict[str, str] | None = None,
        strategy: Incomplete | None = None,
        collections_path: str | Sequence[str] | None = None,
        **options: Incomplete
    ):
        """
        :param servers:
            A list of servers, a string with space-delimited servers or a dict
            with server name as key and ansible host variables as values. The
            api instances will operate on these servers only. Servers which
            cannot be reached or whose use triggers an error are taken out
            of the list for the lifetime of the object.

            Examples of valid uses::

                api = Api(['web.example.org', 'db.example.org'])
                api = Api('web.example.org')
                api = Api('web.example.org db.example.org')
                api = Api({'web.example.org': {'ansible_host': '10.10.5.1'}})
                api = Api(['example.org:2222', 'example.org:2223'])


        :param ignore_unreachable:
            If true, unreachable servers will not trigger an exception. They
            are however still taken out of the list for the lifetime of the
            object.

        :param ignore_errors:
            If true, errors on servers will not trigger an exception. Servers
            who trigger an error are still ignored for the lifteime of the
            object.

        :param sudo:
            If true, the commands run as root using sudo. This is a shortcut
            for the following::

                Api('example.org', become=True, become_user='root')

            If ``become`` or ``become_user`` are passed, this option is
            ignored!

        :param sudo_pass:
            If given, sudo is invoked with the given password. Alternatively
            you can use Ansible's builtin password option (e.g.
            ``passwords={'become_pass': '***'}``).

        :param remote_pass:
            Passwords are passed to ansible using the passwords dictionary
            by default (e.g. ``passwords={'conn_pass': '****'}``). Since this
            is a bit cumbersome and because earlier Suitable releases supported
            `remote_pass` this convenience argument exists.

            If `passwords` is passed, the `remote_pass` argument is ignored.

        :param dry_run:
            Runs ansible in 'check' mode, where no changes are actually
            applied to the server(s).

        :param verbosity:
            The verbosity level of ansible. Possible values:

            * ``debug``
            * ``info`` (default)
            * ``warn``
            * ``error``
            * ``critical``

        :param environment:
            The environment variables which should be set during when
            a module is executed. For example::

                api = Api('example.org', environment={
                    'PGPORT': '5432'
                })

        :param strategy:
            The Ansible strategy to use. Defaults to None which lets Ansible
            decide which strategy it wants to use.

            Note that you need to globally install strategy plugins using
            :meth:`install_strategy_plugins` before using strategies provided
            by plugins.

        :param collections_path:
            Provide a custom path or sequence of path to look for ansible
            collections when loading/hooking the modules.

            Ansible only initializes the module loader once, so it's not
            possible to have multiple ``Api`` instances with different
            values for this parameter. The first one will always be the
            one that matters.

            Additionally if the loader has already been initialized prior
            to the creation of the ``Api`` instance, then this parameter has
            no effect at all.

            Requires ansible-core >= 2.15

        :param host_key_checking:
            Set to false to disable host key checking.

        :param extra_vars:

            Extra variables available to Ansible. Note that those will be
            global and not bound to any particular host::

                api = Api('webserver', extra_vars={'home': '/home/denis'})
                api.file(dest="{{ home }}/.zshrc", state='touch')

            This can be used to specify an alternative Python interpreter::

                api = Api('example.org', extra_vars={
                    'ansible_python_interpreter': '/path/to/interpreter'
                })

        :param ``**options``:
            All remining keyword arguments are passed to the Ansible
            TaskQueueManager. The available options are listed here:

            `<http://docs.ansible.com/ansible/developing_api.html>`_

        """
        # Create Inventory
        self.inventory = Inventory(options.get('connection', None),
                                   hosts=servers)

        # Set connection to smart (if not set by user)
        if 'connection' not in options:
            options['connection'] = 'smart'

        # sudo is just a shortcut that is easier to remember than this:
        if not ('become' in options or 'become_user' in options):
            options['become'] = sudo
            options['become_user'] = 'root'

        assert 'module_path' not in options, """
            Suitable does not yet support the setting of a custom module path.
            Please create an issue if you need this feature!
        """
        options['module_path'] = None

        # load all the other defaults required by ansible
        # the following are available as constants:
        required_defaults = (
            'forks',
            'remote_user',
            'private_key_file',
            'become',
            'become_method',
            'become_user'
        )

        for default in required_defaults:
            if default not in options:
                options[default] = getattr(
                    constants,
                    f'DEFAULT_{default.upper()}'
                )

        # unfortunately, not all options seem to have accessible defaults
        options['ssh_common_args'] = options.get('ssh_common_args', None)
        options['ssh_extra_args'] = options.get('ssh_extra_args', None)
        options['sftp_extra_args'] = options.get('sftp_extra_args', None)
        options['scp_extra_args'] = options.get('scp_extra_args', None)
        options['extra_vars'] = options.get('extra_vars', {})
        options['diff'] = options.get('diff', False)
        options['verbosity'] = VERBOSITY.get(verbosity)
        options['check'] = dry_run

        if 'passwords' not in options:
            options['passwords'] = {
                'conn_pass': (
                    options.get('remote_pass') or options.get('conn_pass')
                ),
                'become_pass': (
                    options.get('sudo_pass') or options.get('become_pass')
                )
            }

        # keep host_key_checking around for the runner
        self.host_key_checking = host_key_checking

        self.options = options_as_class(options)
        self._valid_return_codes: tuple[int, ...] = (0, )

        self.ignore_unreachable = ignore_unreachable
        self.ignore_errors = ignore_errors

        self.environment = environment or {}
        self.strategy = strategy

        if collections_path is None:
            collections_path = []
        elif isinstance(collections_path, str):
            collections_path = [collections_path]

        if Version(__version__) >= Version('2.15'):
            import warnings
            from ansible.plugins.loader import init_plugin_loader
            # NOTE: Ansible emits a warning here, but it's harmless to
            #       call this function multiple times, it just doesn't
            #       do anything the second time around.
            #       We don't want to propagate this warning.
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    'ignore',
                    r'AnsibleCollectionFinder has already been configured',
                    UserWarning
                )
                init_plugin_loader(collections_path)

        for module in list_ansible_modules():
            ModuleRunner(module).hookup(self)

    def on_unreachable_host(self, module: str, host: str) -> NoReturn:
        """ If you want to customize your error handling, this would be
        the point to write your own method in a subclass.

        Note that this method is not called if ignore_unreachable is True.

        If the return value of this method is 'keep-trying', the server
        will not be ignored for the lifetime of the object. This enables
        you to practically write your own flavor of 'ignore_unreachable'.

        If an any exception is raised the server WILL be ignored.

        """
        raise UnreachableError(module, host)

    def on_module_error(
        self,
        module: str,
        host: str,
        result: ResultData
    ) -> NoReturn:
        """ If you want to customize your error handling, this would be
        the point to write your own method in a subclass.

        Note that this method is not called if ignore_errors is True.

        If the return value of this method is 'keep-trying', the server
        will not be ignored for the lifetime of the object. This enables
        you to practically write your own flavor of 'ignore_errors'.

        If an any exception is raised the server WILL be ignored.

        """
        raise ModuleError(module, host, result)

    def is_valid_return_code(self, code: int) -> bool:
        return code in self._valid_return_codes

    @contextmanager
    def valid_return_codes(self, *codes: int) -> Generator[None, None, None]:
        """ Sets codes which are considered valid when returned from
        command modules. The default is (0, ).

        Should be used as a context::

            with api.valid_return_codes(0, 1):
                api.shell('test -e /tmp/log && rm /tmp/log')

        """
        previous_codes = self._valid_return_codes
        self._valid_return_codes = codes

        yield

        self._valid_return_codes = previous_codes

    if TYPE_CHECKING:
        # Fallback for any modules we don't have auto-generated stubs for
        def __getattr__(self, key: str) -> Callable[..., RunnerResults]: ...


def install_strategy_plugins(directories: Iterable[StrPath] | str) -> None:
    """ Loads the given strategy plugins, which is a list of directories,
    a string with a single directory or a string with multiple directories
    separated by colon.

    As these plugins are globally loaded and cached by Ansible we do the same
    here. We could try to bind those plugins to the Api instance, but that's
    probably not something we'd ever have much of a use for.

    Call this function before using custom strategies on the :class:`Api`
    class.

    """
    if isinstance(directories, str):
        directories = directories.split(':')

    for directory in directories:
        strategy_loader.add_directory(directory)


def list_ansible_modules() -> set[str]:
    # inspired by
    # https://github.com/ansible/ansible/blob/devel/bin/ansible-doc

    paths = (p for p in module_loader._get_paths() if os.path.isdir(p))

    modules: set[str] = set()

    for path in paths:
        modules.update(m for m in get_modules_from_path(path))

    return modules


def get_modules_from_path(path: StrPath) -> Generator[str, None, None]:
    blacklisted_extensions = ('.swp', '.bak', '~', '.rpm', '.pyc')
    blacklisted_prefixes = ('_', )

    assert os.path.isdir(path)

    subpaths = list((os.path.join(path, p), p) for p in os.listdir(path))

    for path, name in subpaths:
        if name.endswith(blacklisted_extensions):
            continue
        if name.startswith(blacklisted_prefixes):
            continue
        if os.path.isdir(path):
            for module in get_modules_from_path(path):
                yield module
        else:
            yield os.path.splitext(name)[0]
