from ansible import inventory as ansible_inventory
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars import VariableManager
from datetime import datetime
from pprint import pformat
from suitable.callback import SilentCallbackModule
from suitable.common import log
from suitable.runner_results import RunnerResults


class UncachedInventory(ansible_inventory.Inventory):
    """ Ansible uses an inventory with a global cache, which messes with our
    execution model. We want an inventory to be bound to an api and nothing
    else.

    This Inventory makes sure that no global state is touched.

    """

    def get_hosts(self, *args, **kwargs):
        if hasattr(ansible_inventory, 'HOSTS_PATTERNS_CACHE'):
            ansible_inventory.HOSTS_PATTERNS_CACHE = {}

        return super(UncachedInventory, self).get_hosts(*args, **kwargs)


class ModuleRunner(object):

    def __init__(self, module_name):
        """ Runs any ansible module given the module's name and access
        to the api instance (done through the hookup method).

        """
        self.module_name = module_name
        self.api = None
        self.module_args = None

    def __str__(self):
        """ Return a represenation of the module, including the last
        run module_args (-> this will end up looking a lot like) an entry
        in an ansible yaml file.

        """
        return "{}: {}".format(self.module_name, self.module_args)

    @property
    def is_hooked_up(self):
        return self.api is not None and hasattr(self.api, self.module_name)

    def hookup(self, api):
        """ Hooks this module up to the given api. """

        assert not hasattr(api, self.module_name), """
            '{}' conflicts with existing attribute
        """.format(self.module_name)

        self.api = api

        setattr(api, self.module_name, self.execute)

    def get_module_args(self, args, kwargs):
        # escape equality sign, until this is fixed:
        # https://github.com/ansible/ansible/issues/13862
        args = u' '.join(args).replace('=', '\\=')

        kwargs = u' '.join(u'{}="{}"'.format(
            k, v.replace('"', '\\"')) for k, v in kwargs.items())

        return u' '.join((args, kwargs)).strip()

    def execute(self, *args, **kwargs):
        """ Puts args and kwargs in a way ansible can understand. Calls ansible
        and interprets the result.

        """

        assert self.is_hooked_up, "the module should be hooked up to the api"

        self.module_args = module_args = self.get_module_args(args, kwargs)

        loader = DataLoader()
        variable_manager = VariableManager()
        variable_manager.extra_vars = self.api.options.extra_vars

        # Ansible has some support for host lists, but it assumes at times
        # that these host lists are not in fact lists but a string pointing
        # to a host list file. The easiest way to make sure that Ansible gets
        # what we want is to pass a host list as a string which always contains
        # at least one comma so that ansible knows it's a string of hosts.
        host_list = ','.join(self.api.servers) + ','

        inventory = UncachedInventory(
            loader=loader,
            variable_manager=variable_manager,
            host_list=host_list
        )

        variable_manager.set_inventory(inventory)

        play_source = {
            'name': "Suitable Play",
            'hosts': self.api.servers,
            'gather_facts': 'no',
            'tasks': [{
                'action': {
                    'module': self.module_name,
                    'args': module_args
                }
            }]
        }

        play = Play.load(
            play_source,
            variable_manager=variable_manager,
            loader=loader
        )

        log.info(u'running {}'.format(u'- {module_name}: {module_args}'.format(
            module_name=self.module_name,
            module_args=module_args
        )))

        start = datetime.utcnow()
        task_queue_manager = None
        callback = SilentCallbackModule()

        try:
            task_queue_manager = TaskQueueManager(
                inventory=inventory,
                variable_manager=variable_manager,
                loader=loader,
                options=self.api.options,
                passwords=getattr(self.api.options, 'passwords', {}),
                stdout_callback=callback
            )
            task_queue_manager.run(play)
        finally:
            if task_queue_manager is not None:
                task_queue_manager.cleanup()

        log.info(u'took {} to complete'.format(datetime.utcnow() - start))

        return self.evaluate_results(callback)

    def ignore_further_calls_to_server(self, server):
        """ Takes a server out of the list. """
        log.error(u'ignoring further calls to {}'.format(server))
        self.api.servers.remove(server)

    def trigger_event(self, server, method, args):
        try:
            action = getattr(self.api, method)(*args)

            if action != 'keep-trying':
                self.ignore_further_calls_to_server(server)
        except:
            self.ignore_further_calls_to_server(server)
            raise

    def evaluate_results(self, callback):
        """ prepare the result of runner call for use with RunnerResults. """

        for server, result in callback.unreachable.items():
            log.error(u'{} could not be reached'.format(server))
            log.debug(u'ansible-output =>\n{}'.format(pformat(result)))

            if self.api.ignore_unreachable:
                continue

            self.trigger_event(server, 'on_unreachable_host', (
                self, server
            ))

        for server, answer in callback.contacted.items():

            success = answer['success']
            result = answer['result']

            if 'failed' in result:
                success = False

            if 'rc' in result:
                if self.api.is_valid_return_code(result['rc']):
                    success = True

            if not success:
                log.error(u'{} failed on {}'.format(self, server))
                log.debug(u'ansible-output =>\n{}'.format(pformat(result)))

                if self.api.ignore_errors:
                    continue

                self.trigger_event(server, 'on_module_error', (
                    self, server, result
                ))

        # XXX this is a weird structure because RunnerResults still works
        # like it did with Ansible 1.x, where the results where structured
        # like this
        return RunnerResults({
            'contacted': {
                server: answer['result']
                for server, answer in callback.contacted.items()
            }
        })
