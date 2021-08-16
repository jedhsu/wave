from pytest import approx

from ..duration import Duration


class TestDuration:
    dur = Duration(0.5)

    def test_init(self):
        assert isinstance(self.dur, Duration)
        assert self.dur.seconds == approx(0.5)

    def test_mro(self):
        ...

    def test_set(self):
        duration = self.dur
        duration._set_seconds(0.6)
        assert duration.seconds == 0.6

    def test_mutate(self):
        self.dur.update_seconds(0.6)
        assert self.dur.seconds == 0.6

    def test_repr(self):
        # TODO: monitor the referencing a closer look...
        assert repr(self.dur) == "0.6 seconds"
