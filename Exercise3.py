# Take a list, and write a program that prints out all the elements of the list that are less than 5.

a = [56,2,37,5,3,2,7,67,54,2,9,1,2,1,56]

greaterthannum = []
lessthannum = []
number = int(input("Type in any number: "))

for element in a:
    if element > number:
        greaterthannum.append(element)
    elif element < number:
        lessthannum.append(element)

print("These numbers from the list are greater than the number you provided \n {}".format(greaterthannum))
print("These numbers from the list are less than the number you provided \n {}".format(lessthannum))

