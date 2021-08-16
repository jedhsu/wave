"""

    *Audio Interface*

"""

from dataclasses import dataclass


@dataclass
class AudioInterface:
    index: int
    struct_version: int
    name: str
    host_api: int

    max_input_channels: int
    max_output_channels: int

    default_low_input_latency: float
    default_low_output_latency: float
    default_high_input_latency: float
    default_high_output_latency: float
    default_sample_rate: float

    @classmethod
    def from_dict(
        cls,
        **kwargs,
    ):
        return cls(
            index=kwargs["index"],
            struct_version=kwargs["structVersion"],
            name=kwargs["name"],
            host_api=kwargs["hostApi"],
            max_input_channels=kwargs["maxInputChannels"],
            max_output_channels=kwargs["maxOutputChannels"],
            default_low_input_latency=kwargs["defaultLowInputLatency"],
            default_low_output_latency=kwargs["defaultLowOutputLatency"],
            default_high_input_latency=kwargs["defaultHighInputLatency"],
            default_high_output_latency=kwargs["defaultHighOutputLatency"],
            default_sample_rate=kwargs["defaultSampleRate"],
        )
