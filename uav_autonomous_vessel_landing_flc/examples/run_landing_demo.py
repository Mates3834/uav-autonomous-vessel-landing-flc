import matplotlib.pyplot as plt

from src.simulation.landing_simulation import run_simulation


result = run_simulation()

uav = result["uav"]
vessel = result["vessel"]
angle = result["landing_angle_deg"]
dt = result["dt"]

t = dt * range(len(angle))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(uav[:, 0], uav[:, 1], uav[:, 2], label="UAV")
ax.plot(vessel[:, 0], vessel[:, 1], vessel[:, 2], label="Vessel")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("Altitude [m]")
ax.set_title("Generic UAV-to-Vessel Landing Approach")
ax.legend()
plt.show()

plt.figure()
plt.plot(list(t), angle)
plt.xlabel("Time [s]")
plt.ylabel("Fuzzy approach angle [deg]")
plt.title("Fuzzy Landing-Angle Command")
plt.grid(True)
plt.show()
