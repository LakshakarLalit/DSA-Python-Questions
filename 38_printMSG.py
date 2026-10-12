# Enter your gender and print a message

gender = input("Enter your gender f,F, m,M: ")

if gender == 'f' or gender == 'F':
    print("Good morning ma'am")
elif gender == 'm' or gender == 'M':
    print("Good morning sir")
else:
    print("Invalid input")