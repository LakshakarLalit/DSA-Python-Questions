# take input and reverse the array

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter elements{i+1}: "))
    arr.append(num)

rev = []
for i in range(n-1, -1, -1):
    rev.append(arr[i])

print("Original Array: ", arr)
print(f"Reversed Array: {rev}")