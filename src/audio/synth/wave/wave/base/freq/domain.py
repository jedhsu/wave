"""

Anchor frequency point.

"""


from dataclasses import dataclass

from ...energy import Decibel
from ..base import Frequency

__all__ = ["FrequencyAnchor"]


@dataclass
class _FrequencyAnchor:
    frequency: Frequency
    gain: Decibel  # just stick with db first


@dataclass
class _Validate_:
    frequency_range = (Frequency(10), Frequency(22000))
    gain_range = (Decibel(-30), Decibel(30))


class FrequencyAnchor(_FrequencyAnchor):
    def __init__(
        self,
        freq: Frequency,
        gain: Decibel,
    ):
        super(FrequencyAnchor, self).__init__(freq, gain)
