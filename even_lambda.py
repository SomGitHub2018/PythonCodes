# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:16:40 2018

@author: Somesh
"""

# to take input from the user
lower= int(input("Enter a lower range: "))
upper= int(input("Enter a number range: "))

even_number= filter(lambda k: k%2==0, range(lower,upper+1))
for i in even_number:
    print(i)