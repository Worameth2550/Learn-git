print("welcome to this quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    while True:
        if playing.lower!=playing.isalpha:
            print("You can play next time")
            quit()
        
print("Let's play ")
count=0
#question 1
answer=input("what does cpu stand for?\nans.")
if answer.lower() =="central processing unit":
    print('Correct')
    count+=1
else:
    print('Incorrect')
    #question 2
answer=input("what does GPU stand for?\nans.")
if answer.lower() =="graphic processing unit":
    print('Correct')
    count+=1
else:
    print('Incorrect')
    #question 3
answer=input("what does RAM stand for?\nans.")
if answer.lower() =="random access memory":
    print('Correct')
    count+=1
else:
    print('Incorrect')
    #question 4
answer=input("what does PSU stand for?\nans.")
if answer.lower() =="power supply":
    print('Correct')
    count+=1
else:
    print('Incorrect')

print("you got all score "+ str(count) +" question correct\nans.")
if count==4:
    print("You do all perfect!!!")
else:
    print("Do it next time")
