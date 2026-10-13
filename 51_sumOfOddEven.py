# Accept the number and find a odd and even and also calculate the sum of Odd and Even numbers

n = int(input("Enter a number: "))

EvenSum = 0
OddSum = 0

for i in range(1, n+1):
    if i%2==0:
        EvenSum += i
    else:
        OddSum += i

print("Sum of Even numbers is : ",EvenSum)
print("Sum of Odd numbers is : ",OddSum)