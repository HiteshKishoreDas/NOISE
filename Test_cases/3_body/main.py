#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 07:43:59 2020
@author: hitesh

Code to stitch different modules together in a specific order
"""
from config import *
import initial_condition as init
import assign as asn
import poisson as ps
import time_integration as tin
    
def main_func (particle=0.,t=0,out_count=0):
    particle0,grid_arr = init.initial()
    
    if t==0:
        particle = np.copy(particle0)

    center_arr = grid_arr+step_length/2.
    
    tin.time_int (particle,center_arr,t,out_count)
    
    print("\nstop_time reached...\n")
