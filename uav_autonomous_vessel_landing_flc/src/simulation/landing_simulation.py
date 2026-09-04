import numpy as np

from src.environment.vehicle_models import (
    UAVState,
    VesselState,
    propagate_uav,
    propagate_vessel,
)
from src.fuzzy.landing_fuzzy_controller import LandingFuzzyController
from src.guidance.landing_guidance import (
    heading_to_vessel,
    normalized_landing_inputs,
)


def run_simulation(duration=80.0, dt=0.1):
    """
    Run a generic UAV-to-moving-vessel approach simulation.

    The fuzzy output is interpreted as a descent-angle magnitude.
    """
    uav = UAVState(
        x=0.0,
        y=0.0,
        z=120.0,
        speed=18.0,
        heading=np.deg2rad(20.0),
    )

    vessel = VesselState(
        x=350.0,
        y=120.0,
        speed=4.0,
        heading=np.deg2rad(10.0),
    )

    controller = LandingFuzzyController()

    time = np.arange(0.0, duration + dt, dt)
    uav_log = []
    vessel_log = []
    angle_log = []

    for _ in time:
        uav.heading = heading_to_vessel(uav, vessel)

        alt_n, dist_n, close_n = normalized_landing_inputs(uav, vessel)
        angle_deg = controller.compute(alt_n, dist_n, close_n)

        # Descending flight-path angle.
        gamma = -np.deg2rad(angle_deg)

        uav_log.append([uav.x, uav.y, uav.z])
        vessel_log.append([vessel.x, vessel.y, 0.0])
        angle_log.append(angle_deg)

        if uav.z <= 0.5:
            break

        uav = propagate_uav(uav, gamma, dt)
        vessel = propagate_vessel(vessel, dt)

    return {
        "uav": np.asarray(uav_log),
        "vessel": np.asarray(vessel_log),
        "landing_angle_deg": np.asarray(angle_log),
        "dt": dt,
    }
