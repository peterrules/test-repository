import random
# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

answer = random.randint(1, 20)
number = int(input("Guess a number between 1 and 20! "))
numberofguesses = 0

while {True}:
    numberofguesses = numberofguesses + 1
    if number == answer:
        print(f"Correct! The number was {answer}, it took you {numberofguesses} guess(es)!")
        break     

    if numberofguesses > 2:
        print(f"Out of guesses! The number was {answer}")
        break
    elif number > answer:
        print("Too high! The number needs to be lower!")
        number = int(input("Guess a number between 1 and 20! "))
    elif number < answer:
        print("Too low! The number needs to be higher!")
        number = int(input("Guess a number between 1 and 20! "))
    else: 
        print("invalid input")
        number = int(input("Guess a number between 1 and 20! "))

        