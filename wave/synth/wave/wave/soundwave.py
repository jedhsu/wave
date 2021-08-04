# from __future__ import annotations
# from typing import List, Optional, Iterator

# from .sinusoid import Sinusoid


## considering moving this to synth folder

# import numpy as np


# class Soundwave:
#    def __init__(
#        self,
#        sinusoids: List[Sinusoid],
#        # origin: Union[Primitive, Transform],
#        id: int = 0,
#        name: Optional[str] = None,
#    ):
#        self.__id = id
#        self.__sinusoids = sinusoids

#    #######
#    @property
#    def sinusoids(self) -> List[Sinusoid]:
#        return self.__sinusoids

#    # CHANGE TO POSITION
#    @property
#    def waveform(self) -> Iterator[float]:
#        """This should really be called wave position."""
#        # TODO: this has some major issues
#        position = 0
#        for sinusoid in self.sinusoids:
#            position += next(sinusoid.waveform)
#        yield position

#    # TODO: how can we better leverage generators?
#    # this is ugly... clean me!
#    def as_array(self, number_of_samples: int) -> np.ndarray:
#        arr = np.zeros(number_of_samples)

#        for i in range(number_of_samples):
#            arr[i] = next(self.waveform)

#        return arr

#    # TODO: possibly move transforms to sound manager / cursor (also fits with ID)

#    ##############
#    # TRANSFORMS #
#    # def aggregate(self, sounds: List[Sound], weights: List[float]) -> Sound:
#    #     aggregation = Aggregation(sounds.append(self), weights.append(1 - sum(weights)))
#    #     return aggregation.apply()

#    # def apply(self, transform: Transform) -> Sound:
#    #     return Sound(
#    #         waveform=transform.waveform,
#    #         origin_sound=[self],
#    #         origin_transform=transform,
#    #         parameters=self.parameters,
#    #     )

#    # # def delay(self, delaying: Delaying) -> Sound:
#    #     return delaying.apply(self)

#    # def widen(self, widening: Widening) -> Sound:
#    #     return widening.apply(self)

#    # def pan(self, panning: Panning) -> Sound:
#    #     return panning.apply(self)

#    # def distort(self, distortion: Distortion) -> Sound:
#    #     return distortion.apply(self)
