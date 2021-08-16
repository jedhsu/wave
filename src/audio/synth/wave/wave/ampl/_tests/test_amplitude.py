from pytest import approx
import pytest

from ..amplitude import Amplitude, Decibel, Power, _Validate_


class TestValidate:
    def test_validate(self):
        assert _Validate_(0.5)
        assert _Validate_(0.01)
        assert _Validate_(0.99)

        with pytest.raises(ValueError):
            _Validate_(-0.5).validate()
            _Validate_(2.0).validate()


class TestDisplay:
    def test_repr(self):
        ampl = Amplitude(0.5)

        assert repr(ampl) == "0.500"


class TestFrom:
    def test_from_decibel(self):
        db = Decibel(-10)

        assert Amplitude.from_decibel(db) == approx(0.3162276)
        assert Amplitude.from_decibel(db) == approx(Amplitude(0.3162276))

    def test_from_power(self):
        pow = Power(-10)

        assert Amplitude.from_power(pow) == approx(0.1)
        assert Amplitude.from_power(pow) == approx(Power(0.1))

    def test_from_phon(self):
        pass


class TestInto:
    def test_into_decibel(self):
        ampl = Amplitude(0.1)

        assert ampl.into_decibel() == approx(-20)
        assert ampl.into_decibel() == approx(Decibel(-20))

    def test_into_power(self):
        ampl = Amplitude(0.1)

        assert ampl.into_power() == approx(-10)
        assert ampl.into_power() == approx(Power(-10))

    def test_into_phon(self):
        pass


class TestAmplitude:
    def test_init(self):
        """
        Tests for hooked validator

        """

        Amplitude(0.5)

        with pytest.raises(ValueError):
            Amplitude(-0.5)
