from __future__ import annotations
from math import pi

from ear4.music import MusicParam

from ..spectrum import AngularFrequency, Frequency
from ..time import Duration


class _UVParam:
    frames_per_second: float  # cycles per second
    spectral_ceiling: Frequency  # spectral frequency ceiling
    music: MusicParam


class _FrameParam(_UVParam):
    def frame_duration(self) -> Duration:
        """Sample duration (seconds)."""
        return Duration(1 / self.frames_per_second)

    def angular_frequency(self) -> AngularFrequency:
        return AngularFrequency.from_duration(self.frame_duration())

    # def frames_per_block(self) -> float:
    #    return self.block_duration / self.frame_duration

    def frames_per_block(self) -> float:
        return 1 / self.frames_per_sample


class _BlockParam(_FrameParam):
    def block_duration(self) -> Duration:
        return self.step_duration() / self.frames_per_step()

    ...


#    @property
#    def samples_per_step(self) -> float:
#        return self.samples_per_frame * self.frames_per_step

#    @property
#    def samples_per_beat(self) -> float:
#        return 4 * self.samples_per_step

#    @property
#    def samples_per_bar(self) -> float:
#        return 4 * self.samples_per_bar
class _StepParam(_UVParam):
    def step_duration(self) -> Duration:
        ...


class _UVParam_:
    @property
    def nyquist_frequency(self) -> float:
        return self.frames_per_second / 2

    def frame_duration(self) -> float:
        ...

    def angular_frequency(self) -> AngularFrequency:
        ...


# class SamplingParameters:
#    def __init__(
#        self,
#        tempo: Tempo = Tempo(beats_per_minute=125.25),
#        frames_per_step: int = 10,
#        sampling_rate: int = 48000,
#        frequency_ceiling: int = 22000,
#        ending_frame_buffer: float = 3.0,
#    ):
#        self.__tempo = tempo
#        self.__frequency_ceiling = frequency_ceiling
#        self.__sampling_rate = sampling_rate
#        self.__frames_per_step = frames_per_step
#        self.__ending_frame_buffer = ending_frame_buffer

#    def default(self) -> SamplingParameters:
#        return SamplingParameters(
#            tempo=Tempo(beats_per_minute=125.25),
#            frames_per_step=10,
#            sampling_rate=48000,
#            frequency_ceiling=22000,
#        )

#    @property
#    def tempo(self) -> Tempo:
#        return self.__tempo

#    @property
#    def frequency_ceiling(self) -> float:
#        return self.__frequency_ceiling

#    #######
#    @property
#    def sampling_rate(self) -> int:
#        """Hertz (samples per second)."""
#        return self.__sampling_rate


#    #######

#    @property
#    #######

#    #######
#    @property
#    def ending_frame_buffer(self) -> float:
#        return self.__ending_frame_buffer

#    #######
#    @property
#    def step_duration(self) -> float:
#        """Step duration (seconds)."""
#        return 60 / self.tempo.steps_per_minute

#    def __repr__(self) -> str:
#        return f"""
#       SOUND PARAMETERS
#       ################
#       - Beats Per Minute: {self.tempo.beats_per_minute}
#       - Frames Per Step: {self.frames_per_step}
#       - Samples Per Frame: {self.samples_per_frame}
#       """
