from dataclasses import dataclass


@dataclass
class _Q:
    _value: float


class Q(_Q):
    def __init__(self, value: float):
        super(Q, self).__init__(value)

    def create(
        self,
        anchor: FreqAnchor,
        band: FreqBand,
    ):
        ...
