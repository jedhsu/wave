"""

    *Play*

"""

from .streaming import Streaming

from .._sinusoid import Sinusoid
from .sampling import Sampling


class Play(
    Sampling,
    Sinusoid,
):
    def play(self):
        # with Streaming():
        #     # read data
        #     data = self.filing.readframes(
        #         self.chunk,
        #     )

        # play stream
        with Streaming() as stream:
            stream.write(self.into_samples().tobytes())
