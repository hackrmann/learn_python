t = int(input())
for i in range(0,t):
    p1,p2,k = input().split()
    sum = int(p1) + int(p2)
    k = int(k)
    if (sum)/k==0:
        print("CHEF")
    else:
        if (2*(sum//(2*k))==(sum//(k))):
            print("CHEF")
        else:
            print("COOK") 