# The Large Angle Pendulum

This repository brings together two related pre university projects that explore the large angle pendulum from different angles: a physics extended essay investigating the problem experimentally and computationally, and a math internal assessment digging into the elliptic integrals that fall out of the theory.

The physics side is what sparked the curiosity in the first place. While studying SHM in class, I noticed that the standard period formula relied on a small angle approximation, which raised the question of what actually happens once the angles get larger. That question led to the experiment and simulation you'll find in `physics-ee/`, where I built a pendulum setup, measured periods across a wide range of starting angles, and compared the results against a numerical simulation.

That same investigation showed that the period at larger angles depends on elliptic integrals rather than the simple small angle formula. `math-ia/` picks up from there, deriving where those integrals come from and working through a series expansion to actually compute them.

Both projects were done before university, but they're ones I still look back on with a lot of fondness, since they were really my first taste of combining theory, experiment, and code to understand something properly.
