# Array left rotaion by 1

arr = [1,2,3,4,5]

one = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[-1] = one

print("After left rotation by 1: ", arr)