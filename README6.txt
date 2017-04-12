prob 1
———————
the angle decreases at a constant rate over several periods, this is part of the flaw with RungeKutta solving. The energy of the system is not conserved using this method, and in this case, it appears as if there is a friction causing the pendulum to slow down. Though the pendulum starts at -177 degrees, after one period it is -166.4, and after two it is close to -149.

prob 2
———————


prob 3
———————
this gif was super hard to make. It was easy to get just the bob showing up at each timestep, but I wanted to show the parabolic nature of the motion clearly, so I got each position to show up in time with it’s movement, tracing past positions showing not only the interesting movement, but also that the timesteps were well sampled throughout the space (i.e. not just the same 4 positions over and over again, because you can get that motion from just sampling an incorrectly coded pendulum at the right locations pretty easily)