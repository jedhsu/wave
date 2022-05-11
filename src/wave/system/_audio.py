from typing import Sequence

from pyaudio import PyAudio

from .interface import AudioInterface

"""

nvm sounddevice provides this

"""


class AudioSystem:
    _audio = PyAudio()
    main_interface_name = "Scarlett 2i2"

    @classmethod
    def default_output_device(cls) -> AudioInterface:
        return AudioInterface.from_dict(
            **cls._audio.get_default_output_device_info(),
        )

    @classmethod
    def interfaces(cls) -> list[AudioInterface]:
        interfaces = []
        for id in range(cls._audio.get_device_count()):
            interfaces.append(
                AudioInterface.from_dict(
                    **cls._audio.get_device_info_by_index(id),
                ),
            )
        return interfaces

    @classmethod
    def main_interface(cls) -> AudioInterface:
        interface = [
            interface
            for interface in cls.interfaces()
            if cls.main_interface_name in interface.name
        ]
        if not interface:
            raise ValueError
        return interface[0]
