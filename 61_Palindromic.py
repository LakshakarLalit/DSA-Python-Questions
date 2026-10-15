# Palindromic number 

n = int(input("Enter a number : "))
copy = n
opp = 0

while n>0:
    num = n%10
    opp = opp *10 + num
    n = n//10

if copy == opp:
    print("Number is Palindromic")
else:
    print("Number is not Palindromic")