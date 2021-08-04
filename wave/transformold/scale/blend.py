from typing import Iterator, List, Sequence

from pytest import approx

from ..base.sinusoid import Sinusoid
from .transform import Transform

from ..base.sound import Sound


class Blend(Transform):
    def __init__(self):
        return

    def _combine_and_order_sinusoids(
        self, sinusoid_generators: Sequence[Iterator[Sinusoid]]
    ) -> Iterator[Sinusoid]:
        """Returns a combined and ordered iterator of sinusoids by frequency."""
        singen_map = {i: singen for i, singen in enumerate(sinusoid_generators)}
        sinusoids: dict[int, Sinusoid] = {
            i: next(singen) for i, singen in singen_map.items()
        }

        while sinusoids:
            next_idx = min(sinusoids.keys(), key=lambda i: sinusoids[i].frequency)
            yield sinusoids[next_idx]
            next_sin = next(sinusoid_generators[next_idx], None)
            if next_sin is None:
                del sinusoids[next_idx]

    def apply(self, sounds: Sequence[Sound], weights: Sequence[float]) -> Sound:
        assert len(sounds) == len(weights)
        weights = [wgt / sum(weights) for wgt in weights]
        sinusoid_generators = [
            (sinusoid.modify_amplitude(wgt) for sinusoid in sound.sinusoids)
            for sound, wgt in zip(sounds, weights)
        ]
        ordered_sinusoids = self._combine_and_order_sinusoids(sinusoid_generators)
        return Sound(ordered_sinusoids)
