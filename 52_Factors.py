# Print all the Factors of the number

n = int(input("Enter a number to find factors: "))

print("The Factors is: ")
i = 1
while i<=n:
    if n%i == 0:
        print(i)
    i += 1