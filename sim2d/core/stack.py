from __future__ import annotations
from dataclasses import dataclass, field

from sim2d.stack.estimator import StateEstimator
from sim2d.stack.behaviour import Behaviour
from sim2d.stack.supervisor import Supervisor


@dataclass
class Stack:
    """Onboard-side container: everything that would also run on real hardware.

    A single estimator (fuses all sensor sources), a list of available
    behaviours, and a supervisor that decides which behaviour drives each
    hardware group on a given tick. Behaviours never own filter state — they
    read from `estimator.state`.
    """
    estimator: StateEstimator
    supervisor: Supervisor
    behaviours: list[Behaviour] = field(default_factory=list)
