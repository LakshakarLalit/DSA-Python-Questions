# Find second max value in array

arr = [2, 96, 69, 77, 145, 20]
maxValue = arr[0]
secondMax = float('-inf')

for num in arr:
    if num > maxValue:
        secondMax = maxValue
        maxValue = num
    elif num > secondMax and num != maxValue:
        secondMax = num

print(f"Second Greatest Element = {secondMax}")