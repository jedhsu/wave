import math

from ..base import AngularFrequency, Duration, Freq, Frequency, Period, Radians


class TestFreq:
    def test_type_heirarchy(self):
        assert issubclass(Frequency, Freq)
        assert issubclass(AngularFrequency, Freq)
        assert issubclass(Period, Freq)
        assert issubclass(Radians, Freq)

    def test_frequency(self):
        freq = Frequency(440)

        assert isinstance(freq, Frequency)
        assert isinstance(freq, float)

    def test_period(self):
        per = Period(1 / 440)

        assert isinstance(per, Period)
        assert isinstance(per, Duration)

        assert repr(per) == f"{1/440:.3f} seconds"

    def test_angular_frequency(self):
        omega = AngularFrequency(440 * 2 * math.pi)

        assert isinstance(omega, AngularFrequency)
        assert isinstance(omega, float)

    def test_radians(self):
        pass

    def test_hooks(self):
        assert Freq.Frequency == Frequency
        assert Freq.Period == Period
        assert Freq.Angular == AngularFrequency
        assert Freq.Radians == Radians

        assert issubclass(Freq.Frequency, Freq)
        assert issubclass(Freq.Period, Freq)
        assert issubclass(Freq.Angular, Freq)
        assert issubclass(Freq.Radians, Freq)
