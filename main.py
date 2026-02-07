import time
import random
number=random.randint(1,100)# random number btwn 1-100
def intro():
    print("Welcome to the random Number Generator")
    global name #accessed by all the functions
    name=input("Enter your name:")
    #explain the game
    print(name+", we are playing a game, I guess a random number between 1 and 100 and you try to guess the number I have guessed")
    #check if the number is even or odd
    if number%2==0:
        x="even"
    else:
        x="odd"
    #give a hint
    print("\n This is an {} number".format(x))
    #delay for a few seconds
    time.sleep(1)
    #ask the user for another guess
    print("Go ahead. Guess again!")
#function to handle guessing
def pick():
    guessesTaken=0#number of guesses
    while guessesTaken<6:
        time.sleep (0.25)
        enter=input()
        try:
            #converting the guess into an integer
            guess=int(enter)
            if guess>=1 and guess<=100:
                #increase the guess count
                guessesTaken+=1
                #check if guesses are available
                if guessesTaken<6:
                    #check if the number is smaller than the guessed number
                    if guess<number:
                        print("Hmm, try a bigger number.")
                    if guess>number:
                        print("Try a smaller number")
                    if guess!=number:
                        time.sleep(0.5)
                        print("😕Not really, try again")
                    #if guess is correct
                    if guess==number:
                        break
            else:
                print("The number is not in range, try again")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100")
        except:
            print("Enter a number")
    if guess==number:
        guessesTaken=str(guessesTaken)
        print("Good job,{}!You guessed my number in {} guesses!".format(name,guessesTaken))
    else:
        print("Nope. The number I was thinking of was"+str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes" or playagain=="YES": 
        intro()
        pick()
        print("Do you want to play again?")
        playagain=input()    
