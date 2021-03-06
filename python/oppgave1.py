# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:52:22 2018

@author: matsh_000
"""
from math import sqrt

x1 = [1.0,(1-sqrt(2))] #lager liste med start tall
x2 = [] # vi genererer tall fra starten

def f1(x0,x1): #lager en definisjon
    x3 = 2*x1+x0 #formel for neste tall i følgen
    return x3

def f2(n): #analysert løsning
    x3 = (1-sqrt(2))**n
    return x3

for i in range(0,101): #lager en rekke med n ledd
    x1.append(f1(x1[i],x1[i+1])) #legger til liste
    x2.append(f2(i))

for z in zip(x1,x2,range(0,101)):
    tol = abs(z[0]-z[1]) #finner differansen
    print('{:^10} --> {:<22}'.format(z[2],tol)) #lager liste med differanse

'''
python oppgave1.py
    0      --> 0.0                   
    1      --> 0.0                   
    2      --> 2.7755575615628914e-16
    3      --> 4.3021142204224816e-16
    4      --> 1.186550857568136e-15 
    5      --> 2.789435349370706e-15 
    6      --> 6.774095173689432e-15 
    7      --> 1.6334156249797616e-14
    8      --> 3.944414239676064e-14 
    9      --> 9.522206157255853e-14 
    10     --> 2.2988859080252944e-13
    11     --> 5.549991483099273e-13 
    12     --> 1.3398869246918337e-12
    13     --> 3.2347729841410676e-12
    14     --> 7.8094328989032e-12   
    15     --> 1.885363877813582e-11 
    16     --> 4.5516710456445386e-11
    17     --> 1.098870596904972e-10 
    18     --> 2.6529082983765153e-10
    19     --> 6.404687193657275e-10 
    20     --> 1.5462282685691429e-09
    21     --> 3.732925256504003e-09 
    22     --> 9.012078781577156e-09 
    23     --> 2.1757082819658312e-08
    24     --> 5.2526244420893783e-08
    25     --> 1.2680957166144587e-07
    26     --> 3.0614538774378553e-07
    27     --> 7.39100347149017e-07  
    28     --> 1.7843460820418194e-06
    29     --> 4.307792511232656e-06 
    30     --> 1.0399931104507132e-05
    31     --> 2.510765472024692e-05 
    32     --> 6.0615240545000966e-05
    33     --> 0.00014633813581024885
    34     --> 0.0003532915121654987 
    35     --> 0.0008529211601412463 
    36     --> 0.002059133832447991  
    37     --> 0.004971188825037228  
    38     --> 0.012001511482522449  
    39     --> 0.028974211790082124  
    40     --> 0.0699499350626867    
    41     --> 0.16887408191545553   
    42     --> 0.40769809889359776   
    43     --> 0.984270279702651     
    44     --> 2.3762386582988997    
    45     --> 5.73674759630045      
    46     --> 13.8497338508998      
    47     --> 33.43621529810005     
    48     --> 80.7221644470999      
    49     --> 194.88054419229985    
    50     --> 470.4832528316996     
    51     --> 1135.847049855699     
    52     --> 2742.1773525430976    
    53     --> 6620.201754941894     
    54     --> 15982.580862426887    
    55     --> 38585.36347979567     
    56     --> 93153.30782201822     
    57     --> 224891.9791238321     
    58     --> 542937.2660696824     
    59     --> 1310766.511263197     
    60     --> 3164470.2885960764    
    61     --> 7639707.08845535      
    62     --> 18443884.465506777    
    63     --> 44527476.0194689      
    64     --> 107498836.50444458    
    65     --> 259525149.02835807    
    66     --> 626549134.5611607     
    67     --> 1512623418.1506793    
    68     --> 3651795970.8625193    
    69     --> 8816215359.875717     
    70     --> 21284226690.613953    
    71     --> 51384668741.10362     
    72     --> 124053564172.8212     
    73     --> 299491797086.74603    
    74     --> 723037158346.3132     
    75     --> 1745566113779.3726    
    76     --> 4214169385905.0586    
    77     --> 10173904885589.49     
    78     --> 24561979157084.04     
    79     --> 59297863199757.57     
    80     --> 143157705556599.2     
    81     --> 345613274312955.94    
    82     --> 834384254182511.0     
    83     --> 2014381782677978.0    
    84     --> 4863147819538467.0    
    85     --> 1.1740677421754912e+16
    86     --> 2.8344502663048292e+16
    87     --> 6.8429682747851496e+16
    88     --> 1.652038681587513e+17 
    89     --> 3.988374190653541e+17 
    90     --> 9.628787062894595e+17 
    91     --> 2.324594831644273e+18 
    92     --> 5.612068369578006e+18 
    93     --> 1.3548731570800284e+19
    94     --> 3.270953151117857e+19 
    95     --> 7.896779459315743e+19 
    96     --> 1.9064512069749342e+20
    97     --> 4.6025803598814426e+20
    98     --> 1.111161192673782e+21 
    99     --> 2.682580421335708e+21 
   100     --> 6.476322035345199e+21 
'''