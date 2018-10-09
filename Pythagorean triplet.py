# Check the enter 3 numbers are Pythagorean triplets are not.
#nums = [3,4,5] working
# to take input from the user
a= int(input("Enter a number a: "))
b= int(input("Enter a number b: "))
c= int(input("Enter a number c: "))

nums = [a,b,c]
h = max(nums)
nums.remove(h)
squares=[i ** 2 for i in nums]
others_squares =sum(squares)
if (h ** 2 == others_squares):
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")
