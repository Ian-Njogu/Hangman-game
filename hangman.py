import random

def hangman_game():
    words = ['python', 'master', 'coding', 'hangman', 'program']  # word list
    word = random.choice(words)
    word_display = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
