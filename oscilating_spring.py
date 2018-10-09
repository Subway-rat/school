# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:28:15 2018

@author: matsh_000
"""
import numpy as np
import math
import matplotlib.pyplot as plt

A = 0.3; k= 4; v = 0.15; m=9

'''
Oppgave a bruker t1_array og y1_array
oppgave b bruker t2_array og y2_array
'''

def oscMath(t,A,v,k,m):
    '''
    Tar inn en t verdi med konstanter A,v,k,m
    outputter y(t) for formel
    '''
    return A*math.exp(-v*t)*math.cos(math.sqrt(k/m)*t)

def oscNP(t,A,v,k,m):
    '''
    Tar inn en array t med konstanter A,v,k,m
    outputter array y(t) 
    '''
    return A*np.exp(-v*t)*np.cos(np.sqrt(k/m)*t)

t1_array = np.zeros(101)
y1_array = np.zeros(101)
dt = 25/100

for i in range(101):
    t1_array[i] = i*dt
    y1_array[i] = oscMath(t1_array[i],A,v,k,m)

t2_array = np.linspace(0,25,101)
y2_array = oscNP(t2_array,A,v,k,m)

plt.plot(t2_array,y2_array, label = 'oselering line')
plt.plot(t1_array,y1_array, label = 'oselering for')

plt.xlabel('time (s)')
plt.ylabel('height from 0 (m)')
plt.title('Height of ball')
plt.axis([0,25,-A,A]) #definerer aksene
plt.grid()
plt.legend() #I tilfelle man ikke kan se forskjell
plt.show()

"""
Terminal> python oscilating_spring.py
(output is a plot)
"""
