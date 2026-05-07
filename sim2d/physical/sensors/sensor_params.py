from sim2d.core.params import Params
from dataclasses import dataclass


@dataclass
class SensorParams(Params):
    refresh_rate: float = 10.0 #Hz, how often the sensor updates its readings. Note, this is in sim time, not real time.
    noise_std: float = 0.0 #standard deviation of the noise added to the sensor readings, in the same units as the sensor readings. Note, this is in sim time, not real time.