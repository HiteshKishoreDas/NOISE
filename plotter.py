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
wind = 0.75*dl

for out_count in range(N_t+1):
    if os.path.isfile(path_dir+'particle_'+str(out_count)+'.npy'):
        out_data = np.load(path_dir+'particle_'+str(out_count)+'.npy')
        out_info = np.load(path_dir+'info_'+str(out_count)+'.npy',allow_pickle=True).item()
        
        plt.figure()
        plt.scatter(out_data[:,1],out_data[:,2],s=100./N_particles)
        plt.title('t = '+str(np.round(out_info['t'],4))+' code units')
        plt.xlim(x_start+wind,x_end-wind)
        plt.ylim(y_start+wind,y_end-wind)
        plt.savefig(parent_dir+'Plots/position_'+str(out_count)+'.png')
        print("Plotting done for output file: particle_"+str(out_count)+'......')
        plt.close()
        
        t_list.append(out_info['t'])
        force_sum_x.append(np.sum(out_data[:,7]))
        force_sum_y.append(np.sum(out_data[:,8]))
        force_sum_z.append(np.sum(out_data[:,9]))

        vel_sum_x.append(np.sum(out_data[:,4]))
        vel_sum_y.append(np.sum(out_data[:,5]))
        vel_sum_z.append(np.sum(out_data[:,6]))

plt.figure()
plt.plot(t_list,force_sum_x)
plt.plot(t_list,force_sum_y)
plt.plot(t_list,force_sum_z)
plt.savefig('force_sum.png')

plt.figure()
plt.plot(t_list,vel_sum_x,label='x')
plt.plot(t_list,vel_sum_y,label='y')
plt.plot(t_list,vel_sum_z,label='z')
plt.legend()
plt.savefig('vel_sum.png')
