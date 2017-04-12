prob 1
———————
the angle decreases at a constant rate over several periods, this is part of the flaw with RungeKutta solving. The energy of the system is not conserved using this method, and in this case, it appears as if there is a friction causing the pendulum to slow down. Though the pendulum starts at -177 degrees, after one period it is -166.4, and after two it is close to -149.

prob 2
———————
the angle decreases at a slower rate over several periods than the Runge Kutta method. However, if we increase numerical precision, then the energy lost approaches negligable values. Though the pendulum starts at -92 degrees, after one period it lands at -90.9 (using 5000 steps), and -88.3 after two periods. This is a much smaller percentage decrease than with Runge Kutta, and it can be decreased more with added precision (say, 10000 steps or 100000).

prob 3
———————
this gif was super hard to make. It was easy to get just the bob showing up at each timestep, but I wanted to show the parabolic nature of the motion clearly, so I got each position to show up in time with it’s movement, tracing past positions showing not only the interesting movement, but also that the timesteps were well sampled throughout the space (i.e. not just the same 4 positions over and over again, because you can get that motion from just sampling an incorrectly coded pendulum at the right locations pretty easily).