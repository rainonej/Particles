# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:12:27 2019

@author: Jordan
"""
import numpy as np

import Particle_class
from Particle_class import *

a = np.array([0,0,0.])
b = np.array([1,-1,0])
c = Particle(a, b)

def random_step(particle):
    particle.position += 2*np.random.rand(particle.dim) - 1
    
position_history = []
for i in range(0,9):
    position_history.append(c.position.tolist())
    random_step(c)
    
np.array(position_history)
print(position_history)