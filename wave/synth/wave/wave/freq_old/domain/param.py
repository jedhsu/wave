from __future__ import annotations
from dataclasses import dataclass

from ...base import Bounds
from ..base import Frequency

__all__ = ["SpectralParameters"]


@dataclass(frozen=True)
class _FreqDomainParameters:
    bounds: Bounds[Frequency]
    npoints: int  # number of anchor points


class _Validate_(_FreqDomainParameters):
    def validate(self):
        ...


class _Default_:
    @staticmethod
    def default() -> SpectralParameters:
        return SpectralParameters(
            bot=Frequency(20),
            top=Frequency(20500),
            npoints=100,
        )


class SpectralParameters(_Default_, _FreqDomainParameters):
    def __init__(
        self,
        bot: Frequency,
        top: Frequency,
        npoints: int,
    ):
        return super(SpectralParameters, self).__init__(
            bot,
            top,
            npoints,
        )
