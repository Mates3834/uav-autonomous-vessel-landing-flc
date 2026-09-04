from dataclasses import dataclass
import numpy as np


@dataclass
class UAVState:
    x: float
    y: float
    z: float
    speed: float
    heading: float


@dataclass
class VesselState:
    x: float
    y: float
    speed: float
    heading: float


def propagate_uav(state, flight_path_angle, dt):
    """
    Propagate a simple point-mass UAV kinematic model.

    flight_path_angle:
        Positive values climb, negative values descend.
    """
    horizontal_speed = state.speed * np.cos(flight_path_angle)

    return UAVState(
        x=state.x + horizontal_speed * np.cos(state.heading) * dt,
        y=state.y + horizontal_speed * np.sin(state.heading) * dt,
        z=max(0.0, state.z + state.speed * np.sin(flight_path_angle) * dt),
        speed=state.speed,
        heading=state.heading,
    )


def propagate_vessel(state, dt):
    """Propagate a constant-speed planar vessel model."""
    return VesselState(
        x=state.x + state.speed * np.cos(state.heading) * dt,
        y=state.y + state.speed * np.sin(state.heading) * dt,
        speed=state.speed,
        heading=state.heading,
    )


def relative_state(uav, vessel):
    """Return horizontal range, bearing, and altitude above the vessel plane."""
    dx = vessel.x - uav.x
    dy = vessel.y - uav.y

    return {
        "range": float(np.hypot(dx, dy)),
        "bearing": float(np.arctan2(dy, dx)),
        "altitude": float(uav.z),
    }
