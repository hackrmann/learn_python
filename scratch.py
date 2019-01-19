def fun1():
    loc = 0
    def fun2():
        print("Hey")
        def fun3():
            nonlocal loc
            loc = 56
            print(f"fun 3 loc is{loc}")

fun1()
#fun1().fun2()
def kwargs(**dic):
    print(type(dic.items()))
    print(dic)
a = {
    "A":"a",
    # 1: True,
    # (2,3,4): "Hello",
    "LOPO": "POPO"
}
kwargs(hello="bye",cat="meow",dog="bark",Heather="Lmao")
kwargs(**a)
def all(a,b,c,*args,def1=56,def2=66,**kwargs):
    return [a,b,args,def1,def2,kwargs]
print(all(9,True,"uuu",loli="hen"))