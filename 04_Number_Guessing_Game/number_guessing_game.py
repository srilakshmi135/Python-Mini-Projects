import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)
            break
        elif guess < secret_number:
            print("Too Low! Try Again.")
        else:
            print("Too High! Try Again.")

    except ValueError:
        print("Please enter a valid number.")