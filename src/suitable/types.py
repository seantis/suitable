from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Literal, TypeAlias

Incomplete: TypeAlias = Any
Verbosity: TypeAlias = Literal[
    'critical',
    'error',
    'warn',
    'info',
    'debug'
]
# TODO: Switch to a TypedDict?
HostVariables: TypeAlias = dict[str, Incomplete]
Hosts: TypeAlias = str | Iterable[str] | dict[str, HostVariables]
ResultData: TypeAlias = Any
