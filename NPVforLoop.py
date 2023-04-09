# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:55:36 2023

@author: Korisnik
"""

IO = -500
CF1 = 100
CF2 = 140
CF3 = 170
CF4 = 130
CF5 = 100


CF = [IO,CF1,CF2,CF3,CF4,CF5]
r = 0.07


NPV = 0
for i in range (len(CF)):
   NPV += CF[i] / (1+r)**i
print(round(NPV,3))