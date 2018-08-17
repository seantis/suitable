import logging

from __main__ import display
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from contextlib import contextmanager
from datetime import datetime
from pprint import pformat
from suitable.callback import SilentCallbackModule
from suitable.common import log
from suitable.runner_results import RunnerResults


@contextmanager
def ansible_verbosity(verbosity):
    """ Temporarily changes the ansible verbosity. Relies on a single display
    instance being referenced by the __main__ module.

    This is setup when suitable is imported, though Ansible could already
    be imported beforehand, in which case the output might not be as verbose
    as expected.

    To be sure, import suitable before importing ansible. ansible.

    """
    previous = display.verbosity
    display.verbosity = verbosity
    yield
    display.verbosity = previous


class SourcelessInventoryManager(InventoryManager):
    """ A custom inventory manager that turns the source parsing into a noop.

    Without this, Ansible will warn that there are no inventory sources that
    could be parsed. Naturally we do not have such sources, rendering this
    warning moot.

    """

    def parse_sources(self, *args, **kwargs):
        pass


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
        inventory_manager = SourcelessInventoryManager(loader=loader)

        hosts_with_ports = tuple(self.api.hosts_with_ports)

        for host, port in hosts_with_ports:
            inventory_manager._inventory.add_host(host, group='all', port=port)

        for key, value in self.api.options.extra_vars.items():
            inventory_manager._inventory.set_variable('all', key, value)

        variable_manager = VariableManager(
            loader=loader, inventory=inventory_manager)

        play_source = {
            'name': "Suitable Play",
            'hosts': [h for h, p in hosts_with_ports],  # *must* be a list
            'gather_facts': 'no',
            'tasks': [{
                'action': {
                    'module': self.module_name,
                    'args': module_args,
                },
                'environment': self.api.environment
            }]
        }

        play = Play.load(
            play_source,
            variable_manager=variable_manager,
            loader=loader,
        )

        if self.api.strategy:
            play.strategy = self.api.strategy

        log.info(u'running {}'.format(u'- {module_name}: {module_args}'.format(
            module_name=self.module_name,
            module_args=module_args
        )))

        start = datetime.utcnow()
        task_queue_manager = None
        callback = SilentCallbackModule()

        # ansible uses various levels of verbosity (from -v to -vvvvvv)
        # offering various amounts of debug information
        #
        # we keep it a bit simpler by activating all of it during debug, and
        # falling back to the default of 0 otherwise
        verbosity = self.api.options.verbosity == logging.DEBUG and 6 or 0

        try:
            with ansible_verbosity(verbosity):
                task_queue_manager = TaskQueueManager(
                    inventory=inventory_manager,
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

        log.debug(u'took {} to complete'.format(datetime.utcnow() - start))

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
        except Exception:
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

            # none of the modules in our tests hit the 'failed' result
            # codepath (which seems to not be implemented by all modules)
            # seo we ignore this branch since it's rather trivial
            if result.get('failed'):  # pragma: no cover
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
