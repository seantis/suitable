def options_as_class(dictionary):

    class Options(object):
        pass

    options = Options()

    for key, value in dictionary.items():
        setattr(options, key, value)

    return options
