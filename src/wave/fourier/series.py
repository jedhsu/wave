from dataclasses import dataclass
from typing import Iterator, Sequence

from .a_n import A_n
from .b_n import B_n

@dataclass(frozen=True)
class _FourierSeries:
    a_n: A_n
    b_n: B_n


class FourierSeries(Sequence[float):
    def __init__(self):
        ...
