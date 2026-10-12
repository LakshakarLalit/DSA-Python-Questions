# Enter your name and age and find you are eligible for voting or not

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, You are a valid voter.")
else:
    print(f"Hello {name}, You cannot cast the vote.")
    print(f"You will be eligible for voting after {18 - age} years.")