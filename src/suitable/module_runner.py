from __future__ import annotations

import atexit
import ansible.constants  # type:ignore[import-untyped]
import logging
import os
import signal
import sys

from ansible.executor.task_queue_manager import TaskQueueManager  # type:ignore
from ansible.parsing.dataloader import DataLoader  # type:ignore
from ansible.inventory.manager import InventoryManager  # type:ignore
from ansible.playbook.play import Play  # type:ignore[import-untyped]
from ansible.utils.display import Display  # type:ignore[import-untyped]
from ansible.vars.manager import VariableManager  # type:ignore[import-untyped]
from contextlib import contextmanager
from datetime import datetime
from pprint import pformat
from suitable._modules import AnsibleModules
from suitable.callback import SilentCallbackModule
from suitable.common import log
from suitable.runner_results import RunnerResults
from typing import Any, TYPE_CHECKING

try:
    from ansible import context
except ImportError:
    set_global_context = None
else:
    set_global_context = context._init_global_context

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable
    from suitable.api import Api


if sys.version_info >= (3, 11):
    from datetime import UTC

    def utcnow() -> datetime:
        return datetime.now(UTC)
else:
    utcnow = datetime.utcnow


@contextmanager
def ansible_verbosity(verbosity: int) -> Generator[None, None, None]:
    """ Temporarily changes the ansible verbosity. Relies on a single display
    instance being referenced by the __main__ module.

    This is setup when suitable is imported, though Ansible could already
    be imported beforehand, in which case the output might not be as verbose
    as expected.

    To be sure, import suitable before importing ansible. ansible.

    """
    display = Display()
    previous = display.verbosity
    display.verbosity = verbosity
    yield
    display.verbosity = previous


@contextmanager
def environment_variable(key: str, value: str) -> Generator[None, None, None]:
    """ Temporarily overrides an environment variable. """

    if key not in os.environ:
        previous = None
    else:
        previous = os.environ[key]

    os.environ[key] = value

    yield

    if previous is None:
        del os.environ[key]
    else:
        os.environ[key] = previous


@contextmanager
def host_key_checking(enable: bool) -> Generator[None, None, None]:
    """ Temporarily disables host_key_checking, which is set globally. """

    def as_string(b: bool) -> str:
        return b and 'True' or 'False'

    with environment_variable('ANSIBLE_HOST_KEY_CHECKING', as_string(enable)):
        previous = ansible.constants.HOST_KEY_CHECKING

        ansible.constants.HOST_KEY_CHECKING = enable
        yield
        ansible.constants.HOST_KEY_CHECKING = previous


class SourcelessInventoryManager(InventoryManager):  # type:ignore[misc]
    """ A custom inventory manager that turns the source parsing into a noop.

    Without this, Ansible will warn that there are no inventory sources that
    could be parsed. Naturally we do not have such sources, rendering this
    warning moot.

    """

    if not TYPE_CHECKING:
        def parse_sources(self, *args, **kwargs):
            pass


class ModuleRunner:

    api: Api | None
    module_args: dict[str, Any] | str | None

    def __init__(self, module_name: str) -> None:
        """ Runs any ansible module given the module's name and access
        to the api instance (done through the hookup method).

        """
        self.module_name = module_name
        self.api = None
        self.module_args = None

    def __str__(self) -> str:
        """ Return a represenation of the module, including the last
        run module_args (-> this will end up looking a lot like) an entry
        in an ansible yaml file.

        """
        return f"{self.module_name}: {self.module_args}"

    @property
    def is_hooked_up(self) -> bool:
        return self.api is not None and self.module_name in self.api.__dict__

    def hookup(self, api: Api) -> None:
        """ Hooks this module up to the given api. """

        assert self.module_name not in api.__dict__, (
            f"'{self.module_name}' conflicts with existing attribute"
        )

        self.api = api

        # Create a function with correct __name__ and __doc__ values
        # and memoize it on the Api instance
        def f(*args: Any, **kwargs: Any) -> RunnerResults:
            return self.execute(*args, **kwargs)

        f.__name__ = self.module_name
        if template := getattr(AnsibleModules, self.module_name, None):
            f.__doc__ = template.__doc__
        api.__dict__[self.module_name] = f

        # Also add an alias with a name we can actually easily access
        if self.module_name == 'assert':
            api.__dict__['assert_'] = f

    # TODO: Check whether modules with a free-form argument allow combining
    #       free-form with named parameters.
    #       Check whether more than one free-form parameter is possible.
    def get_module_args(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any]
    ) -> str:
        # escape equality sign, until this is fixed:
        # https://github.com/ansible/ansible/issues/13862
        args_str = ' '.join(args).replace('=', '\\=')

        kwargs_str = ' '.join(
            '{}="{}"'.format(k, v.replace('"', '\\"'))
            for k, v in kwargs.items()
        )

        return ' '.join((args_str, kwargs_str)).strip()

    def execute(self, *args: Any, **kwargs: Any) -> RunnerResults:
        """ Puts args and kwargs in a way ansible can understand. Calls ansible
        and interprets the result.

        """
        assert self.is_hooked_up, "the module should be hooked up to the api"
        assert self.api is not None

        if set_global_context:
            set_global_context(self.api.options)

        # translate parameters that use a reserved keyword
        # TODO: For now async is the only one we know about
        #       but there may be other ones
        if 'async_' in kwargs:
            # with conflicts prefer the real name
            kwargs.setdefault('async', kwargs.pop('async_'))

        # legacy key=value pairs shorthand approach
        module_args: dict[str, Any] | str
        if args:
            self.module_args = module_args = self.get_module_args(args, kwargs)
        else:
            self.module_args = module_args = kwargs

        loader = DataLoader()
        inventory_manager = SourcelessInventoryManager(loader=loader)

        for host, host_variables in self.api.inventory.items():
            inventory_manager._inventory.add_host(host, group='all')
            for key, value in host_variables.items():
                inventory_manager._inventory.set_variable(host, key, value)

        for key, value in self.api.options.extra_vars.items():
            inventory_manager._inventory.set_variable('all', key, value)

        variable_manager = VariableManager(
            loader=loader, inventory=inventory_manager)

        play_source = {
            'name': 'Suitable Play',
            'hosts': 'all',
            'gather_facts': 'no',
            'tasks': [{
                'action': {
                    'module': self.module_name,
                    'args': module_args,
                },
                'environment': self.api.environment,
            }]
        }

        try:
            start = utcnow()
            task_queue_manager = None
            callback = SilentCallbackModule()

            play = Play.load(
                play_source,
                variable_manager=variable_manager,
                loader=loader,
            )

            if self.api.strategy:
                play.strategy = self.api.strategy

            log.info(f'running - {self.module_name}: {module_args}')

            # ansible uses various levels of verbosity (from -v to -vvvvvv)
            # offering various amounts of debug information
            #
            # we keep it a bit simpler by activating all of it during debug,
            # and falling back to the default of 0 otherwise
            verbosity = self.api.options.verbosity == logging.DEBUG and 6 or 0

            with ansible_verbosity(verbosity):

                # host_key_checking is special, since not each connection
                # plugin handles it the same way, we need to apply both
                # environment variable and Ansible constant when running a
                # command in the runner to be successful
                with host_key_checking(self.api.host_key_checking):
                    kwargs = dict(
                        inventory=inventory_manager,
                        variable_manager=variable_manager,
                        loader=loader,
                        options=self.api.options,
                        passwords=getattr(self.api.options, 'passwords', {}),
                        stdout_callback=callback
                    )

                    if set_global_context:
                        del kwargs['options']

                    task_queue_manager = TaskQueueManager(**kwargs)

                    try:
                        task_queue_manager.run(play)
                    except SystemExit:

                        # Mitogen forks our process and exits it in one
                        # instance before returning
                        #
                        # This is fine, but it does lead to a very messy exit
                        # by py.test which will essentially return with a test
                        # that is first successful and then failed as each
                        # forked process dies.
                        #
                        # To avoid this we commit suicide if we are run inside
                        # a pytest session. Normally this would just result
                        # in a exit code of zero, which is good.
                        if 'pytest' in sys.modules:
                            try:
                                atexit._run_exitfuncs()
                            except Exception:
                                pass  # nosec
                            os.kill(os.getpid(), signal.SIGKILL)

                        raise
        finally:
            if task_queue_manager is not None:
                task_queue_manager.cleanup()

            if set_global_context:
                # Ansible 2.8 introduces a global context which persists
                # during the lifetime of the process - for Suitable this
                # singleton/cache needs to be cleared after each call
                # to make sure that API calls do not carry over state.
                #
                # The docs hint at a future inclusion of local contexts, which
                # would of course be preferable.
                from ansible.utils.context_objects import (  # type:ignore
                    GlobalCLIArgs)
                GlobalCLIArgs._Singleton__instance = None

        log.debug(f'took {utcnow() - start} to complete')

        return self.evaluate_results(callback)

    def ignore_further_calls_to_server(self, server: str) -> None:
        """ Takes a server out of the list. """
        assert self.is_hooked_up, "the module should be hooked up to the api"
        assert self.api is not None
        log.error(f'ignoring further calls to {server}')
        del self.api.inventory[server]

    def trigger_event(
        self,
        server: str,
        method: str,
        args: Iterable[Any]
    ) -> None:
        try:
            action = getattr(self.api, method)(*args)

            if action != 'keep-trying':
                self.ignore_further_calls_to_server(server)
        except Exception:
            self.ignore_further_calls_to_server(server)
            raise

    def evaluate_results(
        self,
        callback: SilentCallbackModule
    ) -> RunnerResults:
        """ prepare the result of runner call for use with RunnerResults. """
        assert self.is_hooked_up, "the module should be hooked up to the api"
        assert self.api is not None

        for server, result in callback.unreachable.items():
            log.error(f'{server} could not be reached')
            log.debug(f'ansible-output =>\n{pformat(result)}')

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

            # Add success to result
            result['success'] = success

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
            },
            'unreachable': {
                server: result
                for server, result in callback.unreachable.items()
            }
        }, dry_run=self.api.options.check)
