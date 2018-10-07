# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:45:42 2018

@author: Somesh
"""
#sum of prime numbers from a given list of integers



# Python program to find sum of primes 
# in range from 1 to n. 
  
# Returns sum of primes in range from 
# 1 to n 
  
def sumOfPrimes(n): 
    # list to store prime numbers 
    prime = [True] * (n + 1) 
      
    # Create a boolean array "prime[0..n]"  and initialize all entries it as true. 
    # A value in prime[i] will finally be  false if i is Not a prime, else true. 
      
    p = 2
    while p * p <= n: 
        # If prime[p] is not changed, then 
        # it is a prime 
        if prime[p] == True: 
            # Update all multiples of p 
            i = p * 2
            while i <= n: 
                prime[i] = False
                i += p 
        p += 1    
           
    # Return sum of primes generated through 
    # Sieve. 
    sum = 0
    for i in range (2, n + 1): 
        if(prime[i]): 
            sum += i 
    return sum
  
# Driver code 
# take input from the user
limit = int(input("Enter a number: "))
print (sumOfPrimes(limit)) 