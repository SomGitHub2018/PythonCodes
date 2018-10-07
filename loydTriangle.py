# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:51:53 2018

@author: Somesh
"""

# Python program to make a pattern as loydTriangle
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15


# Function to demonstrate printing pattern of numbers 
def loydTriangle(n): 
      
    # initializing starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # not re assigning num 
        # num = 1 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num = num + 1
      
        # ending line after each row 
        print("\r") 
  
# take input from the user
n = int(input("Enter a number: "))


# sending 5 as argument 
# calling Function 
loydTriangle(n) 
