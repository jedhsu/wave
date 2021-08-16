"""

    *Sampling*

"""

import numpy as np

from .._sinusoid import Sinusoid

from .build import Build


class Sampling(
    Build,
    Sinusoid,
):
    sampling_rate = 44100  # sampling rate
    duration = 1.0  # in seconds

    def into_samples(self) -> np.ndarray:
        return (
            np.sin(
                self.get_angular_frequency()
                * np.arange(self.sampling_rate * self.duration)
                / self.sampling_rate
            )
        ).astype(np.float32)
