# Enter an n and print numbers from n to 1

n = int(input("Enter a positive integer n: "))

for i in range(n, 0, -1):
    print(i, end=' ')