"""This is where I write most of the functions used to make particle 
collision happen"""

import numpy as np
import Particle_class 
from Particle_class import *

def wall_collision(wall, particle):
	'A simple function which reflects a particle against a wall'
	particle.velocity -= 2*np.dot(particle.velocity, wall.normal)*wall.normal


def one_dim_elastic_collision(particle1, particle2):
	'A simple, non-efficient 1-dim collision function'

	particle1.update_energy()
	particle2.update_energy()
	E = 2*particle1.energy + particle2.energy

	particle1.update_momentum()
	particle2.update_momentum()
	P = particle1.momentum + particle2.momentum

	v1 = particle1.velocity
	v2 = particle2.velocity

	m1 = particle1.mass
	m2 = particle2.mass


	"""Actual Code"""
	v2 = (m2*P+np.sqrt(m2**2 * P**2 - (m2**2+ m1 * m2)*(P**2 - E * m1)) ) / (m2**2 + m1* m2)
	v1 = (P - m2 * v2) / m1

	particle1.velocity = v1
	particle2.velocity = v2
