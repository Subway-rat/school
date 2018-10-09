# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:56:31 2018

@author: matsh_000
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,t = 0):
    '''
    tar array x og gir ut en bølge.
    '''
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

x_array = np.linspace(-4,4,1000)

plt.plot(x_array,f(x_array))
plt.show()
'''
trminal> plot_wavepacket.py
<plot>
'''