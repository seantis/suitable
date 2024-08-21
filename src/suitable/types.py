from __future__ import annotations

from typing import Any, Dict, Iterable, Literal, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

Incomplete: TypeAlias = Any
Verbosity: TypeAlias = Literal[
    'critical',
    'error',
    'warn',
    'info',
    'debug'
]
# TODO: Switch to a TypedDict?
HostVariables: TypeAlias = Dict[str, Incomplete]
Hosts: TypeAlias = Union[str, Iterable[str], Dict[str, HostVariables]]
ResultData: TypeAlias = Any
