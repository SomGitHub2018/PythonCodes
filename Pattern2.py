# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:07:28 2018

@author: Somesh
"""

# Python program to make a pattern as bellow
#0 
#1 0 
#0 1 0 
#1 0 1 0 
#0 1 0 1 0

# Function to demonstrate printing pattern of numbers 
def contnum(n): 
      
    # initializing starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # re assigning num 
        num = i % 2
        if num == 0:
            num = 0
        else:
            num = 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            if num == 0:
                num = 1
            else:
                num = 0
          
        # ending line after each row 
        print("\r") 
  
# take input from the user
n = int(input("Enter a number: "))


# sending 5 as argument 
# calling Function 
contnum(n) 
