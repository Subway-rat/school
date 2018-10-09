# -*- coding: utf-8 -*-
from math import sqrt #importerer moduler
a = float(input('a? ')); b = float(input('b?')); c= float(input('c?')) #setter verdier

def solve3(a,b,c): #lager definisjon
    res = [] #lager liste
    del11 = -b-sqrt(b**2-4*a*c) #delformel 1
    del12 = -b+sqrt(b**2-4*a*c) #delformel 2
    del2 = 2*a
    res.append(del11/del2) #legger til liste
    res.append(del12/del2)
    return res #returnerer liste

print('løsninger: {} , {}'.format(solve3(a,b,c)[0],solve3(a,b,c)[1]))#printer ut det vil vil ha

'''
python quadratic_roots_input.py

a? 1

b?2

c?1
løsninger: -1.0 , -1.0
'''
