import random

while True: 

# Generate a random integer between 1 and 10
    random_number = random.randint(1, 10)
    print("I'm thinking of a number between 1-10!")

    guess = 0
    guess_counter = 0

    while guess != random_number:

        try:
            guess = int(input("What's your guess? "))

        except ValueError: #safetynet if the user inputs non-numeric character
            print("That's not a number bruh! Try again.")
            continue

        guess_counter+= 1

        if guess > random_number:
            print("It's lower!")

        elif guess < random_number:
            print("The number is higher!")

        else:
            word = "guess" if guess_counter == 1 else "guesses"
            print(f"You won in {guess_counter} {word}!")


    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
