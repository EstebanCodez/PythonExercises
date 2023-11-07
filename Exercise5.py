#Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

List_A = random.sample(range(1, 20), 15)
List_B = random.sample(range(1, 20), 15)
Common_List = []

for EveryElement in List_A:
    if EveryElement in List_B:
        Common_List.append(EveryElement)

print("This is random list A: \n {}".format(List_A))
print("This is random list B: \n {}".format(List_B))
print("This is what they have in common: \n {}".format(Common_List))



    