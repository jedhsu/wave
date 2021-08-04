from math import sqrt


class Spectrum:
    @staticmethod
    def bins_per_octave(n: int):
        return sqrt(n) * 2
