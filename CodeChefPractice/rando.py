import random
x = random.randint(1,3)
print(x)
y = int(input())
while x==y:
    y = random.randint(1,3)
if (1==x and 2==y) or (2==x and 1==y):
    print(3)
elif (3==x and 2==y) or (2==x and 3==y):
    print(1)
elif (3==x and 1==y) or (1==x and 3==y):
    print(2)