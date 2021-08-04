from dataclasses import dataclass
from typing import Generic, GenericAlias, TypeVar

from .bounds import Bounds

__all__ = ["Domain"]


T = TypeVar("T")


@dataclass
class _Domain(Generic[T]):

    type: T
    bounds: Bounds[T]
    npoints: int 


class _Domain_(_Domain):


class _Display_:
    def __repr__(self):
        ...


class Domain(
    _Display_,
    _Domain_,
    _Domain,
):
    def __init__(self, type: T, bounds: Bounds
    @classmethod
    def __class_getitem__(cls):
        return GenericAlias
