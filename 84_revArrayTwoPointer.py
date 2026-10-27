# Reverse an array by two pointer approch

arr = [11,33,44,55,66,22,99]
left = 0
right = len(arr)-1

while left < right :
    arr[left] = arr[right]
    arr[right] = arr[left]

    left +=1
    right -=1
print("Reverse array: ", arr)