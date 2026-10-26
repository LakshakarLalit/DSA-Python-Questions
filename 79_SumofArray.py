# Sum of array and average

n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    num = int(input("Enter an element: "))
    arr.append(num)

total = sum(arr)
average = total / n

print("Array:", arr)
print("Sum =", total)
print("Average =", average)