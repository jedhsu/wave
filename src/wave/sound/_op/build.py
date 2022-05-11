"""

    *Build*

"""

import numpy as np

from .._sinusoid import Sinusoid

TAU = 2 * np.pi


class Build(
    Sinusoid,
):
    def get_angular_frequency(self) -> float:
        return TAU * self.frequency
