# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:38:49 2018

@author: Somesh
"""

#Example
#Input: n = 16
#Output: 7
#There are two multiples of 7 and/or 5 in {1, 2, .. 16}
#The multiples are 3, 5, 6, 9, 10, 12, 15

# python program to find count 
# of multiples of 3 and 5 in  
# {1, 2, 3, ..n} 
  
def countOfMultiples(n): 
    # Add multiples of 3 and 5. 
    # Since common multples are 
    # counted twice in n/3 + n/15, 
    # subtract common multiples 
    return (int(n/3) + int(n/5) - int(n/15)); 
  
  
# Driver program to test 
# take input from the user
limit = int(input("Enter a number to count multiples: "))
# above function 
print(countOfMultiples(limit)) 
