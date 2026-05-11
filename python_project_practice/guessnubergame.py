import random

top_of_range=input("Type a range of number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('Please type number larger than 0 next time')
        quit()
else:
    print('Please type a number next time')
    quit()
random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess = input("Make a guess:")
    
    if user_guess.lstrip("-").isdigit():
        if int(user_guess)<= 0 :
            print('Please type number larger than 0 next time')
            continue
    
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please type a number next time')
        continue
    
    if user_guess>top_of_range:
        print("Please type number in the range")
    elif user_guess == random_number:
        print("You got it!!")
        print("The number that correct is...",random_number)
        break
    elif user_guess > random_number and user_guess<= top_of_range:
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in",guesses,"guesses")