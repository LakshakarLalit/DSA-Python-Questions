# Automorphic method 2

num = int(input("Enter a number: "))
square= num*num
digit = len(str(num))

lastDigit = square % (10 ** digit)

if lastDigit == num:
    print(f"{num} is an Automorphic Number")
else:
    print(f"{num} is not an Automorphic Number")