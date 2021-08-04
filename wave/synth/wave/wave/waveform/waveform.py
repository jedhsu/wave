from __future__ import annotations

import numpy as np

from .base import _Waveform


class Waveform(_Waveform):
    def __init__(self, vector: np.ndarray):
        self._vector = vector

    @staticmethod
    def initialize(uvparam: UVParam) -> Waveform:


