from ansible.plugins.callback import CallbackBase


class SilentCallbackModule(CallbackBase):
    """ A callback module that does not print anything, but keeps tabs
    on what's happening in an Ansible play.

    """

    def __init__(self):
        self.unreachable = {}
        self.contacted = {}

    def runner_on_ok(self, host, result):
        self.contacted[host] = {
            'success': True,
            'result': result
        }

    def runner_on_failed(self, host, result, ignore_errors=False):
        self.contacted[host] = {
            'success': False,
            'result': result
        }

    def runner_on_unreachable(self, host, result):
        self.unreachable[host] = result
