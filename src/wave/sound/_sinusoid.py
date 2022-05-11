"""

    *Sinusoid*

"""

from dataclasses import dataclass


@dataclass
class Sinusoid:
    frequency: float
    amplitude: float = 1
    # phase: float


def compute_position(sinusoid: Sinusoid):
    ...
