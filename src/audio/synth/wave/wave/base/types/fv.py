"""

Frequency vs. Volume.

"""
from ear4.wave import Decibel, Frequency

from ..base import XY

# FrequencySpectrum


class FreqVolume(XY):

    _xy = XY(Frequency, Decibel)
