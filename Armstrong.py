# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:48:37 2018

@author: Somesh
"""

# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num," is an Armstrong number")
else:
   print(num," is not an Armstrong number")