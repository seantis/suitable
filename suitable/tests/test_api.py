import pytest

from suitable.tests import TestCase
from suitable.api import list_ansible_modules, Api
from suitable.errors import UnreachableError, ModuleError


class TestApi(TestCase):

    def test_auto_localhost(self):
        host = Api('localhost')
        assert host.runner_args.get('transport') == 'local'

        host = Api('localhost', transport='smart')
        assert host.runner_args.get('transport') == 'smart'

    def test_results(self):
        result = Api('localhost').command('whoami')
        assert result.rc('localhost') == 0
        assert result.stdout('localhost') is not None
        assert result['contacted']['localhost']['rc'] == 0

        with pytest.raises(AttributeError):
            result.asdf('localhost')

        result['contacted'] = []

        with pytest.raises(KeyError):
            result.rc('localhost')

    def test_results_single_server(self):
        result = Api('localhost').command('whoami')
        assert result.rc() == 0

    def test_results_multiple_servers(self):
        result = Api(['localhost', '127.0.0.1']).command('whoami')
        with pytest.raises(KeyError):
            result.rc()

    def test_servers_list(self):
        host = Api(('localhost', ))
        assert host.command('whoami').rc('localhost') == 0

    def test_valid_return_codes(self):
        host = Api('localhost')
        assert host._valid_return_codes == (0, )

        with host.valid_return_codes(0, 1):
            assert host._valid_return_codes == (0, 1)
            host.shell('whoami | grep -q asdfasdfasdf')

        assert host._valid_return_codes == (0, )

    def test_list_ansible_modules(self):
        modules = list_ansible_modules()

        # look for some basic modules
        assert 'command' in modules
        assert 'file' in modules
        assert 'user' in modules

    def test_module_error(self):
        with pytest.raises(ModuleError):
            # command cannot include pipes
            Api('localhost').command('whoami | less')

    def test_unreachable(self):
        host = Api('255.255.255.255')

        assert '255.255.255.255' in host.servers

        try:
            host.command('whoami')
        except UnreachableError, e:
            assert '255.255.255.255' in str(e)
        else:
            assert False, "an error should have been thrown"

        assert '255.255.255.255' not in host.servers

    def test_ignore_unreachable(self):
        host = Api('255.255.255.255', ignore_unreachable=True)

        assert '255.255.255.255' in host.servers
        host.command('whoami')
        assert '255.255.255.255' in host.servers

    def test_custom_unreachable(self):
        class MyApi(Api):
            unreachable = []

            def on_unreachable_host(self, module, host):
                self.unreachable.append(host)
                return 'keep-trying'

        host = MyApi('255.255.255.255')

        host.command('whoami')
        assert len(host.unreachable) == 1

        host.command('whoami')
        assert len(host.unreachable) == 2

        host.command('whoami')
        assert len(host.unreachable) == 3

    def test_error_string(self):
        try:
            Api('localhost').command('whoami | less')
        except ModuleError, e:
            # we don't have a msg so we mock that out, for coverage!
            e.result['msg'] = '0xdeadbeef'
            error_string = str(e)

            # we don't make many guarantees with the string messages, so
            # a basic somke test suffices here. This is not something to
            # depend on.

            assert '0xdeadbeef' in error_string
            assert 'command: whoami | less' in error_string
            assert 'Returncode: 1' in error_string
        else:
            assert False, "this needs to trigger an exception"
