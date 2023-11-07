# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

number = int(input("\n Type in any number: "))

if number % 2 == 0:
    print("\n You gave an EVEN number")
elif number % 2 == 1:
    print("\n You gave an ODD number \n")