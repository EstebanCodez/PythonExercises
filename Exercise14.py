#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_duplicates_set_method(any_list):
    turn_to_set = set(any_list)
    turn_back_to_list = list(turn_to_set)
    return turn_back_to_list

def remove_duplicates_loop_method(any_list):
    removed_duplicates = []
    for each_element in any_list:
        if each_element not in removed_duplicates:
            removed_duplicates.append(each_element)
    return removed_duplicates

original_list = [1,1,2,3,4,3,2,4,5,4,6,7,6,5,4,3,5,4,6,7,6,6,8,9]

print(f"\nThis is the set method: {remove_duplicates_set_method(original_list)}")
print(f"\nThis is the loop method: {remove_duplicates_loop_method(original_list)}\n")

