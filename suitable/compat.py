import sys

PYTHON_3 = sys.version_info[0] == 3


if PYTHON_3:
    string_types = (str, )
    text_type = str
else:
    string_types = (basestring, )  # noqa
    text_type = unicode  # noqa
