from abc import ABCMeta
from typing import TypeVar

from ..time import Duration


__all__ = ["Freq"]


class Freq(metaclass=ABCMeta):
    Frequency = TypeVar("Frequency")
    Period = TypeVar("Period")
    Angular = TypeVar("Angular")
    Radians = TypeVar("Radians")


"""

Four forms of frequency.

"""

# [TODO] more accurate base measures for Frequency, AngularFrequency


class Frequency(Freq, float):
    """
    Number of cycles per second.

    """

    def __init__(self, value):
        super(Frequency, self).__new__(float, value)


class Period(Freq, Duration):
    """
    Cycle duration (in seconds).

    """

    def __init__(self, value):
        super(Period, self).__new__(Duration, value)


class AngularFrequency(Freq, Duration):
    def __init__(self, value):
        super(AngularFrequency, self).__new__(Duration, value)


class Radians(Freq, float):
    def __init__(self, value):
        super(Radians, self).__new__(float, value)


Freq.Frequency = Frequency
Freq.Period = Period
Freq.Angular = AngularFrequency
Freq.Radians = Radians
