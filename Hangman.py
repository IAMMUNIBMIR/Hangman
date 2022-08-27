import random
from Hangmanwords import words
from HangmanVisuals import lives_visual_dict
import string
Lives = 7

print("Welcome to Hangman")

def get_valid_word(words):
    word = random.choices(words)
    while '-' or ' ' in word:
        word = random.choices(words)
    return word.Upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    wrong_letters = []
    used_letters = []
    guessed_word = []
    Alphabet = [string.ascii_uppercase]
    while Lives != 0 and word_letters != 0:

        print("You have {} left and you have used these letters till now {}".format(Lives,used_letters))
        print(lives_visual_dict[Lives])
        print('Current word: {}'.format(guessed_word))

        guessed_letter = input("Pls enter a letter").upper()

        if guessed_letter == word_letters:
            word_letters.remove(guessed_letter)
            used_letters.append(guessed_letter)

        if guessed_letter != word_letters and used_letters:
            wrong_letters.append(guessed_letter)
            used_letters.append(guessed_letter)
            Lives -= 1

        if guessed_letter == used_letters:
            print("Please enter a different letter you have already entered this letter once.")

        else:
            print("Please enter a valid letter.")

    if Lives == 0:
        print("You have lost the game.")

    if word_letters == 0:
        print("YAYY you have won the game. You guessed the word")



if __name__ == "__main__":
    get_valid_word(words)
    hangman()
