#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 07:45:03 2020
@author: hitesh

Run this python file to start the simulation with otptions for restart
"""
from config import *
import argparse 
import main
import time
  
# Initialize parser 
parser = argparse.ArgumentParser() 
  
# Adding optional argument 
parser.add_argument("-r", "--restart", help = "Restart simulation from the given timestep") 
  
# Read arguments from command line 
args = parser.parse_args() 
  
if args.restart: 
    restart_file = int(args.restart)
    
    path_dir = parent_dir+'output/'
    
    out_data = np.load(path_dir+'particle_'+str(restart_file)+'.npy')
    out_info = np.load(path_dir+'info_'+str(restart_file)+'.npy',allow_pickle=True).item()
    
    restart_t = out_info['t']
    
    print('Restart from : particle_'+str(restart_file)+'.npy\n')

    start_t = time.time()
    main.main_func(out_data,restart_t,restart_file)
    end_t = time.time()
    
else:
    restart_t = 0.
    start_t = time.time()
    main.main_func()
    end_t = time.time()
    
t_taken = (end_t-start_t)/60.
timesteps = (stop_time-restart_t)/step_time
grids = int((x_end-x_start)/step_length)
print("Total time taken            : "+str(t_taken)+' min')
print("Number of grids             : "+str(grids**3))
print("Avg. time taken per timestep: "+str(t_taken/timesteps)+' min')

