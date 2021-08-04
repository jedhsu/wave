"""
B_n coefficients of a Fourier series.

"""


from sympy import Function, pi


class _B_n:
    function: Function = Function("((-1) ^ n) * ((2 * A) / (pi * n))")


class _Iterate_(Iterator):
    def __next__(self):
        ...

    def __iter__(self):
        return self


class B_n(_Iterate_):
    def __iter__(self):
        ...
