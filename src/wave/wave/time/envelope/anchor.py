"""

Envelope anchor.

"""

from collections import OrderedDict
from dataclasses import dataclass

from .level import Level


__all__ = ["Anchor"]


@dataclass
class _Anchors:
    dict: OrderedDict[int, Level]


class _Anchors_(_Anchors):
    def end_block(self) -> int:
        return self.dict[end]


class _Validate_(_Anchors_, _Anchors):
    def _validate_insert(self):
        ...

    def _validate_append(self, block: int):
        assert block > self.end_block()

    def _validate_modify(self):
        ...

    def _validate_remove(self, block: int):
        assert block in self.dict.keys(), "Block is not in keys."


class _Mutate_(_Validate_, _Anchors):
    def insert(self):
        ...

    def append(self):
        ...

    def modify(self, block: int, level: Level):
        ...

    def remove(self):
        ...


class _Display_(_Anchors):
    def __repr__(self):
        ...


class Anchors(_Anchors_, _Anchors):
    def __init__(self):
        super().__init__(OrderedDict())
