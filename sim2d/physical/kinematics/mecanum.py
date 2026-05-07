import numpy as np
from dataclasses import dataclass

from sim2d.core.params import Params
from sim2d.physical.kinematics.kinematics import Kinematics


@dataclass
class MecanumParams(Params):
    wheel_radius: float = 0.127
    half_wheelbase: float = 0.4
    half_track: float = 0.4
    motor_max_omega: float = 1000.0


class MecanumKinematics(Kinematics):
    # FL, FR, RL, RR
    _S = np.array([-1, 1, 1, -1])

    def __init__(self, params: MecanumParams):
        self.params = params
        Lx, Ly = params.half_wheelbase, params.half_track
        px = np.array([+Lx, +Lx, -Lx, -Lx])
        py = np.array([+Ly, -Ly, +Ly, -Ly])
        S = self._S
        # Each row: (1, s, s*px - py)
        self.jacobian = np.column_stack([np.ones(4), S, S * px - py])

    def IK(self, v: np.ndarray) -> np.ndarray:
        return (self.jacobian @ v) / self.params.wheel_radius

    def FK(self, thetas: np.ndarray) -> np.ndarray:
        # Pseudo-inverse so FK works even though the system is over-determined
        return np.linalg.pinv(self.jacobian) @ (thetas * self.params.wheel_radius)

    def saturate(self, thetas: np.ndarray) -> np.ndarray:
        if np.any(thetas > self.params.motor_max_omega):
            scale_val = np.max(thetas)
            thetas = (thetas / scale_val) * self.params.motor_max_omega
        return thetas
