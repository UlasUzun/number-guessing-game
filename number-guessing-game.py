import random

print("Welcome to the Number Guessing Game. You have 5 chances to guess the number. Let's start!")

lower_bound = int(input("Please enter a lower bound: "))
higher_bound = int(input("Please enter a higher bound: "))

print(f"You have 7 chances to guess the number correctly between {lower_bound} and {higher_bound}. Starting right now...")

target_number = random.randint(lower_bound,higher_bound)

given_chances = 7
guess_counter = 0

while guess_counter < given_chances:

    while True:
        guess = int(input("Enter your guess: "))

        if lower_bound <= guess <= higher_bound:
            break

        else:
            print(f"Please enter a guess between {lower_bound} and {higher_bound}")

    guess_counter += 1

    if guess == target_number:
        print("Correct")
        break

    elif guess_counter >= given_chances and guess != target_number:
        print(f"You lost. The number was {target_number}. ")

    elif guess < target_number:
        print("Too low")

    elif guess > target_number:
        print("Too high")


