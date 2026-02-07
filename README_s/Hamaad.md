# Hamaad-Contributor (Person 3) – Display & Game Loop

## Role
Handled the display logic and game flow for the Hangman CLI game.

## Functions Implemented

### displayWordProgress(word, guessed_letters)
Displays the current state of the word by revealing guessed letters and hiding others using underscores.

### displayGameStatus(attempts_left)
Shows the number of attempts remaining for the player.

### gameLoop()
Controls the game flow for testing purposes. Displays word progress, game status, and final result.

### showFinalResult(is_win, word)
Displays the final win or lose message based on game outcome.

## Variables Used
- word: stores the word to be guessed
- guessed_letters: list of letters guessed so far
- attempts_left: number of remaining attempts

## Issues Faced
- Understanding role-based function separation
- Ensuring no logic overlap with other team members

## Learning Outcome
Learned modular programming, team-based development, and clean function design.
