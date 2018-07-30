import os.path

from suitable.api import Api as Base
from suitable.api import install_strategy_plugins


MITOGEN_LOADED = False


def load_mitogen():
    global MITOGEN_LOADED

    try:
        import ansible_mitogen
    except ImportError:  # noqa
        raise RuntimeError("Mitogen could not be found. Is it installed?")

    strategy_path = os.path.join(
        os.path.dirname(ansible_mitogen.__file__),
        'plugins/strategy'
    )

    install_strategy_plugins(strategy_path)
    MITOGEN_LOADED = True


class Api(Base):
    """ The Suitable Api with Mitogen integration. """

    def __init__(self, *args, **kwargs):
        if not MITOGEN_LOADED:
            load_mitogen()

        if 'strategy' not in kwargs:
            kwargs['strategy'] = 'mitogen_linear'

        super(Api, self).__init__(*args, **kwargs)
