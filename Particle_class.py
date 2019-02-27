# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:17:35 2019

@author: Jordan
"""
import numpy as np


class Particle:
    "the particle class"
    
    def __init__(self, position, velocity):
        '''the essentials are Position and Velocity'''
        self.position = position
        self.velocity = velocity
        
        '''these are the non-essential things'''
        self.shape = "point"
        self.radius = 0
        self.angular_velocity = 0
        self.mass = 1
        self.density = 0
        self.dim = len(self.position)
        
    def dic(self):
        "This goes from the class to the dictionary"
        dic = {}
        dic['position'] = self.position
        dic['velocity'] = self.velocity
        dic['shape'] = self.shape
        dic['radius'] = self.radius
        dic['mass'] = self.mass
        dic['density'] = self.density
        dic['angular_velocity'] = self.angular_velocity
        
        
        return dic
    
    def __str__(self):
        return(str(self.dic()))
        
    def test(self):
        "this tests to make sure everything is in the correct format before things break"
        if (type(self.position) != np.ndarray):
            print('position is not an array')        
        if (type(self.velocity) != np.ndarray):
            print('velocity is not an array')
        if (len(self.position) != len(self.velocity)):
            print('Position and velocity dimensions not the same')
        
    def update_momentum(self):
        self.momentum = self.mass * self.velocity
    
    def update_energy(self):
        self.energy = .5* self.mass * np.linalg.norm(self.velocity)**2

