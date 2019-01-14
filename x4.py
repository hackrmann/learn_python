def op(st,j,f):
    st[j-1]+= (1*f)
    st[j]+= (2*f)
    st[j+1]+= (3*f)
t = int(input())
for i in range(0,t):
    c = int(input())
    sum1=0
    sum2 = 0
    st = input().split(" ")
    dt = input().split(" ")
    for k in range(0,c):
        st[k] = int(st[k])
        dt[k] = int(dt[k])
        sum1+=st[k]
        sum2+=dt[k]
    if st==dt:
        print("TAK")
        continue
    # if c==1:
    #     if(st[0]-dt[0]== -1):
    #         print("TAK")
    #     else:
    #         print("NIE")
    #     continue
    # elif c==2:
    #     if(st[0]-dt[0]== -1 and st[1]-dt[1]== -2):
    #         print("TAK")
    #     else:
    #         print("NIE")
    #     continue
    if((dt[c - 1] - st[c - 1])%3!=0):
        print("NIE")
    else:
        if((sum2-sum1)%6==0):
            no_op = (sum2-sum1)//6
            flag = False
            for j in range(1,c-3):
                op(st,j,((dt[j-1]-st[j-1])))
                op(st,j+1,((dt[j]-st[j])//2))
                op(st,j+2,((dt[j+1]-st[j+1])//3))
            op(st,c-2,((dt[c-1]-st[c-1])//3))
            op(st,c-3,((dt[c-2]-st[c-2])//2))
            if st==dt:
                print("TAK")
            else:
                print("NIE") 
        else:
            print("NIE")
    st = dt =[]