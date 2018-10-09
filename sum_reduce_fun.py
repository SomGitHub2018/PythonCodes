# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:43:38 2018

@author: Somesh
"""
# to take input from the user
lower= int(input("Enter a lower range: "))
upper= int(input("Enter a number range: "))

import functools
sum_list = functools.reduce(lambda x,y: x+y, range(lower,upper+1))
print (sum_list)