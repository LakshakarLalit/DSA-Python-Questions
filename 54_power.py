# input 2 number as a and b and find the value a raised to the power of b

# Method 1

a = int(input("enter base (a): "))
b = int(input("enter Exponent(b): "))

ans = 1
for i in range(1, b+1):
    ans *= a
print(ans)