from __future__ import annotations
from dataclasses import dataclass, field

from sim2d.bodies.body import Body
from sim2d.physical.hardware_group import HardwareGroup
from sim2d.physical.sensors.sensor import Sensor


@dataclass
class Plant:
    """Truth-side container: the robot's physical embodiment.

    Owns the rigid body, hardware groups (motors+encoders+kinematics), and
    any standalone sensors that aren't tied to a single group (e.g. a
    body-mounted lidar). The world steps the Plant forward; the Stack reads
    measurements from it and writes commands back via HardwareGroup.apply().
    """
    body: Body
    hardware_groups: list[HardwareGroup] = field(default_factory=list)
    sensors: list[Sensor] = field(default_factory=list)

    def all_sensors(self) -> list[Sensor]:
        out = list(self.sensors)
        for hg in self.hardware_groups:
            out.extend(hg.sensors)
        return out

    def group(self, name: str) -> HardwareGroup:
        for hg in self.hardware_groups:
            if hg.name == name:
                return hg
        raise KeyError(f"no hardware group named {name!r}")

    def integrate(self, dt: float) -> None:
        """Advance the plant by dt: actuator dynamics + body dynamics. Called
        by the World during the integration phase, after all robots have
        committed their commands.
        """
        for hg in self.hardware_groups:
            hg.integrate(dt)
        # TODO: integrate body dynamics using staged actuator forces /
        # wheel velocities (route through HardwareGroup.kinematics).
