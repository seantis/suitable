from __future__ import annotations

from typing import Any, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from suitable.types import ResultData
    from typing import Dict
    from typing_extensions import TypedDict

    class _RunnerResults(TypedDict):
        contacted: dict[str, ResultData]
        unreachable: dict[str, ResultData]

    _Base = Dict[str, Dict[str, ResultData]]
else:
    _Base = dict


class ResultsCallback(Protocol):
    def __call__(self, server: str | None = None) -> Any: ...


class RunnerResults(_Base):
    """
    Wraps the results of parsed module_runner output.

    The result may be used just like it is in Ansible::

        result['contacted']['server']['rc']

    or it can alternatively be used thusly::

        result.rc('server')

    """

    def __init__(self, results: _RunnerResults, dry_run: bool = False) -> None:
        self.dry_run = dry_run
        self.update(results)  # type:ignore[arg-type]

    def __getattr__(self, key: str) -> ResultsCallback:
        return lambda server=None: self.acquire(server, key)

    def acquire(self, server: str | None, key: str) -> Any:
        contacted = self['contacted']

        # if no server is given and exactly one contacted server exists
        # return the value of said server directly
        if server is None:
            if len(contacted) == 1:
                server = next((k for k in contacted.keys()), None)
            elif contacted:
                raise ValueError(
                    "When contacting multiple servers you need to "
                    "specify which server's result you want"
                )
            elif self.dry_run:
                raise ValueError('Results are not available in dry run')
            elif (unreachable := self['unreachable']):
                raise ValueError(
                    f"{', '.join(unreachable)} could not be contacted"
                )

        if server not in contacted:
            if self.dry_run:
                raise ValueError('Results are not available in dry run')
            raise KeyError(f"{server} could not be contacted")

        if key not in (result := contacted[server]):
            raise AttributeError(key)

        return result[key]
