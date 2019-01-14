def output(b,n,k):
    k = k - 1
    i = k
    count = 0
    for j in b:
        if j>= b[i]:
            count+=1
    print(count)
t = int(input())
for o in range(0,t):
    n, k = input().split(" ")
    n = int(n)
    k = int(k)
    arr = input().split(" ")
    arr.sort()
    b = list(reversed(arr))
    output(b,n,k)