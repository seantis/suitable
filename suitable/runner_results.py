class RunnerResults(dict):
    """ Wraps the results of parsed module_runner output. The result may
    be used just like it is in Ansible:

    result['contacted']['server']['rc']

    or it can alternatively be used thusly:

    result.rc('server')

    """

    def __init__(self, results):
        self.update(results)

    def __getattr__(self, key):
        return lambda server: self.acquire(server, key)

    def acquire(self, server, key):
        if server not in self['contacted']:
            return None

        return self['contacted'][server][key]
