"""
    
    Coefficients

  Base type for Fourier coefficients.

"""

__all__ = ["Coefficients"]

from abc import ABCMeta
from dataclasses import dataclass
from typing import Iterator

from .math import Function


@dataclass(frozen=True)
class _Coefficients:
    function: Function


class _Iterate_(Iterator):
    def __next__(self):
        ...

    def __iter__(self):
        return self


class Coefficients(
    _Iterate_,
    metaclass=ABCMeta,
):
    def __init__(self, fn: Function):
        ...
