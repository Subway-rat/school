from math import *

def N(t,k,B,C): #lager definisjon for funksjon
    del1 = B #deler opp fuksjon (øvre)
    del2 = (1+C*exp(-k*t)) #deler opp fuksjon (nedre)
    funk = del1/del2 #setter sammen
    return funk

def test_N():
    t=0;C=9;k=0.2;B=50000 #test variabler
    expected = 5000 #forvented
    computed = N(t,k,B,C) 
    tol = 1e-14 #toleranse
    test = abs(expected - computed) < tol #tester
    assert test
test_N() #tester
'''
python pop_func.py
'''
