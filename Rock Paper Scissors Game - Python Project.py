#Rock Paper Scissors game

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        print("Please type something valid.")
        continue
    
    random_number = random.randint(0,2)
    # Rock is 0, paper is 1, scissors is 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("You Lost!")
        computer_wins += 1

print("You won", user_wins , "times.")
print("The computer won", computer_wins , "times.")
print("Goodbye!")


