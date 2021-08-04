
"""

Parametric EQ.

"""


@dataclass(frozen=True)
class EQParam:
    frequency:
    delta: Decibel
    q: Q

