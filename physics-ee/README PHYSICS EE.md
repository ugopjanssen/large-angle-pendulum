# Experimental and Computational Study of the Large Angle Pendulum

While learning about SHM in IB physics, I noticed the standard period formula relied on a small angle approximation, which raised the question of what happens once the angles get larger.

The experiment measured how the period T of a pendulum varies across initial angles from 15° to 165°. I built a pendulum setup, took precise measurements of the oscillation periods, and compared them against theoretical predictions. Alongside this, I ran a numerical simulation of the pendulum's motion to validate the experimental results and understand the deviation from the small angle approximation more closely. The period increased significantly at larger angles, well beyond what the small angle formula predicts.

The simulation solves the pendulum's differential equation of motion numerically, using a time stepping algorithm that updates angle and angular velocity based on the forces acting on the bob at each step. It supports varying initial angles, so the simulated results could be compared directly against the experimental data to check how well the model held up.
