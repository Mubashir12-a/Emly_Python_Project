# Emly Python Project

CLI Hangman game (single player) built in Python with a modular structure.

## Project Structure

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

## Current Module Roles

- `Main.py`
  - Entry point.
  - Asks the player whether to start the game.
  - Calls `gameLoop()` from `Gameloop.py`.

- `Gameloop.py`
  - Controls the game lifecycle.
  - Initializes game state.
  - Runs the main loop until win or lose.
  - Shows final result and wrong guesses.

- `Main_Checked_Functions.py`
  - Core game helpers:
    - input and validation
    - random word selection
    - guess processing
    - win/lose checks
    - word progress display

- `CL_Colors.py`
  - ANSI color constants used for styled terminal output.

## Game Flow

1. Player starts from `Main.py`.
2. A random secret word is selected from:
   - `apple`, `banana`, `grapes`, `orange`, `mango`
3. Attempts are initialized to `5`.
4. Player enters one-letter guesses.
5. Correct guesses are revealed in the word progress.
6. Wrong guesses reduce attempts and are tracked.
7. Game ends when:
   - all letters are guessed (win), or
   - attempts reach `0` (lose).

## How to Run

From the project root:

```bash
python Main.py
```

## Notes About Recent Changes

- Game entry now uses `from Gameloop import gameLoop` and calls the function directly.
- Main loop condition in `Gameloop.py` uses:
  - continue while `not lose` and `not win`
- End-of-game summary now displays final result and wrong letters.
