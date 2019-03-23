import random
while True:
    user=input("Enter your move: ")
    pc=random.randint(0,2)
    if pc==0:
        print("computer's move: rock")
        if user=="rock":
            print("its a tie")
        elif user=="paper":
            print("you won")
        elif user=="scissor":
            print("you lost")
        else:
            print("invalid move")
    elif pc==1:
        print("computer's move: paper")
        if user=="paper":
            print("its a tie")
        elif user=="scissor":
            print("you won")
        elif user=="rock":
            print("you lost")
        else:
            print("invalid move")    
    elif pc==2:
        print("computer's move: scissor")
        if user=="scissor":
            print("its a tie")
        elif user=="rock":
            print("you won")
        elif user=="paper":
            print("you lost")
        else:
            print("invalid move")    