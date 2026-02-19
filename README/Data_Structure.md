# Data Structures and Control Flow in Hangman

This document maps the project implementation to the data structures and core control concepts currently used in code.

## 1) List

Used as:
- `WordsList` in `Gameloop.py`

Why it is used:
- Stores candidate words in one indexed collection
- Works directly with `random.choice()` for word selection

Example:
```python
WordsList = ["apple", "banana", "grapes", "orange", "mango"]
```

## 2) String

Used as:
- `selected_word`
- `guess` input from player

Why it is used:
- Secret word is a sequence of characters
- Easy per-letter traversal and comparison in loops

Example:
```python
for letter in selected_word:
    if guess == letter:
        ...
```

## 3) Set

Used as:
- `guessed_letters`
- `Wrong_letters`

Why it is used:
- No duplicates by design
- Fast membership checks (`in`) for repeated guesses and win logic

Examples:
```python
guessed_letters = set()
Wrong_letters = set()
```

## 4) Integer

Used as:
- `attempts_left`

Why it is used:
- Counter for remaining wrong attempts
- Directly drives lose condition

Example:
```python
attempts_left = 5
attempts_left -= 1
```

## 5) While Loop

Used as:
- Main gameplay loop in `Gameloop.py`

Current logic:
```python
while not checkLoseCondition(attempts_left) and not checkWinCondition(guessed_letters, selected_word):
    ...
```

Why it is used:
- Continues game until either lose or win state is reached

## 6) Conditional Statements

Used as:
- Input validation
- Repeated guess checks
- Guess correctness checks
- Start/exit decisions in `Main.py`

Examples:
- `if validateGuess(guess):`
- `if isRepeatedGuess(...):`
- `if Player_Mood == 'Y' or Player_Mood == 'y':`

## 7) Functions (Modular Design)

Used as:
- Isolate game responsibilities into reusable units

Key functions in `Main_Checked_Functions.py`:
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

Key function in `Gameloop.py`:
- `gameLoop`

Why it is used:
- Better readability
- Easier testing and debugging
- Clear separation between flow control and helper logic

## Mapping Table

| Concept | Where Used | Purpose |
|---|---|---|
| List | `WordsList` | Stores all candidate words |
| String | `selected_word`, `guess` | Character-by-character gameplay logic |
| Set | `guessed_letters`, `Wrong_letters` | Prevent duplicates and enable fast lookup |
| Integer | `attempts_left` | Tracks remaining attempts |
| While loop | `gameLoop()` | Runs game until win/lose |
| Conditionals | Across main and helper functions | Drives decisions and state updates |
| Functions | `Main.py`, `Gameloop.py`, `Main_Checked_Functions.py` | Modular, maintainable design |
