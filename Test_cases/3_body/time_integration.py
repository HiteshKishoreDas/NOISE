#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 07:38:48 2020
@author: hitesh

Contains function for calculating velocity and displacement in next timestep
using leapfrog method.
"""
from config import *
import force as fr
import output as ot
import conservation as cons

def leapfrog (particle,center_arr,t=0,out_count=0,testflag=False):
    """
    For time integration using leapfrog method
    """    
    dl = x_end-x_start
    
    if not(testflag):
        # Output the initial condition and output info
        ot.output(particle,out_count,parent_dir)
    
        out_info = {'t':0.,'dt':step_time}
        ot.output_info(out_info,out_count,parent_dir)
    
    # Add forces of initial condition to particle array
    particle_mid = np.copy(fr.partice_to_force(particle,center_arr))
    
    # Calculate acceleration of initial condition
    a_mid = np.transpose(np.transpose(particle_mid[:,7:10])/particle_mid[:,0])
    
    # Forward euler half step to mid step using initial condition
    particle_mid[:,1:4] += 0.5*step_time*particle_mid[:,4:7]
    particle_mid[:,1:4] %= dl
    particle_mid[:,4:7] += 0.5*step_time*a_mid
        
    # Calculate force for mid step
    particle_mid = fr.partice_to_force(particle_mid,center_arr)
    
    if testflag:
        N_t = 1
    else:
        N_t = int(stop_time/step_time)
    
    particle2 = np.copy(particle)
    
    while t<=N_t:
        t += 1
        
        # Acceleration of mid step
        a_mid = np.transpose(np.transpose(particle_mid[:,7:10])/particle_mid[:,0])
        
        # Forward step of main step using mid step
        particle2[:,1:4] += step_time*particle_mid[:,4:7]
        particle2[:,1:4] %= dl
        particle2[:,4:7] += step_time*a_mid
        
        # Calculate force of main step for new coordinates
        particle2 = fr.partice_to_force(particle2,center_arr)
        
        print("Time step completed: t = "+str(np.round(t*step_time,10))+"......")
        print(str(np.round(t*step_time*100./stop_time,4))+"% completed......")

        if t%int(output_dt/step_time)==0 and not(testflag):
            out_count += 1
            ot.output(particle2,out_count,parent_dir)
            out_info['t'] = t*step_time
            ot.output_info(out_info,out_count,parent_dir)
            
        # Acceleration of new main step
        a = np.transpose(np.transpose(particle2[:,7:10])/particle2[:,0])
    
        # Forward step of mid step using main step
        particle_mid[:,1:4] += step_time*particle2[:,4:7]
        particle_mid[:,1:4] %= dl
        particle_mid[:,4:7] += step_time*a
        
        # Calculate force of mid step for new coordinates
        particle_mid = fr.partice_to_force(particle_mid,center_arr)

def time_int_func ():
    """
    Return the required time integration function
    """
    if  time_integration_scheme == 'LEAPFROG':
        f_TI = leapfrog
#    elif time_integration_scheme == 'RK4':
#        f_TI = range_kutta_4
    else:
        raise ValueError('time_integration.py: Invalid time integration scheme...')
        
    return f_TI

time_int = time_int_func()

if __name__=='__main__':
    """
    -----Test block-----
    Run this module to get the time taken for one time integration step
    """
    
    import initial_condition as init
    import assign as asn
    import poisson as ps
    import time    

    particle,grid_arr = init.initial()
    center_arr = grid_arr+step_length/2.
    
    start = time.time()
    time_int (particle,center_arr,testflag=True)
    end = time.time()

    print("Time taken for one time integration step: "+str(end-start)+" sec")
    
