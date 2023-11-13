# Write a password generator and be creative with how you generate passwords
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

#Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string

def generate_random_string(length):
	letters = string.ascii_letters
	random_string = ''.join(random.choice(letters) for i in range(length))
	return random_string

random_string = generate_random_string(5)
ask = input(f'\nHeres a password recommendation: {(random_string)}\nWould you like another recommendation?\n\n')

while ask.strip().lower() != 'no':
	ask = input(f'\nHeres a password recommendation: {(random_string)}\nWould you like another recommendation?\n\n')
	random_string = generate_random_string(5)
	
print("\nThank you for using the password generator!\n")

