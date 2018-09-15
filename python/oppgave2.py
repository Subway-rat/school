# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:56:20 2018

@author: matsh_000
"""
from math import factorial
def u(n,i): #funksjon
    pro = 1.0
    for s in range(1,((n-i)+1)):
        pro = float(pro*((s+i)/s))
    return pro
def fac(n,i):
    del1 = factorial(n)
    del2 = factorial(n-i)*factorial(i)
    pro = (del1/del2)
    return pro
def v(n,i):
    pro = 1.0
    for s in range(1,((n-i)+1)):
        pro = float(pro*(((i+1)*(s))/(s-i)))
    return pro
x =[[5000,4],[100000,60],[1000,500]]
for z in x:
    diff = abs(u(z[0],z[1])-fac(z[0],z[1]))
    print(v(5000,4))
    print(diff)
#def test_u(): #test funksjon
#    x =[[5000,4],[100000,60],[1000,500]]
#    expected = [26010428123751, (round((1.18069197996257*10**218))), (round((2.702882409454366*10**299)))]
#    computed = [u(x[0][0],x[0][1]),u(x[1][0],x[1][1]),u(x[2][0],x[2][1])]
#    tol = 1E-16
#    for t in zip(computed,expected):
#        test = abs(t[0]-t[1]) <= tol
#        assert test, t
#test_u()