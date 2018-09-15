# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:21:01 2018

@author: matsh_000
"""
from random import random
antfeil = 0; N = 100000 #Setter variabler
for i in range(N):
    x = random(); y = random(); z = random() #Henter ut tilfeldige tall mellom 0 og 1
    res1 = x*y+x*z #første utregning
    res2 = x*(y+z) #andre utregning
    if res1 != res2: #ser om det er feil
        antfeil += 1 #teller feil
        x0 = x; y0 = y; z0 = z #lagrer hvilke tall det var
        ikkeass1 = res1 #lagrer siste resultat
        ikkeass2 = res2
print (100. * antfeil/N) #viser prosent feil
print (x0, y0, z0, ikkeass1 - ikkeass2) 
#Viser det siste resultatet i løkken med differansen av funksjonene
