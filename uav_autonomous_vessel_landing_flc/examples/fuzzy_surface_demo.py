import numpy as np
import matplotlib.pyplot as plt

from src.fuzzy.landing_fuzzy_controller import LandingFuzzyController


controller = LandingFuzzyController()

altitudes = np.linspace(0.0, 1.0, 35)
distances = np.linspace(0.0, 1.0, 35)

A, D = np.meshgrid(altitudes, distances)
Z = np.zeros_like(A)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        Z[i, j] = controller.compute(
            A[i, j],
            D[i, j],
            closing_norm=0.0,
        )

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(A, D, Z)
ax.set_xlabel("Normalized altitude")
ax.set_ylabel("Normalized distance")
ax.set_zlabel("Approach angle [deg]")
ax.set_title("Generic Fuzzy Control Surface")
plt.show()
