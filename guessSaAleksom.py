import random

#ulaganje kolacica

print("Give me your cookies! How much do you got?")
cookies = int(input())

print("Ooo you got "+ str(cookies) +" ? Thats great! Make sure that you guess right so you can doubble it. ;-)")
print("Oh sorry, almost forgot...Whats your name?")
name = input()
print("Well " + name + " im thinking of a number bewteen 1 and 7.")
secretNumber = random.randint(1, 7)

for guessesTaken in range(1, 4):
    print("Take a guess.")
    guess = int(input())

    if guess > secretNumber:
        print("Your number is too high boi!")
    elif guess < secretNumber:
        print("Your number is too low!")
    else:
        break

if guess == secretNumber:
    cookies = cookies * 2
    print("Good job " + name + " you win some cookies! Now you got " + str(cookies) + " !")    
else:
    cookies -= cookies
    print("You lost all your cookies :(")


    

