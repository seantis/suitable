import logging
import os

from ansible import constants as C
from ansible.plugins.loader import module_loader
from ansible.plugins.loader import strategy_loader
from contextlib import contextmanager
from suitable.compat import string_types
from suitable.errors import UnreachableError, ModuleError
from suitable.module_runner import ModuleRunner
from suitable.utils import to_host_and_port, options_as_class


VERBOSITY = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARN,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


class Api(object):
    """
    Provides all available ansible modules as local functions::

        api = Api('personal.server.dev')
        api.sync(src='/Users/denis/.zshrc', dest='/home/denis/.zshrc')

    """

    def __init__(
        self, servers,
        ignore_unreachable=False,
        ignore_errors=False,
        host_key_checking=True,
        sudo=False,
        dry_run=False,
        verbosity='info',
        environment=None,
        strategy=None,
        **options
    ):
        """
        :param servers:
            A list of servers or a string with space-delimited servers. The
            api instances will operate on these servers only. Servers which
            cannot be reached or whose use triggers an error are taken out
            of the list for the lifetime of the object.

            Examples of valid uses::

                api = Api(['web.example.org', 'db.example.org'])
                api = Api('web.example.org')
                api = Api('web.example.org db.example.org')

            Each server may optionally contain the port in the form of
            ``host:port``. If the host part is an ipv6 address you need to
            use the following form to specify the port: ``[host]:port``.

            For example::

                api = Api('remote.example.org:2222')
                api = Api('[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:1234')

            Note that there's currently no support for passing the same host
            more than once (like in the case of a bastion host). Ansible
            groups these kind of calls together and only calls the first
            server.

            So this won't work as expected::

                api = Api(['example.org:2222', 'example.org:2223'])

            As a work around you should define aliases for these hosts in your
            ssh config or your hosts file.

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
        if isinstance(servers, string_types):
            self.servers = servers.split(u' ')
        else:
            self.servers = list(servers)

        # if the target is the local host but the transport is not set default
        # to transport = 'local' as it's usually what you want
        if 'connection' not in options:
            for host, port in self.hosts_with_ports:
                if host in ('localhost', '127.0.0.1', '::1'):
                    options['connection'] = 'local'
                    break
            else:
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
                    C, 'DEFAULT_{}'.format(default.upper())
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
        self._valid_return_codes = (0, )

        self.ignore_unreachable = ignore_unreachable
        self.ignore_errors = ignore_errors

        self.environment = environment or {}
        self.strategy = strategy

        for runner in (ModuleRunner(m) for m in list_ansible_modules()):
            runner.hookup(self)

    @property
    def hosts_with_ports(self):
        for server in self.servers:
            yield to_host_and_port(server)

    def on_unreachable_host(self, module, host):
        """ If you want to customize your error handling, this would be
        the point to write your own method in a subclass.

        Note that this method is not called if ignore_unreachable is True.

        If the return value of this method is 'keep-trying', the server
        will not be ignored for the lifetime of the object. This enables
        you to practically write your own flavor of 'ignore_unreachable'.

        If an any exception is raised the server WILL be ignored.

        """
        raise UnreachableError(module, host)

    def on_module_error(self, module, host, result):
        """ If you want to customize your error handling, this would be
        the point to write your own method in a subclass.

        Note that this method is not called if ignore_errors is True.

        If the return value of this method is 'keep-trying', the server
        will not be ignored for the lifetime of the object. This enables
        you to practically write your own flavor of 'ignore_errors'.

        If an any exception is raised the server WILL be ignored.

        """
        raise ModuleError(module, host, result)

    def is_valid_return_code(self, code):
        return code in self._valid_return_codes

    @contextmanager
    def valid_return_codes(self, *codes):
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


def install_strategy_plugins(directories):
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


def list_ansible_modules():
    # inspired by
    # https://github.com/ansible/ansible/blob/devel/bin/ansible-doc

    paths = (p for p in module_loader._get_paths() if os.path.isdir(p))

    modules = set()

    for path in paths:
        modules.update(m for m in get_modules_from_path(path))

    return modules


def get_modules_from_path(path):
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
            if name.endswith('.py'):
                yield name[:-3]
            else:
                yield name
