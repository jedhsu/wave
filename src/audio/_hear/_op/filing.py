"""

    *Filing*

  Context of a file.

"""

from .._audio import Audio

import wave


class Filing(
    Audio,
):
    filing = None

    def __enter__(self):
        self.filing = wave.open(
            str(self),
            "rb",
        )

    def __exit__(self):
        if self.filing:
            self.filing.close()
