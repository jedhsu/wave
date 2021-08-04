"""
    
    Tone

  Model for tone. 

"""


class _MutateTone_:
    def mutate_pitch(self):
        ...


@dataclass
class _Tone:
    pitch: Pitch


class _Tone_:
    def fundamental(self) -> Tone:
        """
        Fundamental tone.

        """
        ...

    def overtones(self) -> Sequence[Tone]:
        """
        Overtones.

        """

        ...


class Tone:
    pass
