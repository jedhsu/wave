"""

    Frequency

  Number of wave cycles per second.

"""


from __future__ import annotations
import math

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


class _From_:
    @staticmethod
    def from_period(per: Period) -> Frequency:
        return Frequency(1.0 / per)

    @staticmethod
    def from_angular(omega: AngularFrequency):
        return Frequency(omega / (2 * math.pi))

    @staticmethod
    def from_radians():
        pass


class _Into_(_Frequency):
    def into_period(self) -> Period:
        return Period(1 / self)

    def into_angular(self) -> AngularFrequency:
        return AngularFrequency(2 * math.pi * self)

    def into_radians(self) -> Radians:
        # [TODO] figure this out
        raise NotImplementedError


class _Convert_(_From_, _Into_):
    pass


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
