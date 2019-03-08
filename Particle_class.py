# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:17:35 2019

@author: Jordan
"""
import numpy as np


class Particle:
    "the particle class"

    class_attribute = "nice"
    
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

        #Run a test to make sure the particle is defined properly
        self.test()
        
    def dic(self):
        "This returns the object as a dictionary"
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

    def change(self):
    	self.class_attribute = "hello"

class SphericalParticle(Particle):
	"testing subclasses"
	def change(self):
		self.class_attribute = "goodbye"

	def __init__(self, position, velocity, radius):
		super().__init__(position, velocity)
		self.radius = radius
		#this seems to override the previous __init__. Can I just add something to the __inti__?

class Wall:
	"A class to define a wall"
	def __init__(self, position, normal):
		"Assumed to be a hyper plane where position is any element of the hyperplane."
		self.position = position
		self.normal = normal

		self.dim = len(self.normal)

		#Run a test to make sure everything is defined properly
		self.test()

	def test(self):
		"this is to make sure the wall is defined properly"
		if(np.linalg.norm(self.normal) != 1):
			print('the normal vector to the wall is not unit length')
		if (len(self.position) != len(self.normal)):
			print('Position and normal vectors are not the same dimension')

	def dic(self):
		"This returns the object as a dictionary"
		dic = {}
		dic['position'] = self.position
		dic['normal'] = self.normal

		return dic
	
	def __str__(self):
		return(str(self.dic()))






def wall_collision(wall, particle):
	'A simple function which reflects a particle against a wall'
	particle.velocity -= 2*np.dot(particle.velocity, wall.normal)*wall.normal



