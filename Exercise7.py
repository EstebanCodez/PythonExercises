#Write one line of Python that takes a list a and makes a new list that has only the even elements of this list in it.
a = [3,45,63,4,34,6,57,7,5,4,3,23,24,2,42]
even_list = []

for each_element in a:
    if each_element % 2 == 0:
        even_list.append(each_element)

print(even_list)
