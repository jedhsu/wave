from ear4.wave import Decibel

from ..base import XY

# TODO: do decibel for now


class VolumeVolume(XY):
    def __init__(self):
        super().__init__(Decibel, Decibel)
