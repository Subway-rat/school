from math import *

def rectify(x): #setter opp funksjonen
    if sin(x)>0: #siden linjen kan utrykkes sin(x) for vf > 0
        return sin(x)
    elif sin(x)<=0: #sin(x)=0 når vf er mindre enn 0
        return 0
    else:
        pass #hvis vi får noe rart

def test_rectify():
    x = (1,10,100,46,9) #lager test variabler
    expected = (sin(1),0,0,sin(46),sin(9)) #forventet
    computed = [rectify(i) for i in x] #lager liste
    tol = 1e-14 #setter toleranse
    for z in zip(expected,computed):
        test = abs(z[0] - z[1]) < tol #tester
        assert test
test_rectify()
'''
python half_wave.py
'''
