"""

Base class for envelope.

"""


from __future__ import annotations
from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence

from numpy import interp
import numpy as np

from .level import Level

__all__ = ["Envelope"]


@dataclass
class _Envelope:
    anchors: OrderedDict[int, Level]


class _Envelope_:
    # ths should just be vector...
    def interpolate(self) -> np.ndarray:
        ...


class _Default_:
    @staticmethod
    def triangle(self) -> Envelope:
        ...


class _From_:
    @staticmethod
    def from_adsr(
        attack: Level,
        decay: Level,
        sustain: Optional[Level] = None,
        release: Optional[Level] = None,
    ):
        ...


class Envelope(
    _Default_,
    _Envelope_,
    _Envelope,
):
    def __init__(self):
        ...


# class LevelEnvelope:
# """Level envelope (2D)."""

# def __init__(self, anchors: Sequence[LevelAnchor]):
# self.__anchors = {0: 0}
# for anchor in anchors:
#     self.add_anchor(anchor)

# # assert (
# #     self.anchors[0] == 0
# # ), f"Beginning anchor ({self.anchors[0]}) must be (0, 0)."

# # assert (
# #     self.anchors[max(self.anchors.keys())] == 0
# # ), "Ending anchor must have level 0."

# @staticmethod
# def from_dict(anchors: dict[int, int]) -> LevelEnvelope:
# return LevelEnvelope(
#     [LevelAnchor(frame, level) for frame, level in anchors.items()]
# )

# # def __repr__(self) -> str:
# #    ret = f"""
# #    Level Envelope
# #    ##############
# #    """
# #    ret += "\n".join([str(anchor) for anchor in self._anchors])
# #    return ret

# @property
# def anchors(self) -> OrderedDict[int, int]:
# return OrderedDict(sorted(self.__anchors.items()))

# def add_anchor(self, anchor: LevelAnchor):
# self.__anchors[anchor.frame] = anchor.level

# def get_level(self, frame: float) -> float:
# assert frame >= 0, "Frame must be positive."
# lower_bound = max(
#     (key for key in self.anchors.keys() if key <= frame),
#     default=min(key for key in self.anchors.keys()),
# )
# upper_bound = min(
#     (key for key in self.anchors.keys() if key >= frame),
#     default=max(key for key in self.anchors.keys()),
# )

# return interp(
#     frame,
#     [lower_bound, upper_bound],
#     [self.anchors[lower_bound], self.anchors[upper_bound]],
# )

# @property
# def finish(self) -> float:
# # TODO: this can also be last key
# return max(self.anchors.keys())


# class FrequencyAnchor:
# """Anchor point for envelope."""

# def __init__(self, frequency: int, level_envelope: LevelEnvelope):
# # TODO: make frequency relative later
# self.__frequency = frequency
# self.__level_envelope = level_envelope
# # assert (
# #     0 <= self.level <= 100
# # ), "Level (relative amplitude) must be between 0 and 100."

# @property
# def frequency(self) -> int:
# return self.__frequency

# @property
# def level_envelope(self) -> LevelEnvelope:
# return self.__level_envelope


# class Envelope:
# """Level + Frequency Envelope (3D)."""

# def __init__(self, frequency_anchors: Sequence[FrequencyAnchor]):
# self.__frequency_anchors = {}
# for anchor in frequency_anchors:
#     self.add_anchor(anchor)

# @staticmethod
# def from_dict(anchors: dict[int, LevelEnvelope]):
# return Envelope([FrequencyAnchor(key, value) for key, value in anchors.items()])

# @property
# def frequency_anchors(self) -> OrderedDict[int, LevelEnvelope]:
# return OrderedDict(sorted(self.__frequency_anchors.items()))

# # TODO: this needs a test!
# @property
# def ending_frame(self) -> float:
# return max(env.finish for env in self.frequency_anchors.values())

# def add_anchor(self, anchor: FrequencyAnchor):
# self.__frequency_anchors[anchor.frequency] = anchor.level_envelope

# def get_level(self, frame: float, frequency: float) -> float:
# """Level envelope at a frame & frequency."""
# assert frame >= 0

# lower_frequency_bound = max(
#     (key for key in self.frequency_anchors.keys() if key <= frequency),
#     default=min(key for key in self.frequency_anchors.keys()),
# )
# upper_frequency_bound = min(
#     (key for key in self.frequency_anchors.keys() if key >= frequency),
#     default=max(key for key in self.frequency_anchors.keys()),
# )

# lower_level = self.frequency_anchors[lower_frequency_bound].get_level(frame)
# upper_level = self.frequency_anchors[upper_frequency_bound].get_level(frame)

# return interp(
#     frequency,
#     [lower_frequency_bound, upper_frequency_bound],
#     [lower_level, upper_level],
# )


# # class AmplitudeEnvelope:
# #     def __init__(
# #         self,
# #         floor: float = 0,
# #         ceiling: float = 1,
# #         envelope: Optional[Envelope] = None,
# #     ):
# #         assert ceiling > floor, "Ceiling must be greater than floor."
# #         self.__floor = floor
# #         self.__ceiling = ceiling
# #         self.__envelope = envelope

# #     @property
# #     def floor(self) -> float:
# #         return self.__floor

# #     @property
# #     def ceiling(self) -> float:
# #         return self.__ceiling

# #     @property
# #     def range(self) -> float:
# #         return self.ceiling - self.floor

# #     @property
# #     def envelope(self) -> Optional[Envelope]:
# #         return self.__envelope

# #     @property
# #     def ending_frame(self) -> Optional[float]:
# #         if self.envelope is not None:
# #             return self.envelope.ending_frame
# #         else:
# #             return None

# #     def amplitude(self, frame: float, frequency: float) -> float:
# #         if self.envelope is None:
# #             return self.ceiling
# #         else:
# #             return self.floor + self.range * self.envelope.get_level(frame, frequency)

# #     def mix(self, env: AmplitudeEnvelope, target: AmplitudeEnvelope):
# #         pass


# # make simple case of level envelope for now, but do experiment
# # THIS NEEDS TO EVENTUALLY BE EXTENDED TO MODULATION! think precisely about what envelopes are
# # class FrequencyEnvelope:
# #     def __init__(
# #         self,
# #         base: float,
# #         target: Optional[float] = None,
# #         envelope: Optional[LevelEnvelope] = None,
# #     ):
# #         self.__base = base
# #         self.__target = target
# #         self.__envelope = envelope

# #     @property
# #     def base(self) -> float:
# #         return self.__base

# #     @property
# #     def target(self) -> Optional[float]:
# #         return self.__target

# #     @property
# #     def range(self) -> float:
# #         return self.target - self.base

# #     @property
# #     def envelope(self) -> Optional[LevelEnvelope]:
# #         return self.__envelope

# #     def frequency(self, frame: float) -> float:
# #         if self.envelope is None:
# #             return self.base
# #         else:
# #             return self.base + self.range * self.envelope.get_level(frame)
