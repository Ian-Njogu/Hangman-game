import random

def hangman_game():
    words = ['python', 'master', 'coding', 'hangman', 'program']  # word list
    word = random.choice(words)
    word_display = ['_'] * len(word)
    attempts = 6
    guessed_letters = set() #FOR INPUT VALIDATION 

    print("Welcome to the hangman game!!!\n Guess the words in less than 6 attempts")
    print("".join(word_display))

    while attempts >0 and '_' in word_display:
        guess = input("Enter a letter: ").lower()

        try:
            if len(guess) !=1 or not guess.alpha():
                raise ValueError("Please enter a single alphabetical letter")
            if guess in guessed_letters:
                raise ValueError("You've already entered that letter")
        except ValueError as ve:
            print(ve)

