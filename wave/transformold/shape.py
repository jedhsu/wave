from typing import List, Iterator


from ..sound.sound import Sound
from ..base.envelope import Envelope
from .transform import Transform

from pytest import approx

# TODO: SHAPE AND FILL MIGHT BE THE SAME!
class Scale(Transform):
    def __init__(self, sound: Sound, envelope: Envelope):
        self.__sound = sound
        self.__envelope = envelope

    #######
    @property
    def sound(self) -> Sound:
        """Input sound."""
        return self.__sound

    @property
    def envelope(self) -> Envelope:
        return self.__envelope

    @property
    def waveform(self) -> Iterator[float]:
        ret = 0
        for sound, weight in zip(self.sounds, self.weights):
            position = yield from sound.waveform
            ret += weight * position
        return ret
