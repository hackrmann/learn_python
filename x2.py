t = int(input())
for o in range(0,t):
    c=[]
    n = int(input())
    d = input().split()
    for dd in d:
        c.append(int(dd))
    #d.append(c.pop(0))
    days = 0
    ind =0
    sum = c[ind]
    ind+=1
    prev = sum
    while len(c)!=ind :
        days = days + 1
        for i in range(0,prev):
            if(ind==len(c)):
                break
            sum = sum + c[ind]
            ind+=1
        prev = sum
    print(days)