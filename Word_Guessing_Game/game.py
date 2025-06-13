import random

words = ["first", "strong", "computer", "test", "python", "player", "japan"]

word_choice_idx = random.randint(0, len(words)-1)
word_choice = words[word_choice_idx]

print("You have 12 guesses to guess all the letters in a randomly chose word.")
user_name = input("What is your name? ")
print(f"Good Luck! {user_name}")

required_letters = set(word_choice)
turn = 1
while required_letters and turn <= 12:
    guess = input(f"Turn #{turn}. Guess a letter: ").lower()
    if guess in required_letters:
        required_letters.remove(guess)
    for c in word_choice:
        print(c if c not in required_letters else '-')

    turn += 1

if turn == 13:
    print("You've run out of guesses. Better luck next time.")

elif not required_letters:
    print(f"Congratulations {user_name}, you win! The word is: {word_choice}")
