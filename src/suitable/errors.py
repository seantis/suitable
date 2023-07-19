class SuitableError(Exception):
    pass


class ModuleError(SuitableError):
    def __init__(self, module, host, result):
        self.module = module
        self.host = host
        self.result = result

    def __str__(self):
        output = []

        if 'msg' in self.result:
            output.append(u"Message: {}".format(self.result['msg']))

        if 'rc' in self.result:
            output.append(u"Returncode: {}".format(self.result['rc']))

        if 'stdout' in self.result:
            output.append(u"Stdout:\n{}".format(self.result['stdout']))

        if 'stderr' in self.result:
            output.append(u"Stderr:\n{}".format(self.result['stderr']))

        return u"Error running '{module}' on {host}\n{output}".format(
            module=self.module,
            host=self.host,
            output='\n'.join(output)
        )


class UnreachableError(SuitableError):
    def __init__(self, module, host):
        self.module = module
        self.host = host

    def __str__(self):
        return u"{host} could not be reached".format(host=self.host)
