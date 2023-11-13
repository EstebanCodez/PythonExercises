#Create a program that will play the “cows and bulls” game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
#For every digit that the user guessed correctly in the correct place, they have a “cow”.
#For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
#Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

random_list = random.sample(range(1, 10), 4)
print(random_list)
trying = "Yes"

def cows_and_bulls(random_list, user_input_number):
    number_bulls = 0
    number_cows = 0
    for index1 in range(len(user_input_number)):
        for index2 in range(len(random_list)):
            if index1 == index2:
                if user_input_number[index1] == random_list[index2]:
                    number_cows = number_cows + 1
                elif user_input_number[index1] != random_list[index2]:
                    number_bulls = number_bulls + 1
    print(f'\nYou have {number_cows} cows and {number_bulls} bulls\n')
    return number_cows, number_bulls


while trying == 'Yes':
    user_input = input('\nEnter a 4 digit number:\n')
    if len(user_input) == 4:
        user_input_number = []
        for each_letter in user_input:
            convert = int(each_letter)
            user_input_number.append(convert)
        number_cows, number_bulls = cows_and_bulls(random_list, user_input_number)
        if number_cows == 4:
            print('\nYou won the game!\n')
            break
        trying = input('\nTry again?(Yes/No):\n')
    else:
        print('\nYou gave a WRONG # of digits\n')








