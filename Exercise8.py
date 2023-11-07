#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

relationships = {('Rock','Scissors'): 'Rock',('Rock','Paper'): 'Paper',('Paper','Scissors'): 'Scissors',
                 ('Scissors','Rock'): 'Rock',('Paper','Rock'): 'Paper',('Scissors','Paper'): 'Scissors',
                 ('Rock','Rock'): 'Nobody',('Paper','Paper'): 'Nobody',('Scissors','Scissors'): 'Nobody'}

def compare_selections(selection1, selection2):
    return relationships.get((selection1,selection2))

print("\nWelcome to my Rock, Paper, Scissors game!\n")

user1 = input("\n(USER1) Enter Rock, Paper, or Scissors:") 
while user1 not in ('Rock','Paper','Scissors'):
    print("\n Not a valid selection")
    user1 = input("\n(USER1) Enter Rock, Paper, or Scissors:") 

user2 = input("\n(USER2) Enter Rock, Paper, or Scissors:")
while user2 not in ('Rock','Paper','Scissors'):
    print("\n Not a valid selection")
    user2 = input("\n(USER2) Enter Rock, Paper, or Scissors:") 

result = compare_selections(user1,user2)

print("\nUSER1 selected {}\nUSER2 selected {}\nThe winner is {}!!!\n".format(user1,user2,result))
