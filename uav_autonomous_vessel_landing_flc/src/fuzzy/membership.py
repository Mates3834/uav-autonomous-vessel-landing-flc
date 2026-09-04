import numpy as np


def triangular(x, a, b, c):
    """Triangular membership function."""
    x = np.asarray(x, dtype=float)
    left = (x - a) / (b - a + 1e-12)
    right = (c - x) / (c - b + 1e-12)
    return np.maximum(np.minimum(left, right), 0.0)


def trapezoidal(x, a, b, c, d):
    """Trapezoidal membership function."""
    x = np.asarray(x, dtype=float)
    rise = (x - a) / (b - a + 1e-12)
    fall = (d - x) / (d - c + 1e-12)
    return np.maximum(np.minimum(np.minimum(rise, 1.0), fall), 0.0)
