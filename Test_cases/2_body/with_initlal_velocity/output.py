#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 07:42:20 2020
@author: hitesh

Contains function for output of data at different timesteps
"""
from config import *

def output (particle,t,parent_dir):
    """
    Saves the particle array at time t in "output" directory
    in parent directory. The "output" directory is created if
    it doesn't exist
    """
    path_dir = parent_dir+'/output/'
    
    if os.path.isdir(path_dir):
        np.save(path_dir+'particle_'+str(t),particle)
        print('Writing file: particle_'+str(t)+'......')
    else:
        os.mkdir(path_dir)
        output (particle,t,parent_dir)
        
def output_info (out_data,t,parent_dir):
    """
    Saves the output info file as csv in "output" directory
    in parent directory. The "output" directory is created if
    it doesn't exist
    """
    path_dir = parent_dir+'/output/'
    
    if os.path.isdir(path_dir):
        np.save(path_dir+'info_'+str(t),out_data)
        print('Writing file:     info_'+str(t)+'......')
    else:
        os.mkdir(path_dir)
        output (out_data,t,parent_dir)
