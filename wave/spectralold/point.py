from dataclasses import dataclass
from typing import Generic, GenericAlias, TypeVar

T = TypeVar("T")
U = TypeVar("U")


@dataclass
class _Point(Generic[T, U]):
    x: T
    y: U


class _Point_(_Point):
    @classmethod
    def __class_getitem__(cls):
        return GenericAlias


class _Display_(_Point):
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Point(
    _Display_,
    _Point_,
    _Point,
    Generic[T, U],
):
    def __init__(self, x: T, y: U):
        super(Point, self).__init__(x, y)
