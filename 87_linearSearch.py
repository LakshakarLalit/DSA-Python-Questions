# Linear Search

arr = [1,2,3,5,6,25,68,95,45,78,32]

target = 45
index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print("index: ", index)