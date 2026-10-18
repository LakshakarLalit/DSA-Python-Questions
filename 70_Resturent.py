# Resturent

total = 0

while True:
    print("\n--- Restaurant Menu ---")
    print("1. Pizza - ₹150")
    print("2. Burger - ₹80")
    print("3. Coffee - ₹50")
    print("4. Exit & Bill")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            total += 150
            print("Pizza added!")
        case 2:
            total += 80
            print("Burger added!")
        case 3:
            total += 50
            print("Coffee added!")
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")

print(f"Your total bill is: ₹{total}")