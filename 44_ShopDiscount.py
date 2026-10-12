# Shop Discount

amount = float(input("Enter the amount: "))

if amount < 5000:
    discount = amount * 0.10
elif amount>=5000 and amount < 9000:
    discount = amount * 0.15
elif amount>=9000:
    discount = amount * 0.20
else:
    discount = 0

final_amount = amount - discount
print(f"Your amount is: {amount}")
print(f"Discount: {discount}")
print(f"Final amount after discount: {final_amount}")