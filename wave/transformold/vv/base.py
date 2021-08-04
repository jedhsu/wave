from ear4.wave import Volume

from ..base import XY


class VolumeVolume(XY):
    def __init__(self):
        super().__init__(Volume, Volume)
