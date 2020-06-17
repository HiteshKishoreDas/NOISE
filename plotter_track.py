#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 02:01:53 2020

@author: hitesh
"""
from config import *

N_t = int(stop_time/step_time)
path_dir = parent_dir+'output/'

t_list = []
x_list = []
y_list = []
z_list = []

dl = 0.5*(x_end-x_start)
wind = 0.75*dl

color_list = ['tab:orange','tab:blue','tab:green']

for out_count in range(N_t+1):
    if os.path.isfile(path_dir+'particle_'+str(out_count)+'.npy'):
        out_data = np.load(path_dir+'particle_'+str(out_count)+'.npy')
        out_info = np.load(path_dir+'info_'+str(out_count)+'.npy',allow_pickle=True).item()
        
        t_list.append(out_info['t'])
        x_list.append(out_data[:,1])
        y_list.append(out_data[:,2])
        z_list.append(out_data[:,3])

        print('Read position from particle_'+str(out_count)+'......')

x_list = np.array(x_list)
y_list = np.array(y_list)
z_list = np.array(z_list)

plt.figure(figsize=(8,8))
for i in range(N_particles):
    plt.plot(x_list[:,i],y_list[:,i],c=color_list[i],linestyle='dashed',linewidth=3)

    plt.scatter(x_list[-1,i],y_list[-1,i],c=color_list[i],s=200)
    plt.scatter(x_list[0,i],y_list[0,i],c=color_list[i],s=200,marker='X')

plt.xlabel("x-coordinate (in code units)",fontsize=15)
plt.ylabel("y-coordinate (in code units)",fontsize=15)
plt.tick_params(labelsize=15)
plt.savefig('position_track.png')
