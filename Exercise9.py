# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# Hint: remember to use the user input lessons from the very first exercise

#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

random_number = random.randint(1,20)
guessed_number = int(input("\nGuess the random number (1-20):"))
number_of_tries = 0

while guessed_number != random_number:
    number_of_tries = number_of_tries + 1
    if guessed_number == 0:
        break
    elif guessed_number > random_number:
        guessed_number = int(input("\nToo high! try again (or press 0 to quit):"))
    elif guessed_number < random_number:
        guessed_number = int(input("\nToo low! try again (or press 0 to quit):"))

if guessed_number == random_number:
    number_of_tries = number_of_tries + 1
    print("\nYou are exactly right! The number was {} and it took you {} tries\n".format(random_number,number_of_tries))
elif guessed_number == 0:
    print("\nYou are a quitter\n")
    