# -*- coding: utf-8 -*-
try: #vi prøver oss frem
    import sys
    v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2]) #spør om input
    y = v0*t - 0.5*g*t**2 #formel
    print(y)
except: #hvis det ikke virker
    v0 = float(input('v0=? ')); g = 9.81; t = float(input('t=? ')) #spør om input
    y = v0*t - 0.5*g*t**2 #formel
    print(y)
'''
python ball_cml_qa.py 50 6
123.42
python ball_cml_qa.py
v0=? 50
t=? 6
123.42
'''
