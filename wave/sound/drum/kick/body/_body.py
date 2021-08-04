"""

    *Kick Body*

  The body component of the kick.

"""

from wave import Wave

from .base import Kick

__all__ = ["Body"]


class KickBody(
    Kick,
    Wave,
):
    ...
