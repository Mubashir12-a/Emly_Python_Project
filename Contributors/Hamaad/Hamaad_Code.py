# Person 3: Display & Game Loop

def displayWordProgress(word, guessed_letters):
    """
    Displays the current progress of the word.
    Guessed letters are shown, others as '_'.
    """
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress.strip())


def displayGameStatus(attempts_left):
    """
    Displays remaining attempts.
    """
    print(f"Attempts left: {attempts_left}")


def showFinalResult(is_win, word):
    """
    Displays final game result.
    """
    if is_win:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"❌ Game Over! The word was: {word}")


def gameLoop():
    """
    Main game loop controller (testing version).
    Actual logic will be integrated in Main.py
    """
    # Hardcoded values for testing
    word = "apple"
    guessed_letters = ['a', 'e']
    attempts_left = 3

    displayWordProgress(word, guessed_letters)
    displayGameStatus(attempts_left)

    # Simulated final result
    showFinalResult(True, word)

if __name__ == "__main__":
    print(displayWordProgress("apple", {"a", "e"}))
    print(displayGameStatus(3))
    print(showFinalResult(True, "apple"))
print("Direct push test by Hamaad")
