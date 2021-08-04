from dataclasses import dataclass
from typing import Generic, TypeVar

from .bounds import Bounds

__all__ = ["DomainParameters"]

T = TypeVar("T")


@dataclass
class _DomainParameters(Generic[T]):
    type: T
    bounds: Bounds[T]
    npoints: int


class _Validate_(_DomainParameters, Generic[T]):
    @staticmethod
    def validate(type_: T, bounds: Bounds[T], npoints: int):
        assert isinstance(type_, type)
        bounds.validate_bounds()
        assert npoints >= 0, "Number of points must be non-negative."


class DomainParameters(
    _Validate_,
    _DomainParameters,
    Generic[T],
):
    def __init__(
        self,
        type: T,
        bounds: Bounds[T],
        npoints: int,
    ):
        super(DomainParameters, self).__init__(type, bounds, npoints)
