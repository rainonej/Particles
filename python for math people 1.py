# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# print 'Hello World!'
print("Hello, World!")
a = 2+2
#print(a)

#print(type (False))

list = [0]
#list.append(1)
print(list)

for x in (1,2,3,4): 
	list.append(x)
 
print (list)

for x in ['b','c','d']: 
	list.append(x)
#print x
print (list)

list = range(0,5)
print (list[3])

import sympy

#from sympy import *

x = sympy.Symbol('x')
y = sympy.integrate(sympy.exp(x**2))
print (y)
from sympy import integrate as integrate

z = integrate(sympy.exp(x**2)+1)
print(z)

y = sympy.integrate(sympy.exp(x**2))
print (y)
x = 'hello'
print (x)
"""
def step(x):
    if (x<= 0):
        return 0
    else:
        return 1
"""
#clear (z)

#z='hello'
def upvalue(x):
    zz=100
    y = x+zz+2
    return y
global zz
zz=5
zz=55

import onefunction
from onefunction import *

#print (step(0))
#print(x)

list = [-1, -.5, 0, .5, 1]
for x in list:
    print(onefunction.step(x))
#print (x)
print(z)
print(step(3))

import matplotlib.pyplot as plt

x=list
y=[]
for i in range(0, len(x)):
    y.append(step(x[i]))
print (y)

plt.plot(x,y, label = "label")
plt.xlabel(r'$\pi$', fontsize = 18)
plt.ylabel("y-data")
plt.xticks(fontsize = 10)

x=list
y=[]
for i in range(0, len(x)):
    y.append(step(x[i])+1)
print (y)

plt.plot(x,y, label = "label2")

plt.legend(fontsize = 18, loc = 'upper right')

plt.savefig('firstpic.png')

#plt.xlabel("x-data2")
#plt.ylabel("y-data2")
