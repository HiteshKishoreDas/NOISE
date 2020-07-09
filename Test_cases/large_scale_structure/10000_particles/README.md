# large_scale_structure: 10000_particles

In this test case, the initial condition has uniformly distributed 10000 particles with no initial velocities.

To get the two point correlation function (TPCF) plot, as shown in **Fig. 5(Left)** in the project report, just **run the command "python3 tp_correlation.py" in the terminal**. It will plot the two point correlation function as **"two_point_corr_180.png"**.

To get the particle distribution plots as shown in **Fig.4(Top row)** in the report, **run "python3 plotter.py"**. This will save Plots from the "output" directory into **"Plots" directory**.



**As this case takes a considerably long time to run due to large number of particles, the obtained output has been included in "output" directory for faster evaluation.** The output only includes the timesteps used in the report to keep the size of the whole project directory small.

Other relevant commands for specific actions:
* If you want to just run the simulations, the outputs are stored in "output" directory: $ python3 run.py 
* If you want to just plot projected positions the outputs, saved in "Plots" directry  : $ python3 plotter.py 
* If you want to just make a video from the Plots made using plotter.py                : $ ./video.txt
