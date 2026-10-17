# Strong Number 

n = int(input("Enter a number : "))
copy = n
total = 0

while n>0:
    digit = n%10
    fact = 1

    for i in range(1, digit+1):
        fact = fact * i

    total = total+fact
    n = n // 10

if total == copy:
    print(f"{copy} is a Strong Number")
else:
    print(f"{copy} is NOT a Strong Number")
