# Project Structure Info

## Repository Layout

```text
Emly_Python_Project/
|-- Contributors/
|-- Docs/
|-- README/
|   |-- Data_Structure.md
|   |-- Program_DryRun.md
|   |-- Project_Structure_Info.md
|   `-- Role_based_Structure.md
|-- CL_Colors.py
|-- Main.py
|-- Gameloop.py
|-- Main_Checked_Functions.py
`-- README.md
```

## File Responsibilities

- `Main.py`
  - Project entry point.
  - Asks player to start (`Y/y`) or exit (`RETURN/R/r`).
  - Calls `gameLoop()` from `Gameloop.py`.

- `Gameloop.py`
  - Orchestrates full game execution.
  - Initializes state using `initializeGameState(...)`.
  - Runs game loop until win/lose.
  - Displays final result and wrong guessed letters.

- `Main_Checked_Functions.py`
  - Contains core helper functions:
    - `getUserGuess`
    - `initializeGameState`
    - `displayWordProgress`
    - `processGuess`
    - `validateGuess`
    - `isRepeatedGuess`
    - `getRandomWord`
    - `checkLoseCondition`
    - `checkWinCondition`
    - `showFinalResult`

- `CL_Colors.py`
  - Terminal color constants used across output messages.

## Runtime Flow

1. Run `Main.py`.
2. Player confirms start.
3. `gameLoop()` initializes:
   - random `selected_word`
   - `attempts_left = 5`
   - empty `guessed_letters`
4. Loop continues while:
   - `not checkLoseCondition(attempts_left)` and
   - `not checkWinCondition(guessed_letters, selected_word)`
5. For each turn:
   - read user guess
   - validate and process guess
   - update `guessed_letters` / `Wrong_letters` / `attempts_left`
   - display current word progress
6. On exit from loop:
   - show win/lose message
   - show wrong guessed letters

## Current Data Used in Game

- Word list: `apple`, `banana`, `grapes`, `orange`, `mango`
- Attempts: `5`

## How to Run

```bash
python Main.py
```
