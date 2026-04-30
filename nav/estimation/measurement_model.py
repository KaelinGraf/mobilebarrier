from dataclasses import dataclass


#used within the measurement model to represent the measurement noise, which is added to the sensor readings to simulate real-world sensor noise. Note, this is in sim time, not real time.
@dataclass
class MeasurementModel:
    pass
