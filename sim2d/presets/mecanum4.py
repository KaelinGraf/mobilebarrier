"""Preset: 4-wheel mecanum drivetrain.

Provides a ready-made HardwareGroup wired with MecanumKinematics so other
projects can drop in a mecanum platform without re-writing the
kinematics/wiring boilerplate. Callers supply their own actuators/sensors,
plus the Stack (estimator, behaviours, supervisor).
"""
from __future__ import annotations
import numpy as np

from sim2d.core.plant import Plant
from sim2d.core.robot import Robot
from sim2d.core.stack import Stack
from sim2d.bodies.body import Body
from sim2d.physical.actuators.actuator import Actuator
from sim2d.physical.hardware_group import HardwareGroup
from sim2d.physical.kinematics.mecanum import MecanumKinematics, MecanumParams
from sim2d.physical.sensors.sensor import Sensor


def make_drivetrain(
        params: MecanumParams,
        actuators: list[Actuator],
        sensors: list[Sensor] | None = None,
        ) -> HardwareGroup:
    return HardwareGroup(
        name="drivetrain",
        kinematics=MecanumKinematics(params),
        actuators=actuators,
        sensors=sensors or [],
    )


def make_mecanum4_robot(
        params: MecanumParams,
        body: Body,
        actuators: list[Actuator],
        stack: Stack,
        sensors: list[Sensor] | None = None,
        start_pose: np.ndarray = np.zeros(3),
        ) -> Robot:
    """Compose a 4-wheel mecanum Robot from caller-supplied hardware and stack."""
    drivetrain = make_drivetrain(params, actuators, sensors)
    plant = Plant(
        body=body,
        hardware_groups=[drivetrain],
        sensors=sensors or [],
    )
    return Robot(plant=plant, stack=stack, start_pose=start_pose)
