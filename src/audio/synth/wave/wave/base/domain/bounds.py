from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic, GenericAlias, TypeVar

T = TypeVar("T")


@dataclass
class _Bounds(Generic[T]):
    left: T
    right: T


class _Validate_(_Bounds):
    def validate_bounds(self):
        assert type(self.left) == type(self.right)


class _Bounds_(_Bounds, Generic[T]):
    def length(self) -> T:
        return self.right - self.left


class Bounds(
    _Bounds_,
    _Validate_,
    _Bounds,
    metaclass=ABCMeta,
):
    def __init__(self, left: T, right: T):
        super().__init__(left, right)

    @classmethod
    def __class_getitem__(cls):
        return GenericAlias
