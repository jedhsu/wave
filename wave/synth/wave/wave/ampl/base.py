"""

Amplitude and its different forms.

"""

from abc import ABCMeta
from typing import TypeVar

__all__ = ["Ampl"]


# wrappers of immutable floats


class Ampl(metaclass=ABCMeta):
    Amplitude = TypeVar("Amplitude")
    Decibel = TypeVar("Decibel")
    Power = TypeVar("Power")
    Phon = TypeVar("Phon")


"""

Four forms of amplitude subclass base type and wrap immutable float.

"""


class Amplitude(Ampl, float):
    def __init__(self, value):
        """Wraps immutable float."""
        super(Amplitude, self).__new__(float, value)


class Decibel(Ampl, float):
    def __init__(self, value):
        """Wraps immutable float."""
        super(Decibel, self).__new__(float, value)


class Power(Ampl, float):
    def __init__(self, value):
        """Wraps immutable float."""
        super(Power, self).__new__(float, value)


class Phon(Ampl, float):
    def __init__(self, value):
        """Wraps immutable float."""
        super(Phon, self).__new__(float, value)


Ampl.Amplitude = Amplitude
Ampl.Decibel = Decibel
Ampl.Power = Power
Ampl.Phon = Phon
