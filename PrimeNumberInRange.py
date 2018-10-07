# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:07:38 2018

@author: Somesh
"""

# Python program to display all the prime numbers within an interval

# the following lines to take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between ",lower," and ",upper," are: ")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:    
           print(num)
