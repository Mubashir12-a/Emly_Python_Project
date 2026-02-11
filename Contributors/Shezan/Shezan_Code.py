# Function to get user input
def getUserGuess():
    # Ask the user to enter a guess
    # Remove extra spaces from beginning and end
    # Convert the guess to lowercase
    guess = input("Enter your guess: ").strip().lower()
    
    # Return the processed guess
    return guess


# Function to validate the user's guess
def validateGuess(guess):
    # Check if:
    # 1. The length of guess is NOT equal to 1
    # OR
    # 2. The guess is NOT an alphabet letter
    if len(guess) != 1 or not guess.isalpha():
        # If any condition is true, return False (invalid guess)
        return False
    
    # Otherwise return True (valid guess)
    return True


# Function to check if guess was already used
def isRepeatedGuess(guess, guessed_letters):
    # Loop through all previously guessed letters
    for letter in guessed_letters:
        # If current guess matches any letter in guessed_letters
        if guess == letter:
            # Return True (it is repeated)
            return True
    
    # If loop completes without match
    # Return False (not repeated)
    return False


# Function to process the guess
def processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    # Loop through each letter in the secret word
    for letter in secret_word:
        
        # If guessed letter matches any letter in secret word
        if guess == letter:
            # Add guess to guessed_letters set
            guessed_letters.add(guess)
            
            # Display correct guess message
            print("Correct guess!")
            
            # Return updated values (no attempt deducted)
            return guessed_letters, wrong_letters, attempts_left
    
    # If guess is not found in secret word
    # Add guess to wrong_letters set
    wrong_letters.add(guess)
    
    # Decrease remaining attempts by 1
    attempts_left -= 1
    
    # Display wrong guess message
    print("Wrong guess!")
    
    # Return updated values
    return guessed_letters, wrong_letters, attempts_left
