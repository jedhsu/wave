"""
Base Vector class (wrapper around np).
"""
from __future__ import annotations
from typing import Sequence, TypeVar

import numpy as np

from ..base import Frequency

T = TypeVar("T")

usize = int


class Vector(Sequence, np.ndarray):
    def __init__(self, arraylike: Sequence[T]):
        super(Vector, self).__init__(arraylike)
