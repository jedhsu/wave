from sympy import Symbol, pi, sin

from ..math import Function


def sinusoid():
    return Symbol("A") * sin(2 * pi * (Symbol("ω ") * Symbol("t")) - Symbol("θ"))


# class Sinusoid(Function):
#     super(Function, cls).__init__(
#     def __init__(self):
#         super().__init__
