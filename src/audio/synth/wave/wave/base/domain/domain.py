from dataclasses import dataclass
from typing import Generic, GenericAlias, TypeVar

from .bounds import Bounds
from .param import DomainParameters

__all__ = ["Domain"]


T = TypeVar("T")


@dataclass
class _Domain(Generic[T]):

    type: T
    bounds: Bounds[T]


class _Domain_(_Domain):
    @classmethod
    def __class_getitem__(cls):
        return GenericAlias


class _Display_:
    def __repr__(self):
        ...


class Domain(
    _Display_,
    _Domain_,
    _Domain,
):
    ...
