"""

Window function.

"""

from enum import Enum


class __WindowFunction(Enum):
    Rectangular = "Rectangular"
    Triangular = "Triangular"
    Hann = "Hann"


class WindowFunction:
    ...
