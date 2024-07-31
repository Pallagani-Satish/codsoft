#imports random module
import random

#prints multiple line strings
#display the rules of the game
print('''Winning Rules Of Rock Paper Scissors \n
      Rock vs Paper --> Paper wins
      Rock vs Scissors --> Rock wins
      Paper vs Scissors --> Scissor wins''')
print("Enter your choice")
print("1.Rock")
print("2.Paper")
print("3.Scissor")
print("\n")

while True:

    # take the input from user
    choice = int(input("Enter your choice :"))

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        print("It's not a valid Choice")
        choice = int(input('Enter a your choice again:'))

    if choice == 1:
        choice_name="Rock"
        print("User choice is Rock")
    elif choice == 2:
        choice_name="Paper"
        print("User choice is Paper")
    else:
        choice_name="Scissors"
        print("User choice is Scissor")

    # print user choice
    print('Now its Computers Turn....')

    # Computer chooses randomly any number among 1 , 2 and 3
    #  Using randint method of random module
    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name="Rock"
        print("Computer choice is Rock")
        
    elif comp_choice == 2:
        comp_choice_name="Paper"
        print("Computer choice is Paper")
    else:
        comp_choice_name="Scissor"
        print("Computer choice is Scissor")
    
    print(choice_name, 'Vs', comp_choice_name)
    
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    
    # condition for winning
    elif (choice == 1 and comp_choice == 2):
        print('paper wins', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins', end="")
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3):
        print('Rock wins\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins\n', end="")
        result = 'RocK'
    elif (choice == 2 and comp_choice == 3):
        print('Scissors wins', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins', end="")
        result = 'Rock'
    
    # Printing either user or computer wins or draw
    if result == 'TIE':
        print("<== Its a draw ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("\nDo you want to play again? (Y/N)")
    
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break
