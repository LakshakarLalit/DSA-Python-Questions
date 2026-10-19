# Right Triangle Number Pattern

n = int(input("Enter a number to print Number Triangle: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()