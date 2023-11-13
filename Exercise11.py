# Ask the user for a number and determine whether the number is prime or not. 
# For those who have forgotten, a prime number is a number that has no divisors. 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

Number = int(input("\nType in a number: "))
CreatedList = range(2,Number)
DivisorList = []

for EveryElement in CreatedList:
    Divisor = Number % EveryElement
    DivisorList.append(Divisor)

if 0 not in DivisorList:
        print("\nYou gave a prime number!\n")
elif 0 in DivisorList:
    print ("\nYou did NOT give a prime number\n")
