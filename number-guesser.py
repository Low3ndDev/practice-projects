import random

while True: 

    lives = 5

    random_number = random.randint(1, 10)
    print (f"I'm thinking of a number between 1-10! You only have {lives} attempts to win!")

    guess = 0
    guess_counter = 0

    while guess != random_number and lives > 0:
        try:
            guess = int(input("What's your guess? "))
        except ValueError: #safetynet if the user inputs non-numeric character
            print("That's not a number bruh! Try again.")
            continue

        guess_counter+= 1

        if guess > random_number:
            print("It's lower!")
            lives -= 1
            print(f"Lives remaining: {lives}")

        elif guess < random_number:
            print("The number is higher!")
            lives -= 1
            print(f"Lives remaining: {lives}")

        else:
            word = "guess" if guess_counter == 1 else "guesses"
            print(f"You won in {guess_counter} {word}!")

    if guess != random_number:
        print(f"Game Over! The number was {random_number}.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break