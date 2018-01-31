
import random

minimum = int(input("Enter the lower range: "))
maximum = int(input("Enter the higher range: "))
maxTries= 4

myRandomNumber = random.randint(minimum,maximum)
guessedNumber = int(input("Guess a number between 1 and 6: "))

tries = 0

while(tries < maxTries):
    if(guessedNumber != myRandomNumber):
        print("You guessed incorrectly")
        tries = tries + 1
        guessedNumber = int(input("Guess again: "))
        if(guessedNumber == myRandomNumber):
            print("You guessed correctly")
            exit(0)

print("Unfortunately, all your guesses were wrong.")









