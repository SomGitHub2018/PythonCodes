# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:07:38 2018

@author: Somesh
"""
# Python program to find the factorial of a number provided by the user.

# to take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of ",num," is ",factorial)