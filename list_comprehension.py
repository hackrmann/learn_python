def func(p):
    p = p*10
    return p
hey = ["meow","bow"]
hey2="hello".join(hey)
print(hey2)
for i in range(1,21,2):
    print(i,end=" ")
print()
dr = range(1,20)
x=[]
print(range(1,20),dr)
for i in dr:
    print(i,end=" ")
    x.append(i)
print()
print(dr,x)
x2 = [func(p) for p in x]
print(x2)
print(x)
alph = ['a','b','c',[],'d','e']
alph2 = [abc for abc in alph if (bool(abc)==True)]
print(alph2)
print(bool(alph[3]))
alph3 = [abc if bool(abc)==False else abc for abc in alph ]
print(alph3)