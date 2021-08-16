"""

    Wave

  Main wave type.

"""

from __future__ import annotations
from dataclasses import dataclass
from typing import MutableSequence

__all__ = ["Wave"]


class Wave:
    waveform: Waveform

class Ops:
    """
    Transform operators.

    """
    
    def __add__(self, w: Wave) -> Wave:
    def convolve(self):
        ...
    def eq(self) -> Wave:
        ...


class Wave(_Fields, Ops):
    ...
