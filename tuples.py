t1 = (1,2,3,4,5)
t2 = ((1,2,3),("Hi, bye", "hiya"))
print(t2)
for t in t2:
    print(t)
x = {1,2}
x.add(45)
print(type(x)," ",x)