"""

Abstract base type for higher-level Sound (Sound Design).

"""

__all__ = ["Sound"]

# maybe should rename as synth...


class _Sound:
    tone: Tone
    frequency_envelope: FrequencyEnvelope
    amplitude_envelope: AmplitudeEnvelope


class Sound:
    ...
