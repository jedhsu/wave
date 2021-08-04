"""

Class for frequency spectral axis.

"""

from dataclasses import dataclass
from typing import Sequence

from ..base import Frequency
from .param import SpectralParameters

__all__ = ["Spectrum"]


@dataclass(frozen=True)
class _Spectrum:
    points: Sequence[Frequency]


class _Spectrum_(_Spectrum):
    def interpolate(self):
        ...


class _Display_(_Spectrum):
    def __repr__(self) -> str:
        # TODO: maybe bold the end points?
        return "\n".join([repr(p) for p in self.points])


class FreqDomain(
    _Display_,
    _Spectrum_,
    _Spectrum,
):
    def __init__(self, points: Sequence[Frequency]):
        super(Spectrum, self).__init__(points)

    @staticmethod
    def construct_with(param: SpectralParameters):
        ...
