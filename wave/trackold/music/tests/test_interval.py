from pytest import approx

from ..interval import Interval, _IntervalEnum

# from ..key import Key, _add


class TestInterval:
    def test_init(self):
        interval = Interval(_IntervalEnum.m3, 0)
        assert isinstance(interval, Interval)
        assert interval == Interval(_IntervalEnum.m3, 0)

    def test_mro(self):
        ...

    def test_repr(self):
        interval = Interval(_IntervalEnum.m3, 0)
        assert repr(interval) == "minor 3rd, 0 octaves"

    def test_semitones(self):
        interval = Interval(_IntervalEnum.m3, 0)
        assert interval.semitones() == 3

    def test_ratio(self):
        interval = Interval(_IntervalEnum.m3, 0)
        assert Interval.ratio(interval) == approx(2 ** (3 / 12))

    def test_add(self):
        interval = Interval(_IntervalEnum.m3, 0)
        assert interval + Interval(_IntervalEnum.m3, 0) == Interval(_IntervalEnum.m5, 0)
