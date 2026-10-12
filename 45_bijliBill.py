# Bijli Bill System

units = int(input("Enter the number of units consumed: "))
bill = 0
if units <= 100:
    bill = units * 4
elif units <= 200:
    bill = (100 * 4) + (units - 100) * 6
elif units <= 400:
    bill = (100 * 4) + (100 * 6) + (units - 200) * 8
else:
    bill = (100 * 4) + (100 * 6) + (200 * 8) + (units - 400) * 12

print(f"Your total bill is: {bill}")