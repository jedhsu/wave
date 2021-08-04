"""

    *Sound*

  The sound type.

"""

from fivear.sampling import Sampling


class Sound(
    Sampled,
):
    __metaclass__ = ABCMeta

    # DB_PATH = Path("/home/jed/4ear/fourear/sounds/")

    # def __init__(self, name: str, sampling_parameters: SamplingParameters):
    #     self.__name = name
    #     self._sampling_parameters = sampling_parameters

    # @property
    # def name(self) -> str:
    #     return self.__name

    # @abstractmethod
    # def synthesize(self) -> Soundwave:
    #     return

    # @property
    # @abstractmethod
    # def amplitude_envelope(self) -> AmplitudeEnvelope:
    #     return

    # @property
    # def number_of_samples(self) -> int:
    #     return self._sampling_parameters.number_of_samples(
    #         self.amplitude_envelope.ending_frame
    #     )

    # @property
    # def duration(self) -> float:
    #     """Duration in seconds."""
    #     return self.number_of_samples * self._sampling_parameters.sample_duration

    # def save(self, soundwave: Soundwave):
    #     path = self.DB_PATH.joinpath(self.name)

    #     soundfile.write(
    #         f"{path}.wav",
    #         soundwave.as_array(self.number_of_samples),
    #         samplerate=self._sampling_parameters.sampling_rate,
    #     )
