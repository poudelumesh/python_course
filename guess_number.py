import random

number = random.randint(0, 100)
while True:
    guess = int(input("Guess a number (0-100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break