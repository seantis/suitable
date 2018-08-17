from ansible.plugins.callback import CallbackBase
from suitable.utils import to_server


class SilentCallbackModule(CallbackBase):
    """ A callback module that does not print anything, but keeps tabs
    on what's happening in an Ansible play.

    """

    def __init__(self):
        self.unreachable = {}
        self.contacted = {}

    def adapt_result(self, result):
        host = result._host.name
        port = result._host.vars.get('ansible_port')

        return to_server(host, port), result._result

    def v2_runner_on_ok(self, result):
        server, result = self.adapt_result(result)

        self.contacted[server] = {
            'success': True,
            'result': result
        }

    def v2_runner_on_failed(self, result, ignore_errors=False):
        server, result = self.adapt_result(result)

        self.contacted[server] = {
            'success': False,
            'result': result
        }

    def v2_runner_on_unreachable(self, result):
        server, result = self.adapt_result(result)

        self.unreachable[server] = result
