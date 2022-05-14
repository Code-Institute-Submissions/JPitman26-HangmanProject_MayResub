# **Terminal Hangman**

[The Live version of this project is here!](https://jp-hangman.herokuapp.com/)

  Terminal Hangman is a Python built game, which runs in the Code Institute's mock terminal on Heroku.com

## Table Of Contents

- [**Terminal Hangman**](#terminal-hangman)
  - [Table Of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [Site User Goals](#site-user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [Game Play Features](#game-play-features)
    - [The Start Page](#the-start-page)
    - [Game Play](#game-play)
    - [Exit](#exit)
  - [Features Left to Implement](#features-left-to-implement)
  - [Testing and Bugs](#testing-and-bugs)
    - [Menu Input Validation](#menu-input-validation)
    - [Game Play Input Validation](#game-play-input-validation)
  - [PEP8](#pep8)
  - [Deployment](#deployment)
  - [Credits](#credits)

## Project Overview

  This Hangman game is a Python terminal game, designed to run in the Code Institues mock terminal on Heroku.
  Users try to guess the letters within a word randomly fetched from the local words.py file.
  If the user is incorrect the Hangman terminal will tell you you have an incorrect pick and how many lives you have left untill the word is guessed.

### Site User Goals

- I want to be able to play a simple online game.
- I want to be able to see which words or letters I have previously guessed.
- I want to be able to replay the game without repeating the same word each time.


### Site Owner Goals

- I want to provide a stimulating game
- I want the user to return and replay the quiz.
- I want to enable the user to easily navigate the game without encountering any difficulty.


## Game Play Features

### The Start Page

- The start page prompts the user to play the game hangman.
- It is a simple set up that is easy to understand.

### Game Play

  The player is prompted to guess a letter they will have nine guesses before game over. The word will be hidden to start the game and will be represented with dashes.

    1. --------
    2. -o------
    3. Mo--m---
    4. Mon-m-n-
    5. Mon-m-nt
    6. Monument
  
  If a guess is a valid guess and is in the word a message tells them the guess was correct and their guess will be displayed where the dotted line was.

  The user also has the ability to guess the full word at any time this will constitute a life but will finish the game quicker.

  If the user guesses a letter or word that is incorrect they will be given a message that tells them that the word or letter that they picked is not in the word and to try again, the user will then lose a life.

  If the user selects a letter or word that they had previously selected they will be given the message you have already selected this letter and to try again, the user will not lose a life for this mistake.

  If the guess is invalid the user will be given a message tellin them that their guess was invalid and to choose a letter or word, they will not lose a life for this mistake.

### Exit

  The player can choose to exit to the terminal after game play if required. They will be asked if they would like to play again and to select the simple (Y/N) option.

## Features Left to Implement

- Difficulty Levels. Retrieving only words of a certain length according to the Player selected difficultly level.
- Increase the gap between the underscores representing the blank word. At present, in some resolutions these underscores can appear to be joined together without any gap.
- Visual representation of the hangman that is drawn throughout the game 

## Testing and Bugs

I have manually tested the site in my local terminal and in the Code Institute Heroku terminal.

### Menu Input Validation

If the player inputs an invalid input on the menu input, the player is advised this is an invalid input and is asked to make a revised choice.

### Game Play Input Validation

If the player inputs an invalid input during game play, the player is advised this is an invalid input and to choose a valid guess.


## PEP8

  Passed the code through a PEP8 linter and confirmed there are no problems.

## Deployment

  I deployed the project code to GitHub and pushed it to Heroku as an [Heroku Terminal App](https://jp-hangman.herokuapp.com/).

  The steps to deployment are:

  1. Fork or clone this repository to your own GitHub repository.
  2. Create a Google Spreadsheet
  3. Create a new [Heroku App](https://id.heroku.com/login/).
  4. Set the buildbacks to Pyhton and NodeJS in that order.
  5. Add Config Var keys  
     - PORT, 8000
  6. Link the Heroku app to repository
  7. Click on Deploy

## Credits

- Code Institute for the deployment terminal
- Google
- Stackoverflow
- YouTube videos

[The Live version of this project can be found here.](https://jp-hangman.herokuapp.com/)
