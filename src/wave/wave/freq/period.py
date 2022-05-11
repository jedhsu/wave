"""

    Period

  Duration of wave cycle.

"""


from __future__ import annotations

from ..time import Duration
from .base import AngularFrequency, Period, Radians
from .base import Frequency as _Frequency


"""

Interfaces
* Convert

"""

# [TODO] State interface
# class _Set_:
#     def _set(self, val: float):
#         self._value = val


# @dataclass
# class _Frequency(_Set_):
#     _value: float


# class _Mutate_(_Frequency):
#     def mutate_frequency(self, val: float):
#         self._set(val)


class _From_(float):
    @staticmethod
    def from_period(per: Period) -> Frequency:
        return Frequency(1.0 / per)

    def from_angular(self):
        pass

    def from_radians(self):
        pass


class _Into_(float):
    def into_angular_frequency(self) -> AngularFrequency:
        ...

    def into_radians(self) -> Radians:
        ...

    def into_period(self) -> Duration:
        return Duration(1 / self)


class _Convert_(_From_, _Into_):
    def from_angular_frequency(self):
        ...


class _Unit_:
    unit = "Hz"
    symbol = "f"


class _Display_(
    _Unit_,
    _Frequency,
):
    def __repr__(self) -> str:
        return f"{self} {self.unit}"


class Frequency(float):
    def __init__(self, value):
        super(Frequency, self).__new__(float, value)
