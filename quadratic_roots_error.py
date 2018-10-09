# -*- coding: utf-8 -*-
from math import sqrt #importerer moduler
import sys

def solve3(a,b,c): #definisjon på formel
    res = []
    del11 = -b-sqrt(b**2-4*a*c) #delformel
    del12 = -b+sqrt(b**2-4*a*c)
    del2 = 2*a
    res.append(del11/del2)
    res.append(del12/del2)
    return res #returnerer liste

try: #vi prøver oss frem
    a = float(sys.argv[1]); b = float(sys.argv[2]); c= float(sys.argv[3]) #setter variabler
    print('løsninger: {} , {}'.format(solve3(a,b,c)[0],solve3(a,b,c)[1]))
except IndexError: #hvis vi har glemt noe
    print('Du mangler noen argumenter.') #kommentar på at vi har glemt noe
'''
terminal>K:\IN1900\oppgaver\quadratic_roots_error2.py 1 2 1
l├©sninger: -1.0 , -1.0
'''