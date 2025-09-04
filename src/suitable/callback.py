from __future__ import annotations

from ansible.plugins.callback import (  # type:ignore[import-untyped]
    CallbackBase
)
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ansible.executor.task_result import TaskResult  # type:ignore
    from ansible.utils.display import Display  # type:ignore
    from suitable.types import ResultData
    from typing_extensions import TypedDict

    class ContactedResult(TypedDict):
        success: bool
        result: ResultData


class SilentCallbackModule(CallbackBase):  # type:ignore[misc]
    """ A callback module that does not print anything, but keeps tabs
    on what's happening in an Ansible play.

    """

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'silent'

    unreachable: dict[str, ResultData]
    contacted: dict[str, ContactedResult]

    def __init__(
        self,
        display: Display | None = None,
        options: dict[str, Any] | None = None
    ) -> None:
        super().__init__(display, options)
        self.unreachable = {}
        self.contacted = {}

    def v2_runner_on_ok(self, result: TaskResult) -> None:
        self.contacted[result._host.name] = {
            'success': True,
            'result': result._result
        }

    def v2_runner_on_failed(
        self,
        result: TaskResult,
        ignore_errors: bool = False
    ) -> None:

        self.contacted[result._host.name] = {
            'success': False,
            'result': result._result
        }

    def v2_runner_on_unreachable(self, result: TaskResult) -> None:
        self.unreachable[result._host.name] = result._result
