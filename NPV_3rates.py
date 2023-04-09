# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:01:46 2023

@author: Korisnik
"""

import numpy_financial as npf

values = [45, 50, 40, -100]
rate1 = 0.50
rate2 = 0.30
rate3 = 1
#Printing NPV Values
print("NPV value with rate ", rate1, " is: ", npf.npv(rate1, values))
print("NPV value with rate ", rate2, " is: ", npf.npv(rate2, values))
print("NPV value with rate ", rate3, " is: ", npf.npv(rate3, values))
