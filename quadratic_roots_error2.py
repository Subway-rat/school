# -*- coding: utf-8 -*-
from math import sqrt #Importerer moduler
import sys

def solve3(a,b,c): #formel for kvadratisk polynom
    res = []
    del11 = -b-sqrt(b**2-4*a*c)
    del12 = -b+sqrt(b**2-4*a*c)
    del2 = 2*a
    res.append(del11/del2)
    res.append(del12/del2)
    return res
try: #vi prøver
    a = float(sys.argv[1]); b = float(sys.argv[2]); c= float(sys.argv[3])
    print('løsninger: {} , {}'.format(solve3(a,b,c)[0],solve3(a,b,c)[1]))
except IndexError: #Hvis noe mangler
    print('Du mangle noe.')
except ValueError: #ugyldig verdi
    print('Ingen reell løsninger')
except TypeError: #ugyldig verdi
    print('Ingen løsninger, og tror det ikke er et tall du har skrevet')

'''
terminal>K:\IN1900\oppgaver\quadratic_roots_error2.py 1 0 -9
l├©sninger: -3.0 , 3.0
'''
