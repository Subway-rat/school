# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:38:39 2018
@author: matsh
"""

g = 9.81; v0 = 50; n = 5 #masse variabler
t0 = [x*(2*v0/(n*g)) for x in range(0,n+1)] #definerer t
y0 = [round((v0*i)-(0.5*g*i**2),2) for i in t0] #definerer y
ty2 = [[round(t,2),y] for t,y in zip(t0,y0)] #rader
ty1 = [t0,y0] #koloner

#print(ty1)

for x in range(len(ty1[0])):
    print("{:^10} --> {:^10}".format(round(ty1[0][x],2), ty1[1][x])) #printer ut kolonner

#print(ty2)
print("")

for x in ty2:
    print("{:^10} --> {:^10}".format(x[0], x[1])) #printer ut rader

#for z in ty1: #henter lister
#    for u in z:       
#        v = round(u,2) #runder tid med 2 desimaler
#        print("") #litt pusterom
#        print("{}: {}".format(v,u)) #printer lister med 2 desimaler

"""
>>> ball_table3.py
   0.0     -->    0.0    
   2.04    -->   81.55   
   4.08    -->   122.32  
   6.12    -->   122.32  
   8.15    -->   81.55   
  10.19    -->    0.0    

   0.0     -->    0.0    
   2.04    -->   81.55   
   4.08    -->   122.32  
   6.12    -->   122.32  
   8.15    -->   81.55   
  10.19    -->    0.0    
"""
