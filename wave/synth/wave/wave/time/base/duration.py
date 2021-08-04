"""

Duration base type.

"""

from dataclasses import dataclass

__all__ = ["Duration"]


class _Set_:
    def _set_seconds(self, val: float):
        self.seconds = val


@dataclass
class _Duration(_Set_):
    seconds: float


class _Mutate_(_Duration):
    def update_seconds(self, val: float):
        self._set_seconds(val)


class _Display_(_Duration):
    units: str = "seconds"

    def __repr__(self) -> str:
        return f"{self.seconds} {self.units}"


class Duration(_Display_, _Mutate_, _Duration):
    def __init__(self, seconds: float):
        super(Duration, self).__init__(seconds)
