import random

words = ["python", "developer", "computer", "algorithm", "keyboard"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print(f"\nWord: {display_word}")
    print(f"Attempts left: {attempts}")
    
    if "_" not in display_word:
        print("Congratulations! You won!")
        break
        
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print(f"Good job! {guess} is in the word.")
        guessed_letters.append(guess)
    else:
        print(f"Sorry, {guess} is not in the word.")
        attempts -= 1
        guessed_letters.append(guess)
        
if attempts == 0:
    print(f"\nGame Over! The word was: {word}")