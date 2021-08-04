from typing import NamedTuple

from .wave import Wave

# TODO: this should really be mutable..
class _Sinusoid(NamedTuple):
    amplitude: Amplitude
    frequency: Frequency
    phase: Phase


def compute_position(sinusoid: Sinusoid):
    ...


class Sinusoid(Wave):
    ...
