from __future__ import annotations

from .base import Frequency, Period
from .base import AngularFrequency as _AngularFrequency

__all__ = ["AngularFrequency"]


class _From_:
    @staticmethod
    def from_frequency(freq: Frequency) -> AngularFrequency:
        raise NotImplementedError

    @staticmethod
    def from_period(per: Period) -> AngularFrequency:
        raise NotImplementedError


class _Into_(_AngularFrequency):
    def into_frequency(self) -> Frequency:
        raise NotImplementedError

    def into_period(self) -> Period:
        raise NotImplementedError


class _Convert_(_From_, _Into_):
    pass


class _Unit_:
    unit = "rad / second"  # [TODO] fraction object for units
    symbol = "\u03c9"


class _Display_(_Unit_, _AngularFrequency):
    def __repr__(self) -> str:
        return f"{self} {self.unit}"


class AngularFrequency(
    _Convert_,
    _AngularFrequency,
):
    pass
