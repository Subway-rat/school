# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:33:39 2018

@author: matsh_000
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, T = 2*math.pi):
    '''
    Tar input t og gir en ny verdi y
    ut fra kriteriene under.
    '''
    if (0<t and t<(T/2.0)):
        t = 1
    elif (t == (T/2)):
        t = 0
    elif ((t>T/2.0) and t<T):
        t = -1
    else:
        t = 0
    return t
f = np.vectorize(f) #vektroiserer funksjonen f
def s(t,n, T = 2*np.pi):
    '''
    tar input t og gir en tilnærming s med nøyaktighet n
    '''
    S = 0.0
    for i in range(1, n+1):
        h1 = (2*(2*i-1)*np.pi*t)/T
        h2 = 1/(2*i-1)
        S = S + h2*np.sin(h1)
    S = S * (4/(np.pi))
    return S

n=100
T = 2*math.pi
x = np.linspace(0,T,n)
values = [1,3,20,200] #Bestemte verdier

for k in range(1,len(values)+1): #går igjennom verdiene
    fx = f(x)
    sx = s(x,values[k-1])
    plt.subplot(2,2,k) #lager en subplot for hver av de, ellers kan man kommentere ut denne linjen for å få alt i et.
    plt.plot(x,fx, label = 'funksjon')
    plt.plot(x,sx, label = 'tilnærmet')
    plt.legend()
plt.show()
'''
terminal> sinesum1_plot.py
<plot>
'''