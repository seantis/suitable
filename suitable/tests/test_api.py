from suitable.tests import TestCase
from suitable.api import list_ansible_modules, Api
from suitable.errors import UnreachableError


class TestApi(TestCase):

    def test_list_ansible_modules(self):
        modules = list_ansible_modules()

        # look for some basic modules
        self.assertIn('command', modules)
        self.assertIn('file', modules)
        self.assertIn('user', modules)

    def test_unreachable(self):
        host = Api('255.255.255.255')

        self.assertIn('255.255.255.255', host.servers)
        self.assertRaises(UnreachableError, host.command, 'whoami')
        self.assertNotIn('255.255.255.255', host.servers)

    def test_ignore_unreachable(self):
        host = Api('255.255.255.255', ignore_unreachable=True)

        self.assertIn('255.255.255.255', host.servers)
        host.command('whoami')
        self.assertIn('255.255.255.255', host.servers)

    def test_custom_unreachable(self):
        class MyApi(Api):
            unreachable = []

            def on_unreachable_host(self, module, host):
                self.unreachable.append(host)
                return 'keep-trying'

        host = MyApi('255.255.255.255')
        
        host.command('whoami')
        self.assertEqual(len(host.unreachable), 1)

        host.command('whoami')
        self.assertEqual(len(host.unreachable), 2)

        host.command('whoami')
        self.assertEqual(len(host.unreachable), 3)
