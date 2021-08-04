"""

    effect

  Abstract base effect type.

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from ear4.wave import Wave


@dataclass(frozen=True)
class _Effect:
    source: Wave  # source sound wave


class _Effect_(
    _Effect,
    metaclass=ABCMeta,
):
    @abstractmethod
    def apply(self) -> Wave:
        """
        Applies effect to return an output wave.

        * Main API function for effect.

        """
        pass

    @abstractmethod
    def diff(self) -> Wave:
        """
        Difference in waveform from source and result.

        """
        pass


class Effect(
    _Effect_,
    _Effect,
    metaclass=ABCMeta,
):
    ...
