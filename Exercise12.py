# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.
import random

random_list = random.sample(range(5,25),5)

def first_and_last_finder(random_list):
    first_and_last_list =  [random_list[0],random_list[-1]]
    print("\nHere is the random list:\n{}\n".format(random_list))
    print("Here is the first and last:\n{}\n".format(first_and_last_list))

first_and_last_finder(random_list)

