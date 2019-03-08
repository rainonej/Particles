# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 00:26:53 2019

@author: Jordan
"""

import numpy as np

import Particle_class
from Particle_class import *

a = np.array([0,0,0.])
b = np.array([1,-1,0])
p = Particle(a, b)
w = Wall(np.array([0,0,0]), np.array([1,0,0]))


