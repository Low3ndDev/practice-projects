import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print("I'm thinking of a number between 1-10!")
guess = 0

while guess != random_number:

    try:
        guess = int(input("What's your guess? "))

    except ValueError:
        print("That's not a number bruh! Try again.")
        continue

    if guess > random_number:
        print("Lower!")

    elif guess < random_number:
        print("higher")

    else:
        print("You won!")