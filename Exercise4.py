# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

number = int(input("Type in a number: "))
CreatedList = range(1,number)
DivisorList = []

for EveryElement in CreatedList:
    if number % EveryElement == 0:
        DivisorList.append(EveryElement)

print("The numbers {} are diversors for your number provided: {}".format(DivisorList,number))

