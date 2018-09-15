# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:12:25 2018

@author: matshol
"""
"""
s = 0; M = 3 #k er ikke definert
for i in range(M): #M går ikke hele veien til maks verdi
    s += 1/2*k**2  #det er ikke flyt tall, mangler parantes
print(s) 
"""
'''
Vi starter med å rette opp programmet.
'''
s = 0; M = 3; k = 1 #K er nå definert med resten av variablene
for i in range(M+1): #M+1 gjør at det går til M og ikke M-1
    s += 1.0/((2*k)**2) #Legger til paranteser for sikkerhet
print(s) #vi printer ut og håper på det beste
'''
Nå gjør vi om programet slik at den bruker en while loop.
'''
s = 0; M = 3; k = 1; i = 0 #legger til en variabel i for telling
while i <= M: #setter opp while loop
    s += 1.0/((2*k)**2) #bruker formel og legger til tidligere verdi
    i += 1 # legger til 1 i teller variabel.
print(s) 
'''
python sum_for.py
1.0
1.0

'''