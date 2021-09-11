# Terminal Hangman
Termainal hangman is a Python language terminal game.

The users main goal is to guess the word either letter by letter or by guessing the full word before their maximum tries had run out.

## How to play
Termainal hangman is based on the classic pen and paper hangman game.

Like the original game the user must guess a word that the computer has randomly selected from the "words.py" list.

The unknown letters are displayed as _ but when the correct letter is guessed that letter will replace the _.

The user must guess the letter before their maximum turns runs out, the user will only win when the word is either guessed with individual letters or if the user guesses the full word.

## Features

1. **Randomisation**:
The computer has a set list of over 500 words and will pick out a word to be guessed at random.
2. **Hidden Words**:
Once a word is chosen the word will be hidden and replaced with a _ the amount of underscores represents the amount of letters in the word.
Once guessed the _ is replaced with the guessed letter.
3. **User Input**:
The user can input any letter or word they like, if the user selects a word or letter they previously guessed the will be prompted with a warning that says so they will not lose a life for this.

## Future Features

1. **GUI Hangman**:
A gui hangman would represent the amount of lifes that the user has left to guess.

## Testing
I have manually tested this project by doing the following:
1. Passed the code through the PEP8 linter and confirmer there are no issues
2. Given inputs that are invalid such as numbers, characters and symbols, there are no issues 


## Bugs 

### Solved Bug:
The computer couldn't recognise the symbol - which would have been used in several words, I removed these words from the words list

### Remaining Bugs

None


## Validator Testing:

Passed the PEP8 Validator