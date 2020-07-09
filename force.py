#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:22:42 2020

@author: hitesh
"""
from config import *
import assign as asn
import poisson as ps

def force (phi,rho):
    N = np.size(phi[:,0,0])
    
    Fx = np.zeros((N,N,N),dtype=float)
    Fy = np.zeros((N,N,N),dtype=float)
    Fz = np.zeros((N,N,N),dtype=float)
    
    Fx = 0.5*rho*(np.roll(phi,1,axis=0)-np.roll(phi,-1,axis=0))/step_length
    Fy = 0.5*rho*(np.roll(phi,1,axis=1)-np.roll(phi,-1,axis=1))/step_length
    Fz = 0.5*rho*(np.roll(phi,1,axis=2)-np.roll(phi,-1,axis=2))/step_length
    
    return Fx,Fy,Fz

def partice_to_force (particle,center_arr):
    
    rho = asn.mass_assign(particle,center_arr)
    phi = ps.poisson(rho,center_arr)
     
    Fx,Fy,Fz = force(phi,rho)
       
    particle = asn.force_assign(particle,Fx,Fy,Fz,center_arr)
    
    return particle

if __name__=='__main__':
    """
    -----Test block-----
    Run this module as a program to get the time taken for
    force calculation and force distribution.
    """
    import initial_condition as init
    import assign as asn
    import poisson as ps
    
    particle,grid_arr = init.initial()
    center_arr = grid_arr+step_length/2.
    
    rho = asn.mass_assign(particle,center_arr)
    phi = ps.poisson(rho,center_arr)
    
    start = time.time()   
    Fx,Fy,Fz = force(phi,rho)
    end = time.time()
    print('Time taken for force calculation: ',end-start, 'sec' )
    
#    Uncomment following line if you want to test particle_to_force function
#    
#    particle = partice_to_force (particle,center_arr)
       
    plt.figure(figsize=(10,10))
    Fx_z = np.sum(Fx,axis=2)
    plt.imshow(Fx_z)
    plt.title(r'$F_x$ projection along z')
    plt.colorbar()

    plt.figure(figsize=(10,10))
    Fy_z = np.sum(Fy,axis=2)
    plt.imshow(Fy_z)
    plt.title(r'$F_y$ projection along z')
    plt.colorbar()
    
    plt.figure(figsize=(10,10))
    Fz_z = np.sum(Fz,axis=2)
    plt.imshow(Fz_z)
    plt.title(r'$F_z$ projection along z')
    plt.colorbar()
    
#    Increase particle size if number of particles is low
    plt.figure(figsize=(10,10))
    plt.scatter((particle[:,2]/step_length-step_length/2)\
                ,(particle[:,1]/step_length-step_length/2),s=1)
    
    plt.show()
    plt.close()
    
    
    
