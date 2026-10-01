marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 70 and marks < 90:
    print("Grade B")
elif marks >= 50 and marks < 70:
    print("Grade C")
else:
    print("Fail")