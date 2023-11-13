# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the value of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …

def fibonacci(position_in_sequence):
    if position_in_sequence == 0:
        return position_in_sequence
    elif position_in_sequence == 1:
        return position_in_sequence
    elif position_in_sequence > 1:
        solution = fibonacci(position_in_sequence - 1) + fibonacci(position_in_sequence - 2)
        return solution

position_in_sequence = 5
print(fibonacci(position_in_sequence))


