from ansible.plugins.callback import CallbackBase


class SilentCallbackModule(CallbackBase):
    """ A callback module that does not print anything, but keeps tabs
    on what's happening in an Ansible play.

    """

    def __init__(self):
        self.unreachable = {}
        self.contacted = {}

    def v2_runner_on_ok(self, result):
        self.contacted[result._host.name] = {
            'success': True,
            'result': result._result
        }

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.contacted[result._host.name] = {
            'success': False,
            'result': result._result
        }

    def v2_runner_on_unreachable(self, result):
        self.unreachable[result._host.name] = result._result
