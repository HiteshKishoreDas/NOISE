#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:39:48 2020
@author: hitesh

Contains function to solve poisson equation using FFT
"""
from config import *

def onebyr (center_arr):
    """
    Returns 1/r array for each center point.
    Used in solution for poisson equation.
    """
    mid_x = (x_end - x_start)/2
    mid_y = (y_end - y_start)/2
    mid_z = (z_end - z_start)/2
    
    N = len(center_arr[0])
    N = len(center_arr[1])
    N = len(center_arr[2])
    
    r_arr = np.zeros((N,N,N))
    
    dx = center_arr[0,:]-mid_x
    dy = center_arr[1,:]-mid_y
    dz = center_arr[2,:]-mid_z
    
    for i in range (N):
        for j in range(N):
            for k in range(N):
                if dx[i]==0.:
                    dx[i] = step_length
                if dy[j]==0.:
                    dy[j] = step_length
                if dz[k]==0.:
                    dz[k] = step_length
                    
                r_arr[i,j,k] = np.sqrt(dx[i]**2+dy[j]**2+dz[k]**2)
    
    return 1/r_arr

def poisson (rho,center_arr):
    """
    To solve the poisson equation
    Uses FFT from numpy and onebyr function above in soluiton
    Returns potential array.
    """
    
    rho_k = np.fft.fftn(rho)
    byr_k = np.fft.fftn(onebyr(center_arr))
    
    phi_k = -G*rho_k*byr_k
    phi   = np.fft.ifftn(phi_k)
    phi   = np.abs(phi)
    
    return phi

if __name__=='__main__':
    """
    -----Test block-----
    Run this module as a program to get the time taken for
    solving poisson equation, phi distribution and particle distribution.
    """
    import initial_condition as init
    import assign as asn
    
    particle,grid_arr = init.initial()
    center_arr = grid_arr+step_length/2.
       
    rho = asn.mass_assign(particle,center_arr)

    start = time.time() 
    phi = poisson(rho,center_arr)
    end = time.time()
    
    print('Time taken: ',end-start, 'sec' )
       
    plt.figure(figsize=(10,10))
    phi_z = np.sum(phi,axis=2)
    plt.imshow(phi_z)
    plt.colorbar()
    
    plt.figure(figsize=(10,10))
    plt.scatter((particle[:,2]/step_length-step_length/2)\
                ,(particle[:,1]/step_length-step_length/2),s=0.001)
    
    plt.show()
    plt.close()