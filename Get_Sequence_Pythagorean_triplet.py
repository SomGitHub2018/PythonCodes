#print all Pythagorean triplet where h <=100
# to take input from the user
max_h= int(input("Enter a number: "))

list_triplets = [(i,j,k)for i in range(1,max_h+1) for j in range(i+1,max_h+1) for k in range(j+1,max_h+1) if(i**2 + j**2 == k**2)]
print("Triplets = %s" %list_triplets)
