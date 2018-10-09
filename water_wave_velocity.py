# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:07:12 2018

@author: matsh_000
"""

import numpy as np
import matplotlib.pyplot as plt

def wave(Lamda,s = 7.9*10**(-2),p = 1000,h = 50, g = 9.81):
    '''
    tar inn et interval Lamda og gir ut funksjons verdien.
    '''
    return np.sqrt((g*Lamda/(2*np.pi))*(1+(s*4*(np.pi**2)/(p*g*Lamda)))*np.tanh(2*np.pi*h/Lamda))

Lamda1 = np.linspace(0.001,0.1,10000)
Lamda2 = np.linspace(1,2000,10000)
plt.subplot(1,2,1)
plt.plot(Lamda1, wave(Lamda1), label = 'small interval')
plt.legend()
plt.subplot(1,2,2)
plt.plot(Lamda2, wave(Lamda2), label = 'Big interval')
plt.legend()
plt.show()

'''
terminal> water_wave_velocity.py
<plot>
'''