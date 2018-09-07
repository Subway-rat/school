# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:36:26 2018
@author: matsh
"""

v0 = 50 #meter per sekund
g = 9.81

t = [t for t in range(int(round((2*v0)/g))+1)] #tids intervall
y = [v0*t-0.5*g*t**2 for t in t] # formel 

for x in zip(t,y): #vever sammen listene
    print("{:^10} --> {:^10}".format(x[0], round(x[1],2)))

"""
>>>ball_table2.py
    0      -->    0.0    
    1      -->   45.09   
    2      -->   80.38   
    3      -->   105.85  
    4      -->   121.52  
    5      -->   127.38  
    6      -->   123.42  
    7      -->   109.66  
    8      -->   86.08   
    9      -->   52.69   
    10     -->    9.5    
"""
