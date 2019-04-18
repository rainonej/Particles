# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:03:36 2019

@author: Jordan
"""

import Particle_class
from Particle_class import *
import collision_functions
from collision_functions import *
import numpy as np

#number of digits - 1
#only works for n = 1, 2, 3, 4
#when n=5, m2 = M = 10000000000  and  M**2 - (1 + 1/M) * (M**2 - M) == 0 in python.


#I need to rework some stuff
#1 change the test function in the Particle class to work for 1-dim floats instead of just arrays
#2 finish writing this script
#3 off load this data into a pkl file

def get_balls(n):

    ball1 = Particle(np.array([1]), np.array([0]))
    ball1.mass = 1

    ball2 = Particle(np.array([2]),np.array([-1]))
    ball2.mass = 100**n

    """{'mass': 1, 'velocity' : 0, 'collisionNum' : 0}
    ball2 = {'mass': 100**n, 'velocity' : -1, 'collisionNum' : 0}
    """
    return [ball1, ball2]

"""defining the wall"""
wall = Wall(np.array([0]), np.array([1]))

def collision_type(ball1, ball2):
    """this determines the type of collision or breaks the cycle"""
    
    if (ball1.velocity < 0):
        return 'wall'
    elif (ball1.velocity>ball2.velocity):
        return 'elastic'
    else:
        return 'done'

def pi_calculation(n):
    """This should calculate pi to n digits"""
    
    #Setting up the system
    [ball1, ball2] = get_balls(n)
    collisionNum = 0
    
    for i in range(0,1000):
        if (collision_type(ball1, ball2) == 'wall'):
            collisionNum += 1
            wall_collision(wall, ball1)
            #print(ball2['velocity'])
        elif (collision_type(ball1, ball2) == 'elastic'):
            collisionNum += 1
            one_dim_elastic_collision(ball1, ball2)
            #print('elastic')
        else:
            print(collisionNum, 'collisions!')
            print(ball1, ball2)
            break
    print(collisionNum)
"""
while (0==0):
    if((ball1['velocity']>ball2['velocity']) or (ball1['velocity']<0)):
        collision(ball1, ball2)
    else:
        print ('End of collisions!') 
        break
    
#print(ball1['velocity'])

print('total collisions =', ball1['collisionNum'])
"""
print(pi_calculation(1))