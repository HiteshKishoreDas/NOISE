#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:43:10 2020
@author: hitesh

Contains functions to assign mass to gridpoints and force to the particles
"""
from config import *
import conservation as cons

def top_hat (x):
    """
    Top-hat function for assignment function
    Takes an array and outputs corresponding function value
    """
    t = np.abs(x)<0.5
    t = t*1.
    t[np.abs(x)==0.5] = 0.5
    
    return t

def triangle (x):
    """
    Triangle function for assigment function
    Takes an array and outputs corresponding function value
    """
    t = np.abs(x)<1.
    t = t*1.
    t = t*(1.-np.abs(x))
    return t

def W_NGP (x,y,z):
    """
    Assignment function for Nearest grid-point assignment scheme
    """
    return top_hat(x/step_length)*top_hat(y/step_length)*top_hat(z/step_length)

def W_CIC (x,y,z):
    """
    Assignment function for Cloud-in-cell assignment scheme
    """
    return triangle(x/step_length)*triangle(y/step_length)*triangle(z/step_length)
    
def assign_scheme ():
    """
    Return the required assignment function and extent of influence
    """
    if mass_assign_scheme == 'NGP':
        W_mass = W_NGP
        n_mass = 0
    elif mass_assign_scheme == 'CIC':
        W_mass = W_CIC
        n_mass = 1
    else:
        raise ValueError('assign.py: Invalid mass assignment scheme...')
    
    if force_assign_scheme == 'NGP':
        W_force = W_NGP
        n_force = 0
    elif force_assign_scheme == 'CIC':
        W_force = W_CIC
        n_force = 1
    else:
        raise ValueError('assign.py: Invalid force assignment scheme...')
        
    return W_mass,W_force,n_mass,n_force

W_mass,W_force,n_mass,n_force = assign_scheme()

def mass_assign (particle,center_arr):
    """
    For mass assignment to grid centers
    Returns a density field
    """
    N = len(center_arr[0])
    N = len(center_arr[1])
    N = len(center_arr[2])
    
    rho = np.zeros((N,N,N))
    
    i = (particle[:,1]/step_length).astype(int)
    j = (particle[:,2]/step_length).astype(int)
    k = (particle[:,3]/step_length).astype(int)
    
    count = np.zeros(N_particles)
    
    di_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    dj_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    dk_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    
    for dd in range(-n_mass,n_mass+1):
        di_arr[dd,:,:] = dd
        dj_arr[:,dd,:] = dd
        dk_arr[:,:,dd] = dd
    
    for p in range(N_particles):
        
        dx = np.abs(center_arr[0,(i[p]+di_arr)%N] - particle[p,1])
        dy = np.abs(center_arr[1,(j[p]+dj_arr)%N] - particle[p,2])
        dz = np.abs(center_arr[2,(k[p]+dk_arr)%N] - particle[p,3])
        
        # To account for grid centers near boundary
        cond_dx = dx>((n_mass+1)*step_length)
        cond_dy = dy>((n_mass+1)*step_length)
        cond_dz = dz>((n_mass+1)*step_length)
        
        dx = dx + cond_dx*((x_end-x_start) - 2*dx)
        dy = dy + cond_dy*((y_end-y_start) - 2*dy)
        dz = dz + cond_dz*((z_end-z_start) - 2*dz)
                       
        rho[(i[p]+di_arr)%N,(j[p]+dj_arr)%N,(k[p]+dk_arr)%N] += particle[p,0]*W_mass(dx,dy,dz)        
        
    return rho/(step_length**3)

def force_assign (particle,Fx,Fy,Fz,center_arr):
    """
    For mass assignment to grid centers
    Returns a density field
    """
    N = len(center_arr[0])
    N = len(center_arr[1])
    N = len(center_arr[2])
    
    rho = np.zeros((N,N,N))
    
    i = (particle[:,1]/step_length).astype(int)
    j = (particle[:,2]/step_length).astype(int)
    k = (particle[:,3]/step_length).astype(int)
    
    count = np.zeros(N_particles)
    
    di_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    dj_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    dk_arr = np.zeros((2*n_mass+1,2*n_mass+1,2*n_mass+1),dtype=int)
    
    for dd in range(-n_mass,n_mass+1):
        di_arr[dd,:,:] = dd
        dj_arr[:,dd,:] = dd
        dk_arr[:,:,dd] = dd
    
    for p in range(N_particles):
        
        dx = np.abs(center_arr[0,(i[p]+di_arr)%N] - particle[p,1])
        dy = np.abs(center_arr[1,(j[p]+dj_arr)%N] - particle[p,2])
        dz = np.abs(center_arr[2,(k[p]+dk_arr)%N] - particle[p,3])
        
        # To account for grid centers near boundary
        cond_dx = dx>((n_mass+1)*step_length)
        cond_dy = dy>((n_mass+1)*step_length)
        cond_dz = dz>((n_mass+1)*step_length)
        
        dx = dx + cond_dx*((x_end-x_start) - 2*dx)
        dy = dy + cond_dy*((y_end-y_start) - 2*dy)
        dz = dz + cond_dz*((z_end-z_start) - 2*dz)
                       
        W = W_mass(dx,dy,dz)
        
        particle[p,7] = np.sum(W*Fx[(i[p]+di_arr)%N,(j[p]+dj_arr)%N,(k[p]+dk_arr)%N])
        particle[p,8] = np.sum(W*Fy[(i[p]+di_arr)%N,(j[p]+dj_arr)%N,(k[p]+dk_arr)%N])
        particle[p,9] = np.sum(W*Fz[(i[p]+di_arr)%N,(j[p]+dj_arr)%N,(k[p]+dk_arr)%N])
        
    particle = cons.energy_cons(particle)
    
    return particle
    
if __name__=='__main__':
    """
    -----Test block-----
    Run this module as a program to get the time taken for
    mass and force assignment
    """
    import initial_condition as init
    import poisson as ps
    import force as fr    

    particle,grid_arr = init.initial()
    center_arr = grid_arr+step_length/2.
    
    start = time.time()
    
    rho = mass_assign(particle,center_arr)
    
    end = time.time()
    print('Time taken for mass assignment: ',str(end-start),'sec')
    
    plt.figure(figsize=(10,10))
    rho_z = np.sum(rho,axis=2)
    plt.imshow(rho_z)
    plt.colorbar()
    
    plt.figure(figsize=(10,10))
    plt.scatter((particle[:,2]/step_length-step_length/2)\
                ,(particle[:,1]/step_length-step_length/2))
    
    phi = ps.poisson(rho,center_arr)
    Fx,Fy,Fz = fr.force(phi,rho)

    start = time.time()   
    particle = force_assign(particle,Fx,Fy,Fz,center_arr)
    end = time.time()
    print('Time taken for force assignment : ',end-start, 'sec' )
    
    plt.show()
    plt.close()
