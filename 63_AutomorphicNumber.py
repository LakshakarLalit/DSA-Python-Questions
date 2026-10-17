# Automorphic Number 

n = int(input("Enter a Number : "))
square = n*n

if str(square).endswith((str(n))):
    print("Automorphic Number.")
else: 
    print("Not an Automorphic Number.")