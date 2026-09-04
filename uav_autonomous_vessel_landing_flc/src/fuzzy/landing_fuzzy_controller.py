import numpy as np

from src.fuzzy.membership import triangular, trapezoidal


class LandingFuzzyController:
    """
    Mamdani-style fuzzy controller for generic landing-angle determination.

    Inputs:
        normalized altitude in [0, 1]
        normalized horizontal range in [0, 1]
        normalized relative closing speed in [-1, 1]

    Output:
        approach angle magnitude in degrees.

    The rule base is intentionally generic and educational.
    """

    def __init__(self):
        self.output_grid = np.linspace(3.0, 25.0, 400)

    def _input_memberships(self, altitude, distance, closing):
        alt = {
            "low": trapezoidal(altitude, -0.1, 0.0, 0.20, 0.45),
            "medium": triangular(altitude, 0.25, 0.55, 0.80),
            "high": trapezoidal(altitude, 0.60, 0.80, 1.0, 1.1),
        }

        dist = {
            "near": trapezoidal(distance, -0.1, 0.0, 0.20, 0.45),
            "medium": triangular(distance, 0.25, 0.55, 0.80),
            "far": trapezoidal(distance, 0.60, 0.80, 1.0, 1.1),
        }

        cls = {
            "opening": trapezoidal(closing, -1.1, -1.0, -0.40, -0.05),
            "steady": triangular(closing, -0.30, 0.0, 0.30),
            "closing": trapezoidal(closing, 0.05, 0.40, 1.0, 1.1),
        }
        return alt, dist, cls

    def _output_memberships(self):
        x = self.output_grid
        return {
            "shallow": trapezoidal(x, 2.0, 3.0, 6.0, 10.0),
            "moderate": triangular(x, 7.0, 13.0, 18.0),
            "steep": trapezoidal(x, 15.0, 19.0, 25.0, 27.0),
        }

    def compute(self, altitude_norm, distance_norm, closing_norm):
        altitude_norm = float(np.clip(altitude_norm, 0.0, 1.0))
        distance_norm = float(np.clip(distance_norm, 0.0, 1.0))
        closing_norm = float(np.clip(closing_norm, -1.0, 1.0))

        alt, dist, cls = self._input_memberships(
            altitude_norm,
            distance_norm,
            closing_norm,
        )
        out = self._output_memberships()

        # Generic rule base:
        # High altitude + near target => steeper approach.
        # Low altitude => shallower approach.
        # Far distance => moderate/shallow approach.
        rules = [
            (min(alt["high"], dist["near"]), "steep"),
            (min(alt["high"], dist["medium"]), "moderate"),
            (min(alt["high"], dist["far"]), "shallow"),
            (min(alt["medium"], dist["near"]), "moderate"),
            (min(alt["medium"], dist["medium"]), "moderate"),
            (min(alt["medium"], dist["far"]), "shallow"),
            (alt["low"], "shallow"),
            (min(cls["closing"], dist["near"]), "shallow"),
            (min(cls["opening"], alt["high"]), "steep"),
        ]

        aggregated = np.zeros_like(self.output_grid)

        for strength, label in rules:
            clipped = np.minimum(float(strength), out[label])
            aggregated = np.maximum(aggregated, clipped)

        area = np.trapz(aggregated, self.output_grid)
        if area <= 1e-12:
            return 10.0

        centroid = np.trapz(
            self.output_grid * aggregated,
            self.output_grid,
        ) / area

        return float(centroid)
