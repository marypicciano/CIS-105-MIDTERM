import random 

def guessing_game():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
if __name__ == "__main__":
    guessing_game()
