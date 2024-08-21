from __future__ import annotations

import logging


log = logging.getLogger('suitable')


class NullHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        pass


log.addHandler(NullHandler())
