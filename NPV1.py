# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 02:46:42 2023

@author: Korisnik
"""
#Net Present Value calculation


I = (-10000)
CF=(10000,25000,30000,50000)
r= 0.07
npv = I + (CF[0]/((1+r)**1.0)) + (CF[1]/((1+r)**2.0)) + (CF[2]/((1+r)**3.0)) + (CF[3]/((1+r)**4.0)) 
print(npv)