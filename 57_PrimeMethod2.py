# Check number is Prime or not

# Method 2

import math

n = int(input("Enter a number : "))

if n <= 1:
    print("Number is not Prime")
elif n == 2:
    print("Number is prime")
elif n % 2 == 0:
    print("Number is not prime")
else:
    isPrime = True
    for i in range (3, int(math.sqrt(n)) +1, 2):
        if n%i==0:
            isPrime = False
            break

    if isPrime:
        print("Number is Prime")
    else:
        print("Number is not Prime")