n = input("Enter number of lines of emoji: ")
n = int(n)
for i in range(1,n+1):
    for j in range(1,i+1):
        print('\U0001f600',end="")
    print("")