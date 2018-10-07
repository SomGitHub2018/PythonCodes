# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:41:38 2018

@author: Somesh
"""

# Program to add natural numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
n = int(input("Enter numbers to be added : "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum natural number ",n,"is ", sum)