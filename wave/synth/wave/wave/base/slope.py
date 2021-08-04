from typing import Generic, TypeVar


T = TypeVar("T")
U = TypeVar("U")


class _Slope(Generic[T, U]):
    x: T
    y: U


class _Slope_(_Slope):
    def value(self):
        return self.x._value / self.y._value
