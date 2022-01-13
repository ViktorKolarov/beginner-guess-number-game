# -*- coding: utf-8 -*-

import numpy
import random

"""
Spyder Editor

This is a temporary script file.
"""

"Igrica opklade"


cookies = 0 #actually coins for bidding
guesses = 0
bid = 0
multiplyer = [1, 1.20, 2]
playerName = ""



numberToGuess = 0

#Main Menu, kind of
print("\n")
print("\n")
print("\n")
print("\t\t\t\t\t\t\tWelcome to The Guessing Game")
print("\n")
print("\n")
print("\n")
print("\n")
print("\t\t\t\t\t\t\tMade by Viktor and Aleksa")
print("\n")
print("\n")

#Player's name input
print("Enter your name: ")
playerName = str(input())

#Player's cookie count input

counter = 0

while True:
    print("\nEnter how much cookies you have, please:")
    print("(between 1 and 100)")
    cookies = int(input())
    counter = counter + 1
    if cookies > 0 and cookies <= 100:
        counter += counter
        print("\n\n")
        print(playerName + ", welcome to The Guessing Game!")
        print("\n(You have " + str(cookies) + " cookies)")
        print("\n")
        break
    elif cookies <= 0 and counter > 7:   
        print("\nYou really don't want to play do you? Oh well...\n")
        counter += counter
        break

#Difficulty settings

difficulty = ""

counter = 0

while True:
    print("\n\n\n\n\n\n\n")
    print("\t\t\t\t\tChoose your difficulty:\n")
    print("\t\t\t\tEasy(a)  \t\t Medium(b)\t\t Hard(c)  ")
    print("\t\t\t\t1 - 10\t\t     1 - 30\t\t     1 - 100\n")
    print("\n\n\n\n(enter a, b or c)")
    difficulty = str(input())
    counter += counter
    if difficulty == 'a' or difficulty == 'b' or difficulty == 'c':
        break
    if difficulty != 'a' and difficulty != 'b' and difficulty != 'c' and counter > 7:
        break
    
#Setting the difficulty    
    
if difficulty == 'a':
    numberToGuess = random.randint(1, 10)
    print("\n\n\n\n\n\n\n\n\n\n\nEasy, huh? Okay...")
    print("\nYou have to guess the number between 1 and 10.\n\n")
    
    # Game Easy 3 tries
    for guesses in range(1, 4):
        print("Take a guess.")
        guess = int(input())

        if guess > numberToGuess:
            print("Your number is too high boi!")
        elif guess < numberToGuess:
                print("Your number is too low!")
        else:
            break

    if guess == numberToGuess:
        cookies = cookies * 2
        print("Good job " + playerName + " you win some cookies! Now you got " + str(cookies) + " cookies!")    

    else:
        cookies -= cookies
        print("You lost all your cookies :(")
    
    
elif difficulty == 'b':
    numberToGuess = random.randint(1, 30)
    print("\n\n\n\n\n\n\n\n\n\n\nCasual. Nothing wrong with that.")
    print("\nYou have to guess the number between 1 and 30.\n\n")
    
    
    # Game Medium 5 tries
    for guesses in range(1, 6):
        print("Take a guess.")
        guess = int(input())
        
        if guess > numberToGuess:
            print("Your number is too high boi!")
        elif guess < numberToGuess:
            print("Your number is too low!")
        else:
            break

    if guess == numberToGuess:
        cookies = cookies * 2
        print("Good job " + playerName + " you win some cookies! Now you got " + str(cookies) + " cookies!")    

    else:
        cookies -= cookies
        print("You lost all your cookies :(")
    
    
elif difficulty == 'c':
    numberToGuess = random.randint(1, 100)
    print("\n\n\n\n\n\n\n\n\n\n\nSo, you want to lose all your money? I mean, cookies.")
    print("\nYou have to guess the number between 1 and 100.\n\n")
    
    
    # Game Hard 7 tries   
    for guesses in range(1, 8):
        print("Take a guess.")
        guess = int(input())
        
        if guess > numberToGuess:
            print("Your number is too high boi!")
        elif guess < numberToGuess:
            print("Your number is too low!")
        else:
            break

    if guess == numberToGuess:
        cookies = cookies * 2
        print("Good job " + playerName + " you win some cookies! Now you got " + str(cookies) + " cookies!")    

    else:
        cookies -= cookies
        print("You lost all your cookies :(")

        

# The Game

#ulaganje kolacica



"""
for guesses in range(1, 4):
    print("Take a guess.")
    guess = int(input())

    if guess > numberToGuess:
        print("Your number is too high boi!")
    elif guess < numberToGuess:
        print("Your number is too low!")
    else:
        break

if guess == numberToGuess:
    cookies = cookies * 2
    print("Good job " + playerName + " you win some cookies! Now you got " + str(cookies) + " !")    
else:
    cookies -= cookies
    print("You lost all your cookies :(")

"""







