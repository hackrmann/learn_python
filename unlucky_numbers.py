for i in range(1,21):
    print(f"{i} is",end=" ")
    if(i==4 or i==13):
        print("UNLUCKY number")
    elif(i%2==0):
        print("even")
    elif(i%2!=0):
        print("odd")