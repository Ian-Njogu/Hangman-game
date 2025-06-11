import random

def hangman_game():
    words = ['python', 'master', 'coding', 'hangman', 'program']  # word list
    word = random.choice(words)
    word_display = ['_'] * len(word)
    attempts = 6
    guessed_letters = set() #FOR INPUT VALIDATION 

    print("Welcome to the hangman game!!!\n Guess the words in less than 6 attempts")
    print("".join(word_display))

    #While loop to keep the game running
    while attempts >0 and '_' in word_display:
        guess = input("Enter a letter: ").lower()
    #try block for input validation
        try:
            if len(guess) !=1 or not guess.alpha():
                raise ValueError("Please enter a single alphabetical letter")
            if guess in guessed_letters:
                raise ValueError("You've already entered that letter")
        except ValueError as ve:
            print(ve)
            continue

        guessed_letters.add(guess) 

        if guess in word:
            print("The letter is in the word")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] == guess
        else:
            attempts -= 1

            print(f"Wrong guess! The monster gets closer... {attempts} attempts left.")
            print("Word:", " ".join(word_display))
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        if '_' not in word_display:
            print("Congratulations! You escaped the monster. You WON!")
        else:
            print(f"The monster got you... The word was '{word}'. You LOST!")

hangman_game()