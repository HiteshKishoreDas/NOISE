# NOISE: N-body simulation using Particle-Mesh method

This code is written on python 3.7, so please use a version of python that's compatible to run this.

Required python packages:
* numpy
* matplotlib
* random
* time
* os
* astroML (only used in tp_correlation.py for TPCF)

ffmpeg is required to made video clips of obtained snapshots. This feature was not used for the report.

**Please ensure that you have all the required packages installed and running before running this code.**

The code set is given in the current directory with all individual code for the test cases in the directory "Test_cases".

There are 3 test cases:
* 2-body simulation (2_body)
* 3-body simulation (3_body)
* Large scale structure formation (large_scale_structure)

There are 2 cases in 2_body:
* no_initial_velocity
* with_initial_velocity

And there are 2 cases in large_scale_structure:
* 10000_particles
* 20000_particles

**For details about what to do in each case, please read the README file in the corresponding directory.** 

**NOTE: These README files are in markdown format. If they're not showing proper formatting, please open these in gedit or other markdown-compatible text editor.**
