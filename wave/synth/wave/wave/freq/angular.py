from __future__ import annotations
from dataclasses import dataclass

from ..time import Duration
from .base import Frequency

__all__ = ["AngularFrequency"]


class _Set_:
    def _set(self, val: float):
        self._value = val


@dataclass
class _AngularFrequency(_Set_):
    _value: float


class _Mutate_(_AngularFrequency):
    def mutate(self, val: float):
        self._set(val)


class _From_:
    @staticmethod
    def from_cycle_frequency(freq: Frequency) -> AngularFrequency:
        ...

    @staticmethod
    def from_duration(dur: Duration) -> AngularFrequency:
        ...


class _Into_(_AngularFrequency):
    def into_cycle_frequency(self) -> Frequency:
        ...


class _Convert_(_From_, _Into_):
    ...


class _Display_(_AngularFrequency):
    units = "radians / second"

    def __repr__(self) -> str:
        return f"{self._value} {self.units}"


class AngularFrequency(
    _Convert_,
    _Mutate_,
    _AngularFrequency,
):
    def __init__(self, value: float):
        super(AngularFrequency, self).__init__(value)
