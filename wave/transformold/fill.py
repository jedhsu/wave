from typing import Iterator, List

from pytest import approx

from ..base.envelope import Envelope
from ..base.sound import Sound
from ..base.sinusoid import Sinusoid
from .transform import Transform


class Fill(Transform):
    def __init__(self, envelope: Envelope):
        self.__envelope = envelope

    #######
    @property
    def envelope(self) -> Envelope:
        return self.__envelope

    def apply(self, sound: Sound) -> Sound:
        sinusoids = (
            # TODO: this can be add envelope method in Sinusoid
            Sinusoid(
                sinusoid.frequency, sinusoid.amplitude, sinusoid.step, self.envelope
            )
            for sinusoid in sound.sinusoids
        )
        return Sound(sinusoids)
