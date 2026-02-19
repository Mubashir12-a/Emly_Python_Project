import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Main_Checked_Functions import *


WordsList = ["apple", "banana", "grapes", "orange", "mango"]

selected_word = ''
attempts_left = 0
guessed_letters = set()
Wrong_letters = set()
User_Guess = ''

def displayWordProgress(word, guessed_letters, attempts_left):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += " " + letter + " "
        else:
            progress += "_ "
    output = f"{progress.strip()} | ===> Attempts Left: {attempts_left}"
    print(output)
    return output


def showFinalResult(is_win, word):
    if is_win:
        print(f"{Green}🎉 Congratulations! You guessed the word: {word}{White}")
    else:
        print(f"{Red}❌ Game Over! The word was: {word}{White}")


def checkWinCondition(guessed_letters, selected_word):
    for letter in selected_word:
        if letter not in guessed_letters:
            return False
    return True

def checkLoseCondition(attempts_left):
    if attempts_left == 0:
        return True
    return False


def gameLoop():     
    global selected_word, guessed_letters, attempts_left, User_Guess, Wrong_letters, WordsList
       
    selected_word, guessed_letters, attempts_left = initializeGameState(
        selected_word, guessed_letters, attempts_left, WordsList
    )
    displayWordProgress(selected_word, guessed_letters, attempts_left)
    
    while checkLoseCondition(attempts_left) != True:
        User_Guess = getUserGuess(guessed_letters, Wrong_letters)
        
        guessed_letters, Wrong_letters, attempts_left = processGuess(
            User_Guess, selected_word, guessed_letters, Wrong_letters, attempts_left
        )
        print(guessed_letters, Wrong_letters, attempts_left)
        
        displayWordProgress(selected_word, guessed_letters, attempts_left)

gameLoop()


