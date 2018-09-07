# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:49:01 2018

@author: matsh
"""

s = 0;k = 1;M = 100 #definerer variabler, M er øvre grense
while k<(M+1): 
    s += float(1/k) # summerer
    k += 1.0 # går viderer til neste tall
print (round(s,9))

"""
>>> sum_while.py
5.187377518
"""
