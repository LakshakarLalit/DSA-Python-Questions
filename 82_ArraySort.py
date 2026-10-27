# Check if array is sorted in increasing order or not

arr = [1,2,3,4,5]

i = 0

while i<len(arr)-1:
    if arr[i] > arr[i+1]:
        print("Array not sorted")
        break
    i+=1
else:
    print("Array is sorted")