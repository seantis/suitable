import pytest

from suitable.tests import TestCase
from suitable.api import list_ansible_modules, Api
from suitable.errors import UnreachableError


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

    def test_list_ansible_modules(self):
        modules = list_ansible_modules()

        # look for some basic modules
        assert 'command' in modules
        assert 'file' in modules
        assert 'user' in modules

    def test_unreachable(self):
        host = Api('255.255.255.255')

        assert '255.255.255.255' in host.servers

        with pytest.raises(UnreachableError):
            host.command('whoami')

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
