"""
output expected for factorial(5)
					factorial 5 
				factorial 4 
			factorial 3 
		factorial 2 
	factorial 1 
factorial 0 
returning 1 
	returning 1 
		returning 2 
			returning 6 
				returning 24 
					returning 120
120
"""

def factorial(n): 
    space = ' ' * (4 * n) 
    print (space, 'factorial', n)
    if n == 0: 
        print (space, 'returning 1')
        return 1 
    else: 
        recurse = factorial(n-1) 
        result = n * recurse 
        print (space, 'returning', result)
        return result 
print(factorial(5))
