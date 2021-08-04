"""
    
    Primitive

  Primitive wave type.

"""

from dataclasses import dataclass

from ..wave import Wave
from .sawtooth import Sawtooth
from .sinusoid import Sinusoid
from .square import Square


class _MutatePrimitive_:
    def mutate_sine(self):
        ...


@dataclass
class _Primitive:
    """
    Blend of primary waveforms.

    """

    blend: dict[str, float]

    sine: Sinusoid
    saw: Sawtooth
    square: Square


class Primitive(Wave):
    ...
