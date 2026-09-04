# Fuzzy Logic Based UAV Landing on an Autonomous Vessel

A simulation-oriented autonomous landing project investigating the use of
**Fuzzy Logic Control (FLC)** for determining an appropriate UAV landing
approach angle toward an autonomous surface vessel.

The project focuses on the interaction between UAV flight conditions,
environmental effects, and landing geometry within an autonomous maritime
operation.

---

## Overview

Landing an Unmanned Aerial Vehicle (UAV) on a surface vessel introduces a
challenging control problem due to the interaction between aerial vehicle
dynamics, environmental disturbances, and the landing platform.

This project investigates a fuzzy-logic-based approach for determining the
UAV landing angle using flight and environmental information.

The main areas of the project are:

- UAV landing simulation
- Autonomous vessel landing
- Fuzzy Logic Control
- Landing-angle determination
- Environmental disturbance consideration
- Autonomous aerial-maritime operations
- 3D trajectory visualization

---

## System Concept

The proposed architecture is conceptually structured as:

```text
         UAV States
             │
             │
      Environmental Data
             │
             ▼
     Fuzzy Logic Controller
             │
             ▼
      Landing Angle
             │
             ▼
      Descent Dynamics
             │
             ▼
    Autonomous Vessel
```

The objective of the fuzzy controller is to determine an appropriate
landing approach according to the current operating conditions.

---

## UAV Model

The simulation represents several UAV operating variables, including:

- Altitude
- Airspeed
- Wind speed
- Landing angle
- Descent behavior

These variables provide the basis for evaluating the landing approach.

---

## Fuzzy Logic Controller

The intended FLC architecture maps UAV and environmental information to a
landing-angle command.

A general structure is:

```text
UAV / Environment States
          │
          ▼
      Fuzzification
          │
          ▼
       Rule Base
          │
          ▼
   Fuzzy Inference
          │
          ▼
    Defuzzification
          │
          ▼
 Landing-Angle Command
```

The final implementation is intended to include:

- Input membership functions
- Output membership functions
- Fuzzy rule base
- Inference mechanism
- Defuzzification
- Landing-angle constraints

---

## Landing-Angle Determination

The landing-angle command determines the UAV descent behavior during the
approach to the vessel.

The controller is intended to consider the relationship between:

- Current altitude
- UAV velocity
- Wind conditions
- Required descent behavior

rather than relying on a fixed landing angle.

---

## Autonomous Maritime Landing

The project is motivated by UAV operations involving autonomous or
unmanned surface platforms.

Conceptually:

```text
              UAV
               │
               │ Landing Approach
               ▼
       ┌─────────────────┐
       │ Autonomous      │
       │ Surface Vessel  │
       └─────────────────┘
```

The combination of aerial and maritime autonomous systems provides a basis
for investigating cooperative multi-domain autonomy.

---

## Current Simulation

The current Python prototype defines a UAV with:

- Initial altitude
- UAV speed
- Wind speed
- Landing-angle variable

The simulation progressively reduces UAV altitude according to the selected
landing angle and records the landing behavior over time.

A 3D visualization is used to represent:

```text
Time × Landing Angle × Altitude
```

---

## Current Development Status

The current prototype establishes the UAV and landing simulation
environment.

**Important:** The current Python implementation uses a preliminary
landing-angle generator rather than a complete fuzzy inference system.

The next development stage is to replace this preliminary mechanism with
the complete FLC architecture consisting of:

1. Membership functions
2. Fuzzy rule base
3. Inference mechanism
4. Defuzzification
5. Constraint handling
6. Controller validation

---

## Planned Evaluation

Following implementation of the complete FLC, the controller can be
evaluated under different:

- UAV altitudes
- UAV velocities
- Wind conditions
- Landing geometries

Potential performance metrics include:

- Landing-angle behavior
- Descent time
- Approach stability
- Sensitivity to wind
- Landing accuracy

---

## Technologies

- Python
- NumPy
- Matplotlib
- Fuzzy Logic
- UAV Simulation
- Autonomous Systems
- Maritime Autonomy

---

## Research Areas

- Autonomous Systems
- Unmanned Aerial Vehicles
- Unmanned Surface Vehicles
- Fuzzy Logic Control
- Autonomous Landing
- Guidance and Control
- Multi-Domain Autonomy

---

## Repository Structure

```text
uav-autonomous-vessel-landing-flc/
│
├── README.md
│
├── src/
│   ├── uav_model/
│   ├── fuzzy_controller/
│   └── landing_simulation/
│
├── fuzzy/
│   ├── membership_functions/
│   └── rule_base/
│
├── scenarios/
│
├── results/
│   ├── landing_trajectory/
│   ├── landing_angle/
│   └── sensitivity_analysis/
│
└── docs/
```

---

## Project Status

**Under development**

Initial UAV landing simulation and visualization have been implemented.
The complete fuzzy inference architecture and systematic controller
evaluation are planned as the next development stage.
