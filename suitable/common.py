import logging
log = logging.getLogger('suitable')


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


log.addHandler(NullHandler())
