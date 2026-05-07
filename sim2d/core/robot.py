from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from sim2d.core.plant import Plant
from sim2d.core.stack import Stack


@dataclass
class Robot:
    """A Robot is the pairing of a Plant (truth-side hardware) with a Stack
    (onboard autonomy). The same Stack should run unchanged against either a
    sim Plant or a hardware Plant — that's the load-bearing seam.
    """
    plant: Plant
    stack: Stack
    start_pose: np.ndarray
