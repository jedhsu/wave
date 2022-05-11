"""

    *Buffer,   [Play]*

"""

import asyncio
import sounddevice as sd

from .._buffer import Buffer


class Play(
    Buffer,
):
    async def play(
        self,
        **kwargs,
    ):
        loop = asyncio.get_event_loop()
        event = asyncio.Event()
        idx = 0

        def callback(
            outdata,
            frame_count,
            time_info,
            status,
        ):
            nonlocal idx

            if status:
                print(status)

            remainder = len(self) - idx
            if remainder == 0:
                loop.call_soon_threadsafe(event.set)
                raise sd.CallbackStop

            valid_frames = frame_count if remainder >= frame_count else remainder
            outdata[:valid_frames] = self[idx : idx + valid_frames]
            outdata[valid_frames:] = 0
            idx += valid_frames

        stream = sd.OutputStream(
            callback=callback,
            dtype=self.dtype,
            channels=self.shape[1],
            **kwargs,
        )
        with stream:
            await event.wait()
