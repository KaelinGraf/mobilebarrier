"""Project-specific composition: the motorway barrier robot.

Wires the sim2d mecanum4 preset together with the barrier's specific
sensor suite, behaviours (cruise, dock), and stack configuration.
"""
from __future__ import annotations
import numpy as np

from sim2d.core.robot import Robot
from sim2d.physical.kinematics.mecanum import MecanumParams


def make_barrier_robot(start_pose: np.ndarray = np.zeros(3)) -> Robot:
    raise NotImplementedError("compose Plant + Stack from sim2d pieces here")
