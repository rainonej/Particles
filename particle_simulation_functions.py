# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:15:57 2019

@author: Jordan
"""

import numpy as np

test_data = np.loadtxt("sample.txt", comments='*')
#delimiter and comments can be used to change how it reads the txt file.


"""Write a program that does the following:
    2 particles that start at random positions (np.random.rand)
    1 is spherical, the other is a cube
    radius is .05, side length is 0.08
    density of one is 1, the other is 2
    calculate volume of each particle
    calculate mass of volume of each particle
    calculate gravitational force from eart acting on them
    displace particles randomly for 10 time steps (dt =  0.005sec) (random walk (ignore diffusivity))
    update position and velocity at each step
    save the above path 
    plot the position of at least one of the particles at each step
    """
    
particle = {'mass' : 1, 'density' : 1,  'position' : np.zeros(3), 'velocity' : np.zeros(3), 
            'shape' : 'sphere', 'scale' : 1}

particle2 = {'mass' : 2, 'density' : 1,  'position' : np.zeros(3), 'velocity' : np.zeros(3)+1, 
            'shape' : 'sphere', 'scale' : 1}

wall = { 'shape' : 'wall', 'position' : np.zeros(3), 'angular position' : np.array([1,0,0]), 
        'velocity' : np.zeros(3), 'mass' : 'infinite' }

#particle_position_history = [particle['position']]

def timestep(particle):
    particle['position'] += 2*np.random.rand(3) - 1
    particle['mass'] += 1


"""
def system_info(list_of_particles):
    info = {'energy' : 0, 'momentum' : 'p'}
    
    #Kinetic Energy Calculation
    for i in range(0, len(list_of_particles)):
        m = list_of_particles[i]['mass']
        v = list_of_particles[i]['velocity']
        
        #testing
        #print('mass = ', m, 'and velocity =', v)
        #temp.append(.5*np.linalg.norm(v)**2)
        info['energy'] += .5*np.linalg.norm(v)**2
        if (i == 0):
            info['momentum'] = m*v
        else:
            info['momentum'] += m*v
        
    return info
"""

def get_energy(list_of_particles):
    """enter a list of particles and get the energy as a Float"""
    E = 0
    for i in range(0, len(list_of_particles)):
        m = list_of_particles[i]['mass']
        v = list_of_particles[i]['velocity']
        
        #testing
        #print('mass = ', m, 'and velocity =', v)
        #temp.append(.5*np.linalg.norm(v)**2)
        E += .5*m*np.linalg.norm(v)**2    
        
    return E

def get_momentum(list_of_particles):
    """enter a list of particles and get the momentum as an array"""
    P = 0
    for i in range(0, len(list_of_particles)):
        m = list_of_particles[i]['mass']
        v = list_of_particles[i]['velocity']
        
        #testing
        #print('mass = ', m, 'and velocity =', v)
        #temp.append(.5*np.linalg.norm(v)**2)
        P += m*v
    return P

ball1 = {'mass': 1, 'velocity' : 1}
ball2 = {'mass': 1, 'velocity' : -1}


def one_dim_elastic_collision(particle1, particle2):
    """This should be a more efficient way of doing 1-dim elastic collisions"""
    
    #Rescaling
    m1 = particle1['mass']
    m2 = particle2['mass']
    nm1 = np.sqrt(m1)
    nm2 = np.sqrt(m2)
    v1 = particle1['velocity']
    v2 = particle2['velocity']
    u1 = particle1['velocity']/nm1
    u2 = particle2['velocity']/nm2
    P = m1*v1 + m2*v2
    #writing the velocities as a vector in momentum space
    U = np.array([u1,u2])
    
    #the (unnormalized) normal vector to the plane of reflection
    N = np.array([nm2, -nm1])
    
    #Reflecting
    U -= 2 * np.dot(U, N) * N /(m1+m2)
    
    #un-rescaling
    particle1['velocity'] = U[0]*nm1
    particle2['velocity'] = U[1]*nm2
    
    #testing 
    NewP = get_momentum([particle1, particle2])
    if (P != NewP):
        print('Aha!', P, ' is not ', NewP)


def elastic_collision(particle1, particle2, info = 'none'):
    if (info == 'none'):
        info = {'energy' : 'none', 'momentum' : 'none'}
    if (info['energy'] == 'none'):
        info['energy'] = get_energy([particle1, particle2])
    if (info['momentum'] == 'none'):
        info['momentum'] = get_momentum([particle1, particle2])
        
    #do the math here. The 1 dim case is easy
    
def wall_collision(wall, particle):  
    #to make sure the angle is norm 1
    #I should probably not have to run this everytime
    
    if (np.size(particle['velocity']) == 1):
        particle['velocity'] = -particle['velocity'] 
        
    #to make sure the angle is norm 1
    #I should probably not have to run this everytime    
    elif (np.linalg.norm(wall['angular position']) != 1):
        wall['angular position'] = wall['angular position'] / np.linalg.norm(wall['angular position'])
    else:
        
        particle['velocity'] -= 2*np.dot(particle['velocity'], wall['angular position'])*wall['angular position']
        
    

particle_position_history = [[0,0,0]]

particle_velocity_history = [particle['velocity']]
particle_position_history_x = []

for i in range(0,10):    
    timestep(particle)
    particle_position_history.append(particle['position'].tolist())
    
    #how do I get this to work?
    #a list of arrays will update each time, so I won't store any of the particle's history. 
    #But a List of Lists works
    
for i in range(0, len(particle_position_history)):
    particle_position_history_x.append(particle_position_history[i][0])
    
import matplotlib.pyplot as plt

t = range(0,11)
plt.plot(t,particle_position_history_x, label = "label")
particle_position_history_array = np.array(particle_position_history)

particle_velocity_history_array = particle_position_history_array[1:] - particle_position_history_array[:-1]
#import sys and use sys.exit() to exit out of the program entirely

f = open("position_history.txt", "w")

np.savetxt(f, particle_position_history_x)

f.close()
