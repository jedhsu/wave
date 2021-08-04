from ...base.envelope import AmplitudeEnvelope, Envelope, LevelEnvelope
from fourear.base.frequency.frequency import Frequency
from ...base.sampling import SamplingParameters
from ...base.soundwave import Soundwave

# from ...transform.fill import Fill
from ...base.primary import PrimaryWave, PrimaryWaveType

from ..sound import Sound


class Pluck(Sound):
    def __init__(
        self,
        name: str,
        fundamental: Frequency,
        amplitude_envelope: AmplitudeEnvelope,
        sampling_parameters: SamplingParameters,
    ):
        self.__fundamental = fundamental
        self.__amplitude_envelope = amplitude_envelope
        super().__init__(name, sampling_parameters)

    def synthesize(self) -> Soundwave:
        saw = PrimaryWave(
            PrimaryWaveType.SAWTOOTH,
            self.fundamental,
            self.amplitude_envelope,
            self._sampling_parameters,
        ).synthesize()

        # TODO: ugly grammar, clean me later
        # fill = Fill(saw, self.envelope)
        # return saw.apply(fill)
        return saw

    #######
    def __repr__(self) -> str:
        return "Pluck"

    #######
    @property
    def fundamental(self) -> Frequency:
        """Fundamental frequency."""
        return self.__fundamental

    @property
    def amplitude_envelope(self) -> AmplitudeEnvelope:
        return self.__amplitude_envelope


class PluckFactory:
    @staticmethod
    def basic():
        envelope = Envelope.from_dict(
            {
                0: LevelEnvelope.from_dict({1: 1, 17: 0}),
                5000: LevelEnvelope.from_dict({1: 1, 9: 0}),
                11000: LevelEnvelope.from_dict({1: 1, 6: 0}),
                22000: LevelEnvelope.from_dict({1: 1, 4: 0}),
            }
        )
        amp_envelope = AmplitudeEnvelope(0, 1, envelope)

        pluck = Pluck(
            "Test_Pluck",
            fundamental=Frequency(600.0),
            amplitude_envelope=amp_envelope,
            sampling_parameters=SamplingParameters(),
        )
        number_of_samples = pluck._sampling_parameters.number_of_samples(
            amp_envelope.ending_frame
        )
        wf = pluck.synthesize()

        pluck.save(wf, number_of_samples)
