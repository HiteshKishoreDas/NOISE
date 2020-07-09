# large_scale_structure: 20000_particles

In this test case, the initial condition has uniformly distributed 20000 particles with no initial velocities.

To get the two point correlation function (TPCF) plot, as shown in **Fig. 5(middle)** in the project report, just **run the command "python3 tp_correlation.py" in the terminal**. It will plot the two point correlation function as **"two_point_corr_4.png"**.

To get the particle distribution plots as shown in **Fig. 3(Middle row)** in the report, **run "python3 plotter.py"**. This will save Plots from the "output" directory into **"Plots" directory**.



**As this case takes a considerably long time to run due to large number of particles, the obtained output has been included in "output" directory for faster evaluation. It may not even run in many desktop computers with less RAM.** I used a cluster core for this test case.

Other relevant commands for specific actions:
* If you want to just run the simulations, the outputs are stored in "output" directory: $ python3 run.py 
* If you want to just plot projected positions the outputs, saved in "Plots" directry  : $ python3 plotter.py 
* If you want to just plot the trajectory of the particles as "position_track.png"     : $ python3 plotter_track.py 
* If you want to just make a video from the Plots made using plotter.py                : $ ./video.txt

