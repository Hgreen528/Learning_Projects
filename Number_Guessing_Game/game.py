import random

def generate_number(low, high):
    return random.randint(low, high)

low_bound = 1
high_bound = 100
number = generate_number(low_bound, high_bound)

print("Welcome to the guessing game. You have 7 chances to guess the number.")
print(f"I am thinking of a number between {low_bound} and {high_bound}")

guess = 0
guess_count = 1
while guess != number and guess_count <= 7:
    guess = input(f"Guess #{guess_count}. Guess a number: ")
    try:
        guess = int(guess)
    except:
        print("Only guess numbers!")
        continue

    guess_count += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You got it!")
        break
