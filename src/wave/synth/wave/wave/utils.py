from enum import Enum
from math import log

# TODO: now with this logic, think about how to side chain on the addition of various amplitude envelopes


class EnvelopeUnit(Enum):
    POWER = "POWER"
    AMPLITUDE = "AMPLITUDE"
    DECIBELS = "DECIBELS"
    PHON = "PHON"





def power_to_db(power: float) -> float:


def amp_to_power(amp: float) -> float:
    pass


def power_to_amp(power: float) -> float:
    pass


# TODO: need to think about energy variance at frequency on loudness
def db_to_phon(phon: float) -> float:
    raise NotImplementedError


class PhonCurve:
    def __init__(self, db: float):
        pass
