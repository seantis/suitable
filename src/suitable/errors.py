from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from suitable.types import ResultData


class SuitableError(Exception):
    pass


class ModuleError(SuitableError):
    def __init__(self, module: str, host: str, result: ResultData) -> None:
        self.module = module
        self.host = host
        self.result = result

    def __str__(self) -> str:
        output = []

        if 'msg' in self.result:
            output.append(f"Message: {self.result['msg']}")

        if 'rc' in self.result:
            output.append(f"Returncode: {self.result['rc']}")

        if 'stdout' in self.result:
            output.append(f"Stdout:\n{self.result['stdout']}")

        if 'stderr' in self.result:
            output.append(f"Stderr:\n{self.result['stderr']}")

        out = '\n'.join(output)
        return f"Error running '{self.module}' on {self.host}\n{out}"


class UnreachableError(SuitableError):
    def __init__(self, module: str, host: str) -> None:
        self.module = module
        self.host = host

    def __str__(self) -> str:
        return f"{self.host} could not be reached"
