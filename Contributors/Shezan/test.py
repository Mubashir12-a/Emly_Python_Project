# test.py
# Manual testing for hangman functions

from Shezan_Code import validateGuess, isRepeatedGuess, processGuess
# Replace "your_file_name" with your actual python file name (without .py)

print("===== MANUAL TESTING STARTED =====\n")

# ---------------------------------
# Test validateGuess()
# ---------------------------------
print("Testing validateGuess()")

print("validateGuess('A') →", "Valid" if validateGuess('A') else "Invalid")
print("validateGuess('1') →", "Valid" if validateGuess("1") else "Invalid")

print("\n---------------------------------\n")

# ---------------------------------
# Test isRepeatedGuess()
# ---------------------------------
print("Testing isRepeatedGuess()")

print("isRepeatedGuess('a', ['a','b']) →", 
      isRepeatedGuess('a', ['a','b']))

print("\n---------------------------------\n")

# ---------------------------------
# Test processGuess()
# ---------------------------------
print("Testing processGuess()")

secret_word = "apple"
guessed_letters = {'a'}          # set
wrong_letters = set()            # empty set
attempts_left = 5

# Wrong guess test
guessed_letters, wrong_letters, attempts_left = processGuess(
    'c',
    secret_word,
    guessed_letters,
    wrong_letters,
    attempts_left
)

print("\nAfter processGuess('c', 'apple', {'a'})")
print("Guessed Letters:", guessed_letters)
print("Wrong Letters:", wrong_letters)
print("Attempts Left:", attempts_left)

print("\n===== TESTING COMPLETED =====")
