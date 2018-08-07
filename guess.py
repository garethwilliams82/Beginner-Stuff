import random

guess = int(random.randint(1,10))
guess_made = int (0)

#print (guess_made)
print (guess)

print ("Simple guessing game")
print ("You have 6 attempts")

while guess_made < 6:

    playerchoice = int (input ("Pick a number between 1 & 10 "))
    print (guess_made)
    guess_made += 1
    print guess_made, "guess made"
        
    if guess < playerchoice:
        print ("Too High")
        continue
    if guess  > playerchoice:
       print ("Too Low")
       continue
    if guess == playerchoice:
        print ("Well done")
        break
