"""

    Amplitude

  Models amplitude ratio.

"""


from __future__ import annotations
from math import log

from ..freq import Frequency
from .base import Decibel, Phon, Power
from .base import Amplitude as _Amplitude

__all__ = ["Amplitude"]


# def new(value: float) -> Amplitude:
#     ...


"""

[Interfaces]
* Validate
* Convert (From, Into)
* Display (Unit)

"""


class _Validate_(_Amplitude):
    def validate(self) -> bool:
        """
        Validates value.

        """
        if not 0.0 <= self <= 1.0:
            raise ValueError("Amplitude must be between 0 and 1.")

        return True


class _From_:
    @staticmethod
    def from_decibel(db: Decibel) -> _Amplitude:
        return _Amplitude(10.0 ** (db / 20))


class _Convert_(
    _From_,
    _Into_,
):
    pass


class _Unit_:
    unit = None  # [TODO] confirm this is no units


class _Display_(_Unit_):
    def __repr__(self) -> str:
        number = f"{self:.3f}"
        return f"{number} {self.unit}" if self.unit else number


class Amplitude(
    _Display_,
    _Convert_,
    _Validate_,
    _Amplitude,
):
    def __init__(self, val: float):
        """
        Hooks validator to init.
        """

        super(Amplitude, self).__init__(val)
        self.validate()
