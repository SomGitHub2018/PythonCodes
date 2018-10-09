# Check the enter 3 numbers are Pythagorean triplets are not.
#nums = [1,2,3]
nums = [4,5,3]
h = max(nums)
nums.remove(h)
squares=[i ** 2 for i in nums]
others_squares =sum(squares)
if (h ** 2 == others_squares):
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")
