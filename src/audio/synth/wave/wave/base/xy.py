from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic, Type, TypeVar

__all__ = ["XY"]

T = TypeVar("T")
U = TypeVar("U")


@dataclass
class _XY(Generic[T, U]):
    x: T
    y: U


class _XY_:
    ...


class _Validate_(_XY):
    @staticmethod
    def validate_types(x: T, y: U):
        assert type(x) == type
        assert type(y) == type


class _Display_(_XY_):
    def __repr__(self):
        ...


class XY(
    _Display_,
    _Validate_,
    _XY_,
    _XY,
    Generic[T, U],
    metaclass=ABCMeta,
):
    def __init__(self, x: T, y: U):
        super().__init__(x, y)
