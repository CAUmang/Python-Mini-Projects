name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it  has come to  an end and  you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around  it or swim accross? Type 'walk' to walk and 'swim' to swim accross: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose the game.")
    elif answer == "cross":
        answer = input("You cross the bridg and meet a stranger.  Do you want to talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")
 
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thanyou for trying", name)
