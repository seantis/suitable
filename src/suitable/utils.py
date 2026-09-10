from __future__ import annotations

from ansible import __version__  # type:ignore[import-untyped]
from packaging.version import Version

from typing import Any, TYPE_CHECKING


ANSIBLE_VERSION = Version(__version__)
ANSIBLE12 = ANSIBLE_VERSION >= Version('2.19')  # ruff:ignore[yoda-conditions]
ANSIBLE14 = ANSIBLE_VERSION >= Version('2.21')  # ruff:ignore[yoda-conditions]


class Options:
    if TYPE_CHECKING:
        def __getattr__(self, key: str) -> Any: ...


def options_as_class(dictionary: dict[str, Any]) -> Options:

    options = Options()
    options.__dict__.update(dictionary)

    return options
