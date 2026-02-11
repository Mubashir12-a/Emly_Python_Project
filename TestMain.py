import random

# temp data:

guessed_letters = ['a', 'p', 'l', 'e']
words = ["apple", "banana", "grapes", "orange", "mango"]


def getUserGuess():
    guess = input("Enter your guess: ").strip().lower()
    
    if validateGuess(guess):
        print("user guess is valid")
        
        if isRepeatedGuess(guess, guessed_letters):
            print("user guess is repeated")
            return False
        else:
            print("user guess is not repeated")
            return True
    else:
        print("user guess is invalid")
        return False
        
    


def validateGuess(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True

def isRepeatedGuess(guess, guessed_letters):
    for letter in guessed_letters:
        if guess == letter:
            return True
    return False

def processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    for letter in secret_word:
        if guess == letter:
            guessed_letters.add(guess)
            print("Correct guess!")
            return guessed_letters, wrong_letters, attempts_left
    wrong_letters.add(guess)
    attempts_left -= 1
    print("Wrong guess!")
    return guessed_letters, wrong_letters, attempts_left






def getRandomWord():
    word = random.choice(words)
    return word


def initializeGameState():
    selected_word = getRandomWord()
    attempts_left = 5
    guessed_letters = []

    return selected_word, attempts_left, guessed_letters


def checkWinCondition(guessed_letters, selected_word):
    for letter in selected_word:
        if letter not in guessed_letters:
            return False
    return True


def checkLoseCondition(attempts_left):
    if attempts_left == 0:
        return True
    return False



words = ["apple", "banana", "grapes", "orange", "mango"]





if __name__ == "__main__":

   
    #check functions:
    
    
    
    # checkLoseCondition() ---> Working ✅
    
    # _______________________________________________________________________________
    # | for i in range(5, -1, -1):                                                  |
    # |     print(f"Player Lose: {checkLoseCondition(i)} | Attempts Left: {i}");    |
    # |_____________________________________________________________________________|
        

    
    # getUserGuess() --> Working ✅
    # validateGuess() --> Working ✅
    # isRepeatedGuess() --> Working ✅
    
    # _______________________________
    # | while True:                 |    
    # |     temp = getUserGuess()   |
    # |                             |
    # |     if temp:                |
    # |         break               |
    # |_____________________________|
    
    
    # initializeGameState() --> Working ✅
    
    # ___________________________________
    # |                                 |
    # |  print(initializeGameState());  |
    # |_________________________________|
    
    
    # getRandomWord() --> Working ✅
    
    # _______________________________
    # |                             |
    # | print(getRandomWord());     |
    # |_____________________________|
    
    # checkWinCondition() --> Working ✅
    
    # _______________________________________________________________
    # |                                                             |
    # print(checkWinCondition(['a', 'p', 'l', 'e'], "apple"));      |
    # |_____________________________________________________________|
    
    
    # processGuess() --> Pending review
    
    print(processGuess('a', "apple", set(), set(), 5));

    
    
    
    
       
    
    
    
        
    
    
    
    
