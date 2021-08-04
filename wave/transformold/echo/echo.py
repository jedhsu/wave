from typing import List, Iterator

from ..sound.sound import Sound
from .transform import Transform

from pytest import approx


class Echo(Transform):
    def __init__(self, sounds: List[Sound], weights: List[float]):
        self.__sounds = sounds
        self.__weights = weights

    def __post_init_(self):
        assert sum(self.weights) == approx(1), "Weights must sum to 1."

    #######
    @property
    def sounds(self) -> List[Sound]:
        return self.__sounds

    @property
    def weights(self) -> List[float]:
        return self.__weights

    @property
    def waveform(self) -> Iterator[float]:
        ret = 0
        for sound, weight in zip(self.sounds, self.weights):
            position = yield from sound.waveform
            ret += weight * position
        return ret
