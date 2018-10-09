# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:48:33 2018

@author: matsh_000
"""

import numpy as np
import matplotlib.pyplot as plt

f_array = np.linspace(-20,120,10)#interval
c_ish_array = (f_array-30)/2.0 #funksjon
c_array = (f_array-32)*5.0/9#funksjon
plt.plot(f_array,c_ish_array, label = 'c-ish')
plt.plot(f_array,c_array, label = 'c')
plt.legend()
plt.show()
'''
terminal> f2c_shortcut_plot.py
<plot>
'''