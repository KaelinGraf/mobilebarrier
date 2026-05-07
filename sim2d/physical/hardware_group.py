from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np

from sim2d.physical.sensors.sensor import Sensor
from sim2d.physical.actuators.actuator import Actuator
from sim2d.physical.kinematics.kinematics import Kinematics


@dataclass
class HardwareGroup:
    """A bundle of physically-related sensors, actuators, and the kinematics
    that ties commands to motion (e.g. drivetrain = motors + encoders +
    mecanum FK/IK).

    A HardwareGroup is the unit a Behaviour drives. Typically only one
    Behaviour writes to a given group per tick — the Supervisor enforces
    that.
    """
    name: str
    kinematics: Kinematics | None = None
    actuators: list[Actuator] = field(default_factory=list)
    sensors: list[Sensor] = field(default_factory=list)

    def apply(self, command: np.ndarray) -> None:
        for actuator, u in zip(self.actuators, command):
            actuator.command(np.atleast_1d(u))

    def integrate(self, dt: float) -> None:
        for actuator in self.actuators:
            actuator.integrate(dt)
