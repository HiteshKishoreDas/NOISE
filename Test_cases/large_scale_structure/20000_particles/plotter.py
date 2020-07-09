#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 02:01:53 2020

@author: hitesh
"""
from config import *

N_t = int(stop_time/step_time)
path_dir = parent_dir+'output/'

if not(os.path.isdir(parent_dir+'Plots/')):
    os.mkdir(parent_dir+'Plots/')

force_sum_x = []
force_sum_y = []
force_sum_z = []

vel_sum_x = []
vel_sum_y = []
vel_sum_z = []

t_list = []

dl = 0.5*(x_end-x_start)
wind = 0.*dl

for out_count in range(N_t+1):
    if os.path.isfile(path_dir+'particle_'+str(out_count)+'.npy'):
        out_data = np.load(path_dir+'particle_'+str(out_count)+'.npy')
        out_info = np.load(path_dir+'info_'+str(out_count)+'.npy',allow_pickle=True).item()
        
        plt.figure()
        plt.scatter(out_data[:,1],out_data[:,2],s=10000./N_particles)
        plt.title('t = '+str(np.round(out_info['t'],4))+' code units')
        plt.xlim(x_start+wind,x_end-wind)
        plt.ylim(y_start+wind,y_end-wind)
        plt.savefig(parent_dir+'Plots/position_'+str(out_count)+'.png')
        print("Plotting done for output file: particle_"+str(out_count)+'......')
        plt.close()
        
