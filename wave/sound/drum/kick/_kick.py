"""

    *Kick*

  The kick.

"""

from dataclasses import dataclass
from typing import TypeVar

__all__ = ["Kick"]


@dataclass
class Kick(
    Drums,
):
    Transient = TypeVar("Transient")
    Roll = TypeVar("Roll")
    Body = TypeVar("Body")
