import sys

PYTHON_3 = sys.version_info[0] == 3


if PYTHON_3:
    string_types = (str, )  # pragma: no cover
    text_type = str  # pragma: no cover
else:
    string_types = (basestring, )  # noqa
    text_type = unicode  # noqa
