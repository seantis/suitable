import __main__

from ansible.utils.display import Display  # type:ignore[import-untyped]
__main__.display = Display()

from suitable.api import Api  # noqa: E402
from suitable.api import install_strategy_plugins  # noqa: E402

__all__ = ('Api', 'install_strategy_plugins')
