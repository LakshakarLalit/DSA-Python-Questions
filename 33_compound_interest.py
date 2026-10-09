# Compound Interest Calculator

import math
p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time in years: "))

CI = p * math.pow((1 + r / 100), t) - p
print(f"The compound interest after {t} years is: {CI:.2f}")