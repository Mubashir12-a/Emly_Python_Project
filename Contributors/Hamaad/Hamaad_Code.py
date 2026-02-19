from CL_Colors import *

def displayWordProgress(word, guessed_letters, attempts_left):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += " " + letter + " "
        else:
            progress += " x "
    print(f"\033[1;30;47m{progress.strip()}  {Red}|-=-=-> Attempts Left: {attempts_left}\033[0m\n")


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
