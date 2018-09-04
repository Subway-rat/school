# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:22:53 2018

@author: matsh
"""


for f in range(0,101,10):
    cup = (f-30)/2
    c = (5.0/9)*(f-32)
    print("{:^5} --> {:^5} ~ {:^5}".format(f,round(c,2),cup))