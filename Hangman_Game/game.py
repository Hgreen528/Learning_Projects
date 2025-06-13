import random

some_words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

word_choices = some_words.split(' ')
word = word_choices[random.randint(0, len(word_choices)-1)]

print("Guess the word! HINT: word is a name of a fruit")
print("- "*len(word))

required_characters = set(word)

turn_limit = len(word)+2
turn = 1
while turn < turn_limit + 1 and required_characters:    
    guess = input(f"Turn #{turn}. Enter a letter to guess: ").lower()
    if len(guess) > 1 or not guess.isalpha():
        print("Only guess single letters!")
        continue

    if guess in required_characters:
        required_characters.remove(guess)
    
    to_print = ""
    for c in word:
        if c in required_characters:
            to_print += "-"
        else:
            to_print += c
        to_print += ' '
    print(to_print)

    turn += 1

if not required_characters:
    print("Congratulations, You won!")

elif turn >= turn_limit:
    print("You ran out of turns. Better luck next time.")
