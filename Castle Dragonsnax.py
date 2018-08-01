#my first if statement game

import random

print ("You are in a dark room in a mysterious castle")
print ("In front of you are three doors. You must choose one.")
playerChoice = input("Choose 1, 2, or 3...")

if playerChoice == "1":
    print ("You find a room full of treasure")
    print ("GAME OVER, YOU WIN!")
elif playerChoice == "2":
    print ("You lose")
elif playerChoice == "3":
    print ("you lose")
elif playerChoice == "4":
    print ("You enter a room with a sphix")
    print ("It asks your to guess what number it is thinking of, between 1 and 10")
else:
    print ("You didn't select 1, 2, 3 or 4")
guess = int(random.randint (1,10))
#print (guess)
number = int(input("What number do you choose? "))
if number == guess:
    print ("The sphinx says you guessed correctly")
    print ("GAME OVER. YOU WIN")
else:
    print ("The sphix says you gussed wrong")
    print ("GAME OVER. YOU LOOSE")
    

    
    

    

