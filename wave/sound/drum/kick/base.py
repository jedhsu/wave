from dataclasses import dataclass
from typing import TypeVar

__all__ = ["Kick"]


@dataclass
class Kick:
    Transient = TypeVar("Transient")
    Roll = TypeVar("Roll")
    Body = TypeVar("Body")
