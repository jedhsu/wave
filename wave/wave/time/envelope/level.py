"""

Envelope level.

"""

from dataclasses import dataclass

__all__ = ["Anchor"]


class _Set_:
    def _set(self, val: float):
        self._value = val


@dataclass
class _Level(_Set_):
    _value: float


class _Mutate_(_Level):
    def mutate(self, val: float):
        self._set(val)


class _Validate_(_Level):
    @staticmethod
    def validate(value: float):
        assert 0 <= value <= 1, "Level must be a percentage."


class Level(
    _Validate_,
    _Mutate_,
    _Level,
):
    def __init__(self, level: float):
        super(Level, self).__init__(level)

    @classmethod
    def create(cls, level: float):
        cls.validate(level)
        cls(level)
