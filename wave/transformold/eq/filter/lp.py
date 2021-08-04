from ..base import Frequency
from .vec import Vector


def get_cutoff_ratio(frequency: Frequency, sample_rate: SampleRate):
    ...


def from_range(start: usize, stop: usize) -> Vector:
def lowpass_filter(cutoff: Frequency, band: Frequency) -> Vector[Frequency]:
    ...

def spectral_invert():
    ...

def highpass_filter(cutoff: Frequency, band: Frequency):
    ...

def highpass_filter(cutoff: Frequency, band: Frequency):
    ...
