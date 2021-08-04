"""
    
    PureTone

  Model for pure tone. 

"""

from __future__ import annotations
from typing import Sequence

from ear4.music import Pitch

# THIS NEEDS MORE THOUGHT


class _MutateTone_:
    def mutate_pitch(self):
        ...


@dataclass
class _PureTone:
    pitch: Pitch


class _PureTone_(_PureTone):
    def fundamental(self) -> PureTone:
        """
        Fundamental tone.

        """
        return PureTone(self.pitch)

    def overtones(self) -> Sequence[PureTone]:
        """
        Overtones.

        """

        ...


class PureTone:
    def __init__(self, pitch: Pitch):
        self.pitch = pitch
