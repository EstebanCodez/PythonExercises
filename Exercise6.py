# Ask the user for a string and print out whether this string is a palindrome or not. 
# A palindrome is a string that reads the same forwards and backwards.

word = input("\nEnter a word: ")
reverse_word = word[::-1]

if word == reverse_word: 
    print("\nSince {} spelled backwords is {}, you made a palindrome\n".format(word,reverse_word))
else:
    print("\nYou did NOT make a palindrome\n")
