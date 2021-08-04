from dataclasses import dataclass

from ear4.wave import Wave

from .body import Body
from .roll import Roll
from .transient import Transient

__all__ = ["Kick"]


@dataclass(frozen=True)
class _Kick:
    transient: Wave
    roll: Wave
    body: Wave


class Kick(Wave):
    def __init__(self, transient: KickTransient, roll: KickRoll, body: KickRoll):
        self.__transient = transient
        self.__roll = roll
        self.__body = body

    @property
    def transient(self):
        return self.__transient

    @property
    def roll(self):
        return self.__roll

    @property
    def body(self):
        return self.__body
