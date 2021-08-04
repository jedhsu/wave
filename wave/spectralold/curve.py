from dataclasses import dataclass
from typing import Generic, Mapping, TypeVar

__all__ = ["Curve"]


T = TypeVar("T")
U = TypeVar("U")


@dataclass
class _Curve(Generic[T, U]):
    mapping: Mapping[T, U]
