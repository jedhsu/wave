"""

    *Sinusoid,   [Bindings]*

"""

from ._sinusoid import Sinusoid as _Sinusoid

from ._op import Build
from ._op import Play


class Sinusoid(
    Play,
    Build,
    _Sinusoid,
):
    pass
