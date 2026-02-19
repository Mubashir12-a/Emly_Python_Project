# Hamaad – Contributor (Person 3)
## Display Logic & Game Loop – Hangman CLI Game

---

## 👤 Contributor Information

- **Name:** Hamaad  
- **Role:** Person 3 (Display & Game Flow Handler)  
- **Module:** Hangman Command-Line Interface (CLI) Game  
- **Project Type:** Team-based Python mini project  

---

## 🎯 Role & Responsibility

My primary responsibility in this project was to **handle the display logic and control the overall game flow** of the Hangman CLI game.

This includes:
- Showing the current progress of the guessed word
- Displaying remaining attempts
- Managing the game loop
- Displaying the final game result (win / lose)

I focused on making the game **clear, readable, and user-friendly** when played in the terminal.

---

## 🧠 Functions Implemented

### 1️⃣ `displayWordProgress(word, guessed_letters)`

**Purpose:**  
Displays the current state of the word by:
- Revealing letters that have already been guessed
- Hiding unguessed letters using underscores (`_`)

**Example Output:**

Word: h _ n g m a n


This helps the player visually track their progress during the game.

---

### 2️⃣ `displayGameStatus(attempts_left)`

**Purpose:**  
Shows how many attempts the player has remaining.

**Example Output:**

Attempts remaining: 4


This function improves clarity and prevents confusion during gameplay.

---

### 3️⃣ `gameLoop(word)`

**Purpose:**  
Controls the entire game flow:
- Takes user input
- Calls display functions
- Tracks guessed letters
- Reduces attempts on wrong guesses
- Determines win or loss conditions

This function acts as the **central controller** of the game logic.

---

### 4️⃣ `showFinalResult(is_win, word)`

**Purpose:**  
Displays the final message when the game ends.

**Possible Outputs:**
🎉 Congratulations! You guessed the word correctly.
or
❌ Game Over! The correct word was: hangman

---

## 🔧 Variables Used

| Variable Name     | Description |
|------------------|------------|
| `word`            | The word to be guessed |
| `guessed_letters`| List of letters guessed by the player |
| `attempts_left`  | Number of attempts remaining |

---

## 🧪 How to Test My Code

### ▶️ Run Individually (For Testing)

From the project root directory:

python Contributors/Hamaad/Hamaad_Code.py

This allows isolated testing of display logic and game loop.

▶️ Run Through Main Game

Run the main entry file:

python Main.py

Ensure Hamaad_Code.py is properly imported inside Main.py.

⚠️ Challenges Faced

Understanding role-based function separation in a team project

Avoiding overlap with logic implemented by other contributors

Maintaining clean terminal output

Ensuring compatibility with the main game file

📚 Learning Outcomes

Through this contribution, I learned:

How to structure Python functions for CLI-based games

Managing game loops effectively

Working collaboratively using Git & GitHub

Writing clean, readable terminal output

Proper folder structure and modular coding

✅ Conclusion

My contribution ensures that the Hangman game:

Runs smoothly

Is easy to understand for players

Displays meaningful game feedback

Ends with clear win or loss messages

This module improves the user experience of the Hangman CLI game.

Contributor: Hamaad
Role: Display Logic & Game Loop Handler