# Find max value and index in the array

arr = [2, 96, 69, 77, 145, 20]

maxValue = arr[0]
index = 0

for i in range(1, len(arr)):
    if arr[i] > maxValue:
        maxValue = arr[i]
        index = i

print(f"Max element = {maxValue} found at index {index}")