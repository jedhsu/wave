from pytest import approx

from ..frequency import Frequency


class TestFrequency:
    def test_init(self):
        freq = Frequency(1)
        assert isinstance(freq, float)
        assert isinstance(freq, Frequency)
        assert freq == approx(1.0)

    def test_float_operations(self):
        freq = Frequency(1)
        assert freq + freq == approx(2.0)
        assert 2 * freq == approx(2.0)
