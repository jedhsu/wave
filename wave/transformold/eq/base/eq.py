"""
    
    Eq

  Base class for equalization effects.

"""

from abc import ABCMeta

from ...base import Effect


__all__ = ["Eq"]


class _Eq_:
    def spectral_diff(self):
        """
        Computes the spectral frequency difference.
        """
        pass


class Eq(
    Effect,
    metaclass=ABCMeta,
):
    ...
