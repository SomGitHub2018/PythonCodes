# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:56:09 2018

@author: Somesh
"""

# Python program to make a pattern as bellow
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 

# Function to demonstrate printing pattern triangle 
def triangle(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing according to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing according to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# take input from the user
n = int(input("Enter a number: "))


# sending 5 as argument 
# calling Function 
triangle(n) 
