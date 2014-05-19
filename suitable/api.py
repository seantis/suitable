import os

from contextlib import contextmanager
from ansible.utils.plugins import module_finder

from suitable.module_runner import ModuleRunner
from suitable.errors import UnreachableError, ModuleError


class Api(object):
    """ The api is a kind of proxy to the Ansible API. It goes through the
    list of modules offered by Ansible and hooks them up to itself. This means
    that a module like the 'sync' module of ansible is made available as
    a local function:

    api = Api('personal.server.dev')
    api.sync(src='/Users/denis/.zshrc', dest='/home/denis/.zshrc')

    The function is actually not defined on the api, the attribute simply
    points to the 'execute' function of each module runner instance which is
    hooked up to the Api. (see suitable.module_runner.ModuleRunner).
)

    """

    def __init__(
        self, servers,
        ignore_unreachable=False,
        ignore_errors=False,
        **runner_args
    ):
        """ Initializes the api.

        :servers:
            A list of servers or a string with space-delimited servers. The
            api instances will operate on these servers only. Servers which
            cannot be reached or whose use triggers an error are taken out
            of the list for the lifetime of the object.

            e.g: ['server1', 'server2'] or 'server' or 'server1 server2'.

        :ignore_unreachable:
            If true, unreachable servers will not trigger an exception. They
            are however still taken out of the list for the lifetime of the
            object.

        :ignore_errors:
            If true, errors on servers will not trigger an exception. Servers
            who trigger an error are still ignored for the lifteime of the
            object.

        :**runner_args:
            All remining keyword arguments are passed to the Ansible runner
            initializiation. A common option would be sudo:

            Api('myserver', sudo=True)

        """
        if isinstance(servers, basestring):
            self.servers = servers.split(u' ')
        else:
            self.servers = servers

        self.runner_args = runner_args
        self._valid_return_codes = (0, )

        self.ignore_unreachable = ignore_unreachable
        self.ignore_errors = ignore_errors

        for runner in (ModuleRunner(m) for m in list_ansible_modules()):
            runner.hookup(self)

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

        Should be used as a context:

            with api.valid_return_codes(0, 1):
                api.shell('test -e /tmp/log && rm /tmp/log')

        """
        previous_codes = self._valid_return_codes
        self._valid_return_codes = codes

        yield

        self._valid_return_codes = previous_codes


def list_ansible_modules():

    # constant and code copied from ansible
    # https://github.com/ansible/ansible/blob/devel/bin/ansible-doc

    BLACKLIST_EXTS = ('.swp', '.bak', '~', '.rpm')
    paths = (p for p in module_finder._get_paths() if os.path.isdir(p))

    modules = []

    for path in paths:
        modules.extend(m for m in os.listdir(path) if m not in BLACKLIST_EXTS)

    return modules
