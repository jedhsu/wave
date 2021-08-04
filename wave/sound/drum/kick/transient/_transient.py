"""

    *Kick Transient*

  The transient component of the kick.

"""

from dataclasses import dataclass

from ear4.base import Wave

from .base import Kick

__all__ = ["Transient"]


# @dataclass
# class _Transient:
#     base: Noise


class _Build_:
    pass


class KickTransient(
    Build,
    Wave,
):
    ...
