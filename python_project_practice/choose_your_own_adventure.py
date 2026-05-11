name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer=input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)?\n ").lower()

if answer=="left":
    answer=input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across(swim/walk):\n ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.\n ")
    elif answer == "walk":
        print("You walk for many miles,ran out of water and you lost the game\n ")
    else:
        print("Not valid option. You lose.\n ")

elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?\n ").lower()
   
    if answer == "back":
        print("You go back and loose.\n ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?\n ")

        if answer=="yes":
            print("You talk to the stranger and they give you gold. You win !!!\n ")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not valid option. You lose.\n ")
    else:
        print("Not valid option. You lose.\n ")

else:
    print('Not a valid option. You lose.')
    
print("Thank you for playing")