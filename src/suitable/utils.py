from __future__ import annotations

from typing import Any, TYPE_CHECKING


class Options:
    if TYPE_CHECKING:
        def __getattr__(self, key: str) -> Any: ...


def options_as_class(dictionary: dict[str, Any]) -> Options:

    options = Options()
    options.__dict__.update(dictionary)

    return options
