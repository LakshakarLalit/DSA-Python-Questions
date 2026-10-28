# Reverse an array without using extra Sapce

arr = [1,2,3,4,5,6]

n = len(arr)

for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

print("Reverse array without extra space: ", arr)