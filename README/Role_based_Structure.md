# Role-Based Structure

This document reflects contributor responsibilities based on the actual files inside `Contributors/` and final project integration.

## Shezan - Input and Guess Processing

Source file:
- `Contributors/Shezan/Shezan_Code.py`

Implemented responsibilities:
- `getUserGuess()`
- `validateGuess(guess)`
- `isRepeatedGuess(guess, guessed_letters)`
- `processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left)`

Scope owned:
- User input handling
- Guess validation rules
- Repeated-guess detection
- Guess result processing and attempt deduction

## Hamaad (Hammad) - Display and End-State Checks

Source file:
- `Contributors/Hamaad/Hamaad_Code.py`

Implemented responsibilities:
- `displayWordProgress(word, guessed_letters, attempts_left)`
- `showFinalResult(is_win, word)`
- `checkWinCondition(guessed_letters, selected_word)`
- `checkLoseCondition(attempts_left)`

Scope owned:
- Word progress UI rendering
- Final win/lose message display
- Win/lose condition helpers

## Mubashir - Everything Else (Core Ownership)

Core ownership and remaining responsibilities:
- Project architecture and module organization
- Integration of contributor functions into final runnable modules
- Main entry flow and start/exit handling in `Main.py`
- Game orchestration in `Gameloop.py`
- Final consolidated implementation in `Main_Checked_Functions.py`
- Color configuration integration via `CL_Colors.py`
- Documentation updates and project consistency across files

## Final Integration Note

The final game is integrated and run through:
- `Main.py` -> `gameLoop()` from `Gameloop.py`
- `Gameloop.py` -> helper functions from `Main_Checked_Functions.py`

This means contributor functions were used as role-based building blocks, and final end-to-end ownership/integration remains under Mubashir.
