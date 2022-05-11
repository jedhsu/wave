"""

    *Record*

"""

import asyncio
import sounddevice as sd

from .._buffer import Buffer


class Record(
    Buffer,
):
    async def record(
        self,
        **kwargs,
    ):
        loop = asyncio.get_event_loop()
        event = asyncio.Event()
        idx = 0

        def callback(
            indata,
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

            indata = indata[:remainder]
            self[idx : idx + len(indata)] = indata
            idx += len(indata)

        stream = sd.InputStream(
            callback=callback,
            dtype=self.dtype,
            channels=self.shape[1],
            **kwargs,
        )

        with stream:
            await event.wait()
