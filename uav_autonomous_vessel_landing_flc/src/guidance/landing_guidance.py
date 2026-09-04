import numpy as np


def wrap_angle(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi


def heading_to_vessel(uav, vessel):
    """Return heading command toward the moving vessel."""
    return float(np.arctan2(vessel.y - uav.y, vessel.x - uav.x))


def closing_speed(uav, vessel):
    """
    Approximate relative closing speed along line of sight.
    Positive value means closing.
    """
    dx = vessel.x - uav.x
    dy = vessel.y - uav.y
    distance = np.hypot(dx, dy)

    if distance < 1e-9:
        return 0.0

    los = np.array([dx, dy]) / distance

    vu = np.array([
        uav.speed * np.cos(uav.heading),
        uav.speed * np.sin(uav.heading),
    ])
    vv = np.array([
        vessel.speed * np.cos(vessel.heading),
        vessel.speed * np.sin(vessel.heading),
    ])

    return float(np.dot(vu - vv, los))


def normalized_landing_inputs(
    uav,
    vessel,
    max_altitude=150.0,
    max_range=500.0,
    max_closing_speed=30.0,
):
    """Generate normalized fuzzy-controller inputs."""
    distance = np.hypot(vessel.x - uav.x, vessel.y - uav.y)
    closing = closing_speed(uav, vessel)

    return (
        float(np.clip(uav.z / max_altitude, 0.0, 1.0)),
        float(np.clip(distance / max_range, 0.0, 1.0)),
        float(np.clip(closing / max_closing_speed, -1.0, 1.0)),
    )
