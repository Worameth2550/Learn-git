import random

user_wins = 0
computer_wins=0
Draw=0

options=["rock","paper","scissors"]

while True:
    user_guess=input("Type Rock Paper or Scissors or Q to quit :").lower()
    if user_guess=="q":
        break

    if user_guess not in options:
        print("Please select in option")
        continue

    random_number=random.randint(0,2)
    #rock = 0 paper = 1 scissors = 2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")

    if user_guess =="rock" and computer_pick == "scissors":
        print("You won!")
        user_wins+=1
    elif user_guess =="paper" and computer_pick == "rock":
        print("You won!")
        user_wins+=1
    elif user_guess =="scissors" and computer_pick == "paper":
        print("You won!")
        user_wins+=1
    elif user_guess == computer_pick:
        print("Draw")
        Draw+=1
    else:
        print("You lost!")
        computer_wins+=1

print("you won",user_wins,"times.")
print("Draw",Draw,"times.")
print("computer won",computer_wins,"times.")
print("Goodbye!")