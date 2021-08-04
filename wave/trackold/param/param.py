from dataclasses import dataclass

from .tempo import Tempo


@dataclass(frozen=True)
class _MusioParam:
    tempo: Tempo


class _Update_(_MusioParam):
    def update_bpm(self, val: float):
        self.tempo.mutate_bpm(val)


class _Default_:
    ...


class SamplingParam:
    ...


class MusioParam:
    ...
