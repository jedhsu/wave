"""

    Function

  Encapsulates and extends sympy.Function.

"""

from dataclasses import dataclass

from sympy import Function as __Function


@dataclass
class _Function:
    _fn: __Function


class Function:
    ...
