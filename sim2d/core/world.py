from __future__ import annotations

from sim2d.bodies.body import Body
from sim2d.core.robot import Robot

PHYSICS_TIMESTEP = 0.001  # seconds per physics tick
GRAVITY = 9.81


class World:
    """Top-level simulation harness. Owns time, static/dynamic bodies, and
    the robots in the scene.

    `step` is strictly two-phase: every robot senses, estimates, and decides
    against the current world state, *then* every robot's commands are
    integrated together. This keeps multi-robot motion simultaneous — no
    robot ever sees a partially-updated world.
    """

    def __init__(self, robots: list[Robot], bodies: list[Body] | None = None):
        self.robots = robots
        self.bodies = bodies or []
        self.t = 0.0

    def step(self, dt: float = PHYSICS_TIMESTEP) -> None:
        for r in self.robots:
            estimate = r.stack.estimator.state
            active = r.stack.supervisor.select(self.t, estimate)
            if active is not None:
                command = active.update(self.t, estimate)
                active.target.apply(command)  # stages command on actuators


        for r in self.robots:
            r.plant.integrate(dt)
        for body in self.bodies:
            body.update()

        self.t += dt
