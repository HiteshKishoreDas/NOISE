#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 08:09:31 2020

@author: hitesh

Module to define all the global variables used in the program
Define different parameters related to simulations in this module
Add all the required python modules here.
"""

#### Python modules used ---------------------

import numpy as np
import random as rnd
from matplotlib import pyplot as plt
import time
import os

#### Unit in SI ------------------------------

# solar mass in kilograms
unit_mass   = 1.98847e30

# 1 pc in metres
unit_length = 3.0857e16             

# Myr in seconds
unit_time   = 3.1536e13

#### Derived quantities

# New gravitational constant, G = [M^-1 L^3 T^-2]
G = 6.67408e-11 * (unit_mass*unit_time**2/unit_length**3)

#### Parameters ------------------------------

# Dimensions of simulation box
x_start = 0.
x_end   = 7.

y_start = x_start
y_end   = x_end

z_start = x_start
z_end   = x_end

# End time for the simulation
stop_time = 25.

# Grid size
step_length = 0.25                   

# Time step
step_time   = 0.1

# Number of particles
N_particles = 2

# Maximum initial speed
max_vmag0   = 0.1
       

#### Assignment schemes ------------------------

mass_assign_scheme  = 'CIC'
force_assign_scheme = 'CIC'

#### Time integration scheme -------------------

time_integration_scheme = 'LEAPFROG'

#### Output parameters

parent_dir = './'
output_dt  = 2.*step_time 

#### For expansion

# Dimenstionless Hubble constant
h = 0.5

# Age of universe
t_0 = 9.78*1000./h

# Power in relation for scale factor
# Put a_p = 0 for no expansion
# For matter-dominated universe
#a_p = 2./3. 
# For radiation-dominated universe
#a_p = 1./2.
a_p = 0.

#### Print function ----------------------------

def print_config():
    """
    To print the defined parameters at the start
    """
    
    print ('config.py: Units and G defined.\n')
    print ('Unit mass   : ',unit_mass)
    print ('Unit length : ',unit_length)
    print ('Unit time   : ',unit_time)
    print ('\n',end='')
    
    print ('config.py: Parameters defined.\n')
    print ('x dimension : ',x_start,'  ',x_end)
    print ('y dimension : ',y_start,'  ',y_end)
    print ('z dimension : ',z_start,'  ',z_end)
    print ('t_stop      : ',stop_time)
    print ('dx          : ',step_length)
    print ('dt          : ',step_time)
    print ('v_max       : ',max_vmag0)
    print ('# particles : ',N_particles)
    print ('\n',end='')
    
    print ('config.py: Assignment schemes defined.\n')
    print ('Mass assignment  : ',mass_assign_scheme)
    print ('Force assignment : ',force_assign_scheme)
    print ('\n',end='')

    if a_p!=0:
        print ('config.py: Parameters for expansion defined.\n')
        print ('h     : ',h)
        print ('t_0   : ',t_0)
        print ('a_p   : ',a_p)
        print ('\n',end='')
    

#### Test block ---------------------------------
if __name__=='__main__':
    """
    -----Test block-----
    Run this module as a program to get a list of 
    defined parameters
    """
    print_config()
