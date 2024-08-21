from __future__ import absolute_import

import os.path
import mitogen  # type:ignore
import ansible  # type:ignore[import-untyped]

from suitable.api import Api as Base
from suitable.api import install_strategy_plugins
from typing import TYPE_CHECKING


MITOGEN_LOADED = False


def assert_mitogen_support() -> None:

    if mitogen.__version__ <= (0, 2, 6):
        if ansible.__version__.startswith('2.8'):
            raise RuntimeError(
                "Mitogen <= 0.2.6 is incompatible with Ansible 2.8")


def is_mitogen_supported() -> bool:
    try:
        assert_mitogen_support()
    except RuntimeError:
        return False
    else:
        return True


def load_mitogen() -> None:
    global MITOGEN_LOADED

    assert_mitogen_support()

    try:
        import ansible_mitogen  # type:ignore
    except ImportError as err:  # pragma: no cover
        raise RuntimeError(
            "Mitogen could not be found. Is it installed?"
        ) from err

    strategy_path = os.path.join(
        os.path.dirname(ansible_mitogen.__file__),
        'plugins/strategy'
    )

    install_strategy_plugins(strategy_path)
    MITOGEN_LOADED = True


class Api(Base):
    """ The Suitable Api with Mitogen integration. """

    # retain arguments from base class
    if not TYPE_CHECKING:
        def __init__(self, *args, **kwargs):
            if not MITOGEN_LOADED:
                load_mitogen()

            if 'strategy' not in kwargs:
                kwargs['strategy'] = 'mitogen_linear'

            super().__init__(*args, **kwargs)
