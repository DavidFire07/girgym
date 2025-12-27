import random as r

with open("obesenec.txt", "r") as file:
    words = file.readlines()

guessing_word = r.choice(words).strip()
coverd_word = ["." for i in range(len(guessing_word))]
tried_letters = set()
wrong_attempts = 0

print("Guess the word!")

while True:
    
    print("".join(coverd_word))

    letter = input("Enter a char: ")
    if letter in guessing_word:
        print("Correct guess")
        tried_letters.add(letter)
    else:
        print("Incorrect guess")
        wrong_attempts += 1
    
    for letter1 in tried_letters:
        if letter1 in guessing_word and letter1 not in coverd_word:
            for i, letter2 in enumerate(guessing_word):
                if letter1 == letter2:
                    coverd_word[i] = letter1

    if "".join(coverd_word) == guessing_word:
        print("You won the game")
        break

    if wrong_attempts == 10:
        print("You lost the game")
        break