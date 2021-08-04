from dataclasses import dataclass


class _Mutate_:
    def mutate_bpm(self, val: float):
        self.bpm = val


@dataclass
class _Tempo(_Mutate_):
    beats_per_minute: float  # mutable

    steps_per_beat: int = 4
    beats_per_bar: int = 4


# class _Beat(_Tempo):
#     beats_per_minute: float  # mutable


class _Tempo_(_Tempo):
    """
    Pure temporal conversions.

    """

    @property
    def steps_pm(self) -> float:
        return self.bpm * 4

    @property
    def bars_pm(self) -> float:
        return self.bpm / 4


class Tempo(
    _Tempo_,
    _Tempo,
):
    def __init__(
        self,
        bpm: float,
    ):
        self.bpm = bpm
