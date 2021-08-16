"""

    *Streaming*

  Streaming context.

"""

import sounddevice as sd

from audio.system import AudioSystem


class Streaming:
    # these statics should be moved to default audio later
    sampling_rate = 44100  # sampling rate
    chunk_size = 1024
    number_of_channels = 2

    player = None
    streaming = None

    def __enter__(self):
        assert self.player is None
        assert self.streaming is None

        self.player = AudioSystem
        self.streaming = sd.play(
            format=self.format,
            channels=self.number_of_channels,
            rate=self.sampling_rate,
            output=True,
            output_device_index=self.player.main_interface().index,
            frames_per_buffer=self.chunk_size,
        )
        return self.streaming

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback,
    ):
        self.streaming.stop_stream()
        self.streaming.close()
        self.player._audio.terminate()

        self.streaming = None
        # [TODO] can move this None assignment into the Audio abstraction
        self.player = None
