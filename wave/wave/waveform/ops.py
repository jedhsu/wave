"""
    
Operators on waveforms.

"""

from .base import _Waveform


class _Validate_(_Waveform):
    def validate_shape(self, wf: _Waveform):
        """
        Validate waveforms are same shape.

        """
        assert self._vector.shape == wf._vector.shape


class _Op_(_Validate_, _Waveform):
    def add(self, wf: _Waveform) -> _Waveform:
        # TODO: assert same size
        return self._vector + wf._vector

    def scale(self, n: float) -> _Waveform:
        return n * self._vector

    def convolve(self, wf: _Waveform) -> _Waveform:
        return self._vector.convolve(wf._vector)


#     def __sub__(self, wf: _Waveform) -> _Waveform:
#         return self._vector + wf._vector

#     def __mul__(self, wf: _Waveform) -> _Waveform:
#         return self._vector + wf._vector

#     def __div__(self, wf: _Waveform) -> _Waveform:
#         return self._vector + wf._vector
