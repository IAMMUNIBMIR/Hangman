import random
from Hangmanwords import words
from HangmanVisuals import lives_visual_dict
import string


print("Welcome to Hangman")

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    Alphabet = set(string.ascii_uppercase)

    Lives = 7

    while Lives > 0 and len(word_letters) > 0:

        print('You have', Lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[Lives])
        print('Current word: ', ' '.join(word_list))

        guessed_letter = input("Pls enter a letter").upper()

        if guessed_letter in Alphabet - used_letters:
            used_letters.add(guessed_letter)
            
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print('')
            
            else:
                Lives = Lives - 1 
                print('\nYour letter,', guessed_letter, 'is not in the word.')

        elif guessed_letter == used_letters:
            print("Please enter a different letter you have already entered this letter once.")

        else:
            print("Please enter a valid letter.")

    if Lives == 0:
        print('You died, sorry. The word was', word)
        print(lives_visual_dict[Lives])

    if word_letters == 0:
        print("YAYY you have won the game. You guessed the word")



if __name__ == "__main__":
    hangman()

