#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:38:15 2020

@author: hitesh
"""
from config import *

def energy_cons (particle):
    
    ax_com = np.sum(particle[:,7])/np.sum(particle[:,0])
    ay_com = np.sum(particle[:,8])/np.sum(particle[:,0])
    az_com = np.sum(particle[:,9])/np.sum(particle[:,0])

    particle[:,7] -= particle[:,0]*ax_com
    particle[:,8] -= particle[:,0]*ay_com
    particle[:,9] -= particle[:,0]*az_com
    
    return particle

def momentum_cons (particle):
    
    if os.path.isfile(path_dir+'particle_0.npy'):
        particle_initial = np.load(path_dir+'particle_0.npy')

    vx_com0 = np.sum(particle_initial[:,0]*particle_initial[:,4])\
                /np.sum(particle_initial[:,0])          
    vy_com0 = np.sum(particle_initial[:,0]*particle_initial[:,5])\
                /np.sum(particle_initial[:,0])          
    vz_com0 = np.sum(particle_initial[:,0]*particle_initial[:,6])\
                /np.sum(particle_initial[:,0])
                
    vx_com = np.sum(particle[:,0]*particle[:,4])/np.sum(particle[:,0])
    vy_com = np.sum(particle[:,0]*particle[:,5])/np.sum(particle[:,0])
    vz_com = np.sum(particle[:,0]*particle[:,6])/np.sum(particle[:,0])
    
    particle[:,4] -= vx_com-vx_com0
    particle[:,5] -= vy_com-vy_com0
    particle[:,6] -= vz_com-vz_com0
    
    return particle
    
