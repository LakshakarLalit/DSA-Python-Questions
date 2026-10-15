# Separate each digit of a number and print it on a new line

n = int(input("Enter a number: "))

while n>0:
    digit = n%10
    print(digit)
    n = n//10