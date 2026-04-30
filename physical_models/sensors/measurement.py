from dataclasses import dataclass
import numpy as np

@dataclass
class Measurement:
    z: np.ndarray #the measurement vector, in the same units as the sensor readings
    r: np.ndarray #the measurement noise, in the same units as the sensor readings
    t: float #the time the measurement was taken, in sim time, not real time
