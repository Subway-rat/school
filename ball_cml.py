# -*- coding: utf-8 -*-
import sys #inporterer modul
v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2]) #Sette variabler
y = v0*t - 0.5*g*t**2 #lager formel
print(y)
'''
python ball_cml.py 50 6
123.42
'''
