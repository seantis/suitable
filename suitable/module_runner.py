from datetime import datetime
from pprint import pformat

from ansible.runner import Runner
from suitable.common import log


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

        if hasattr(api, self.module_name):
            log.warn(u'{} conflicts with existing attribute'.format(self.name))
            return

        self.api = api

        setattr(api, self.module_name, self.execute)

    def get_module_args(self, args, kwargs):
        args = u' '.join(args)
        kwargs = u' '.join(u'{}={}'.format(k, v) for k, v in kwargs.items())

        return u' '.join((args, kwargs)).strip()

    def execute(self, *args, **kwargs):
        """ Puts args and kwargs in a way ansible can understand. Calls ansible
        and interprets the result.

        """

        assert self.is_hooked_up, "the module should be hooked up to the api"

        self.module_args = module_args = self.get_module_args(args, kwargs)

        runner_args = {
            'module_name': self.module_name,
            'module_args': module_args,
            'pattern': 'all',
            'host_list': self.api.servers
        }
        runner_args.update(self.api.runner_args)

        runner = Runner(**runner_args)

        log.info(u'running {}'.format(u'- {module_name}: {module_args}'.format(
            module_name=self.module_name,
            module_args=module_args
        )))
        start = datetime.utcnow()

        results = runner.run()
        log.info(u'took {} to complete'.format(datetime.utcnow() - start))

        return self.parse_results(results)

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

    def parse_results(self, results):
        """ Parses the result of runner call. """

        unreachable_servers = results['dark']

        for server, result in unreachable_servers.items():
            log.error(u'{} could not be reached'.format(server))
            log.debug(u'ansible-output =>\n{}'.format(pformat(result)))

            if self.api.ignore_unreachable:
                continue

            self.trigger_event(server, 'on_unreachable_host', (
                self, server
            ))

        contacted_servers = results['contacted']

        for server, result in contacted_servers.items():
            failure = False

            if 'failed' in result:
                failure = True

            if 'rc' in result:
                if not self.api.is_valid_return_code(result['rc']):
                    failure = True

            if failure:
                log.error(u'{} failed on {}'.format(self, server))
                log.debug(u'ansible-output =>\n{}'.format(pformat(result)))

                if self.api.ignore_errors:
                    continue

                self.trigger_event(server, 'on_module_error', (
                    self, server, result
                ))

        return results
