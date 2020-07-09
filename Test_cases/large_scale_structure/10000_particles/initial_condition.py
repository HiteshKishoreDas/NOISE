#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 08:54:48 2020
@author: hitesh

Contains function to define the function for initial conditions
Change initial() to change the initial condition of the simulation
"""
from config import *

def rand_spherical (rad):
    
    r = rnd.uniform(0.,rad)
    th = rnd.uniform(0.,np.pi)
    ph = rnd.uniform(0.,2*np.pi)
    
    x = r*np.sin(th)*np.cos(ph)
    y = r*np.sin(th)*np.sin(ph)
    z = r*np.cos(th)
    
    return x,y,z

def initial():
    """
    To create the initial condition for the simulation
    Returns the grid array and particle array with mass,
    position and velocity
    """
    
    print_config()
    
    x_arr = np.arange(x_start,x_end,step_length)
    y_arr = np.arange(y_start,y_end,step_length)
    z_arr = np.arange(z_start,z_end,step_length)
    
    grid_arr = np.array([x_arr,y_arr,z_arr])
    
    particle_pos = np.array([[rnd.uniform(x_start,x_end),\
                              rnd.uniform(y_start,y_end),\
                              rnd.uniform(z_start,z_end)]\
                              for i in range(N_particles)])

    particle_vel = np.array([rand_spherical(max_vmag0) for i in range(N_particles)])
    
    particle_mass = np.array([2e5 for i in range(N_particles)])
    particle_force = np.zeros_like(particle_mass)
    
    particle = np.column_stack([particle_mass,\
                         particle_pos[:,0],particle_pos[:,1],particle_pos[:,2],\
                         particle_vel[:,0],particle_vel[:,1],particle_vel[:,2],\
                         particle_force,particle_force,particle_force])
    
    del (x_arr,y_arr,z_arr)
    del (particle_mass)
    del (particle_pos)
    del (particle_vel)
    
    return (particle,grid_arr)

if __name__ == '__main__':
    """
    -----Test block-----
    Run this module as a program to get mass distribution, 
    position scatter and velocity scatter of initial condition.
    """
    
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    part,grid = initial()
    print('Wait for the plots...')
    
    plt.figure()
    plt.hist(part[:,0])
    plt.title('Mass distribution')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(part[:,1],part[:,2],part[:,3])
    plt.title('Position scatter')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(part[:,4],part[:,5],part[:,6])
    plt.title('Velocity scatter')
    
    plt.show()
    plt.close()
