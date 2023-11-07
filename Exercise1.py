# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 

name = input("What is your name? \n")
age = int(input("What is your age? \n"))
yearAge100 = (100 - age) + 2023

print ("Your name is {} and you're {} years old. you will turn 100 in the year {}".format(name,age,yearAge100))
