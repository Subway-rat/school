# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:22:53 2018

@author: matshol
"""
maks_temp = 100 #definerer variabler
min_temp = 0 #ikke nødvendig med greit å ha.
intervall = 10 #også ikke nødvendig men greit å ha
print("{:^5}--> {:^5} ~ {:^5}".format("c","f","approximately f")) #definerer koloner
for f in range(min_temp,maks_temp+1,intervall): #lager en for løkke
    c_n = (f-30)/2 #tilnærmet formel
    c = (5.0/9)*(f-32) #presis formel
    print("{:^5}--> {:^5} ~ {:^5}".format(f,round(c,2),c_n)) #printer liste
'''
python f2c_approx_table.py
  c  -->   f   ~ approximately f
  0  --> -17.78 ~ -15.0
 10  --> -12.22 ~ -10.0
 20  --> -6.67 ~ -5.0 
 30  --> -1.11 ~  0.0 
 40  --> 4.44  ~  5.0 
 50  --> 10.0  ~ 10.0 
 60  --> 15.56 ~ 15.0 
 70  --> 21.11 ~ 20.0 
 80  --> 26.67 ~ 25.0 
 90  --> 32.22 ~ 30.0 
 100 --> 37.78 ~ 35.0 
 
'''