import __main__

from ansible.utils.display import Display
__main__.display = Display()

from suitable.api import Api  # noqa
__all__ = ['Api']
