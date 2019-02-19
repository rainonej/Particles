# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:45:13 2019

@author: Jordan
"""

"""Reading and Writting Data"""

import numpy as np

f = open("sample.txt", "w")

my_array = np.zeros(6)

ar = np.array(6)

#np.array takes in lists, sets, etc... and converts it to an array


x = ['a', 'b', 'c']
y = np.array(x)
z = np.array('hello')

zeros = np.zeros((2,3))
#zeros = np.zeros((2,3), dtype=int)
#np.size and np.shape tells you the size and shape of your array in two different ways

for i in range(0,np.size(zeros, 0)):
    for j in range(0, np.size(zeros, 1)):
        zeros[i][j] = i + j
        
np.savetxt(f, zeros)

#test_data=np.loadtxt(f)


f.close()

