from pytest import approx

from ..duration import Duration


class TestDuration:
    def test_init(self):
        dur = Duration(0.5)

        assert isinstance(dur, Duration)
        assert isinstance(dur, float)

        assert dur == approx(0.5)
        assert dur == approx(Duration(0.5))

    def test_mro(self):
        ...

    def test_repr(self):
        dur = Duration(0.5)
        assert repr(dur) == "0.500 seconds"
