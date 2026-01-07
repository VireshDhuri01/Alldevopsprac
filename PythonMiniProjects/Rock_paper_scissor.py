# Import random module
import random

# Print multiline instruction
# perform string concatenation
print("Winning Rules: \n"
      + "Rock vs Paper = Paper Wins \n"
      + "Rock vs Scissor = Rock Wins \n"
      + "paper vs Scissor = Scissor Wins \n")

while True:
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
    # takes input from user
    choice = int(input("User turn: "))

    # looping until user enter valid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

        # initialize value of variables
    # corresponding to the chosen value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("Your choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # computer chooses randomly any number among 1,2&3
    # using randint method
    comp_choice = random.randint(1, 3)

    # looping until computer choice is
    # equal to choice
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

        # initialize value of comp_choice
    # corresponding to the variable
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("\n Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # Condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("Paper Wins => ", end="")
        result = "Paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock Wins =>", end="")
        result = "Rock"
    else:
        print("Scissor Wins =>", end="")
        result = "Scissor"

    # Printing the results
    if result == choice_name:
        print("   YOU WON  ")
    else:
        print("  YOU LOSE  ")

    print("Do you want to play again? (Y/N)")
    ans = input()

    # User wants to continue playing or end game
    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playling")