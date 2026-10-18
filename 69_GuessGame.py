# Guess the Number Game

import random
number = random.randint(1, 100)
guess = 0
attempts = 0

print(f"Welcome the Guess Game.")
print(f"Guess a Number between 1 to 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts +=1

    if guess < number:
        print("Too Low, Try Again!")
    elif guess > number:
        print("Too High, Try Again")
    else:
        print("Congratulation, You Guess The Right Number.")
        print(f"Number of Attempts: {attempts}")