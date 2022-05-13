import random
from words import word_list


# Selects word from word.py
def get_word(word_list):
    word = random.choice(word_list)
# Uppercase for terminal readability
    return word.upper()


# Displays word during the turn
def play(word):
    # Hidden guesses are displayed with _
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    # Amount of tries the user has, based on the original hangman body parts
    tries = 8
    print("Guess The Word To Win Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        # Prompts the user to start guessing
        guess = input("Guess a letter or word:\n ").upper()
        if len(guess) == 1 and guess.isalpha():
            # Displays if a letter is already guessed
            if guess in guessed_letters:
                print("You already guessed", guess,)
            # Displays if the letter guessed is not in the word a try is deducted as penalty
            elif guess not in word:
                print(guess, "isn't in the word")
                tries -= 1
                guessed_letters.append(guess)
            # Displays when the user has guessed a correcct letter, this letter will replace the _
            else:
                print("Got one!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # Displays when the user guesses a full word that they had previously guesed
            if guess in guessed_words:
                print("You already tried ", guess)
            # Displays when the user guesses an incorrect full word a try is deducted as penalty
            elif guess != word:
                print(guess, " is not the correct word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        print(word_completion)
        print("\n")
    # Displays when the user has indevidualy guessed the letters or the full word
    if guessed:
        print("Well Done, you guessed the word!")
    # Displays when the user has tried more than 8 times
    else:
        print("You ran out of tries. The word was " + word + ". Better luck next time")


# Propts the user to play again or quit
def main():
    word = get_word(word_list)
    play(word)
    while input("Want to play again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()
