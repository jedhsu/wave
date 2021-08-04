from __future__ import annotations
from math import pi

from .tempo import Tempo


class SamplingParameters:
    def __init__(
        self,
        tempo: Tempo = Tempo(beats_per_minute=125.25),
        frames_per_step: int = 10,
        sampling_rate: int = 48000,
        frequency_ceiling: int = 22000,
        ending_frame_buffer: float = 3.0,
    ):
        self.__tempo = tempo
        self.__frequency_ceiling = frequency_ceiling
        self.__sampling_rate = sampling_rate
        self.__frames_per_step = frames_per_step
        self.__ending_frame_buffer = ending_frame_buffer

    def default(self) -> SamplingParameters:
        return SamplingParameters(
            tempo=Tempo(beats_per_minute=125.25),
            frames_per_step=10,
            sampling_rate=48000,
            frequency_ceiling=22000,
        )

    @property
    def tempo(self) -> Tempo:
        return self.__tempo

    @property
    def frequency_ceiling(self) -> float:
        return self.__frequency_ceiling

    #######
    @property
    def sampling_rate(self) -> int:
        """Hertz (samples per second)."""
        return self.__sampling_rate

    @property
    def nyquist_frequency(self) -> float:
        return self.sampling_rate / 2

    #######
    @property
    def sample_duration(self) -> float:
        """Sample duration (seconds)."""
        return 1 / self.sampling_rate

    @property
    def angular_frequency(self) -> float:
        return 2 * pi * self.sample_duration

    @property
    def samples_per_frame(self) -> float:
        return 1 / self.frames_per_sample

    @property
    def samples_per_step(self) -> float:
        return self.samples_per_frame * self.frames_per_step

    @property
    def samples_per_beat(self) -> float:
        return 4 * self.samples_per_step

    @property
    def samples_per_bar(self) -> float:
        return 4 * self.samples_per_bar

    def number_of_samples(self, number_of_frames) -> int:
        return int(
            (number_of_frames + self.ending_frame_buffer) * self.samples_per_frame
        )

    #######
    @property
    def frame_duration(self) -> float:
        return self.step_duration / self.frames_per_step

    @property
    def frames_per_sample(self) -> float:
        return self.sample_duration / self.frame_duration

    @property
    def frames_per_step(self) -> int:
        return self.__frames_per_step

    #######
    @property
    def ending_frame_buffer(self) -> float:
        return self.__ending_frame_buffer

    #######
    @property
    def step_duration(self) -> float:
        """Step duration (seconds)."""
        return 60 / self.tempo.steps_per_minute

    def __repr__(self) -> str:
        return f"""
       SOUND PARAMETERS
       ################
       - Beats Per Minute: {self.tempo.beats_per_minute}
       - Frames Per Step: {self.frames_per_step}
       - Samples Per Frame: {self.samples_per_frame}
       """
