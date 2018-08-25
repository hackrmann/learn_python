import random
#guessing game 
# a = random.randint(0,100)
# print("Let's play a guessing game! Enter a number from 1-100")
# b = int(input())
# while(a!=b):
#     if (a>b):
#         print("Too low!")
#     else:
#         print("Too high!")
#     b = int(input())
# print("Congratulations! You guessed right!")

#rock_paper_scissors advanced play against AI
a = input("Let's play rock paper scissors! Type n to quit!\nEnter your choice: ").lower()
c = ['rock','paper','scissors']
b = random.randint(0,2)
d = 0
e = 0
while True:
    print(f"Computer entered {c[b]}")
    if(a==c[b]):
        print("Draw!")
    elif (a==c[0] and b==1):
        print("Computer wins!")
        e = e + 1
    elif (a==c[1] and b==2):
        print("Computer wins!")
        e = e + 1
    elif(a==c[2] and b==0):
        print("Computer wins!")
        e = e + 1
    elif a==c[0] or a==c[1] or a==c[2]:
        print("Player wins")
        d = d + 1
    elif a=="n":
        break
    else:
        print("Invalid expression! Please give proper input")
    b = random.randint(0,2)
    a = input("Enter another: ")
print("Final Score\nYou:{}\nComputer:{}".format(d,e))