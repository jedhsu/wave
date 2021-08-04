from __future__ import annotations
from math import sin
from typing import Generator, Iterator, Optional

from fourear.base.sampling import SamplingParameters

from .envelope import AmplitudeEnvelope, FrequencyEnvelope
from .frequency.frequency import Frequency


class Sinusoid:
    def __init__(
        self,
        amplitude_envelope: AmplitudeEnvelope,
        frequency_envelope: FrequencyEnvelope,
        amplitude_coefficient: float,
        sampling_parameters: SamplingParameters,
    ):
        # TODO: maybe should have a clock
        self.__amplitude_envelope = amplitude_envelope
        self.__frequency_envelope = frequency_envelope
        self.__angular_frequency = sampling_parameters.angular_frequency
        self.__frames_per_sample = sampling_parameters.frames_per_sample

    # TODO: frequency will need setter when extending to modulation
    # will need to work with statefulness
    # TODO: amplitude and envelope are the same... GENERALIZE

    def __repr__(self) -> str:
        return f"""
        SINUSOID
        - Amplitude Envelope: {self.amplitude_envelope}
        - Frequency Envelope: {self.frequency_envelope}
        """

    @property
    def amplitude_envelope(self) -> AmplitudeEnvelope:
        return self.__amplitude_envelope

    @property
    def frequency_envelope(self) -> FrequencyEnvelope:
        return self.__frequency_envelope

    @property
    def angular_frequency(self) -> float:
        return self.__angular_frequency

    @property
    def frames_per_sample(self) -> float:
        return self.__frames_per_sample

    #######
    def _amplitude(self) -> Generator[Optional[float], float, None]:
        frame = 0
        frequency = yield
        while True:
            frequency = yield self.amplitude_envelope.amplitude(frame, frequency)
            frame += self.frames_per_sample

    def _frequency(self) -> Iterator[float]:
        frame = 0
        while True:
            yield self.frequency_envelope.frequency(frame)
            frame += self.frames_per_sample

    @property
    def waveform(self) -> Iterator[float]:
        # probably move timestamp to a sender
        timestamp = 0

        frequency = self._frequency()
        amplitude = self._amplitude()

        next(amplitude)
        while True:
            freq = next(frequency)
            amp = amplitude.send(freq)
            yield amp * sin(timestamp * freq)
            timestamp += self.angular_frequency

    #######
    def modify_amplitude(self, multiplier: float) -> Sinusoid:
        # return Sinusoid(
        #     self.frequency,
        #     multiplier * self.amplitude,
        #     self.step,
        #     self.amplitude_envelope,
        #     self.frequency_envelope,
        # )
        raise NotImplementedError
