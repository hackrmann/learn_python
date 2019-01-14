# Parameter Ordering:
# Parameters
# *args               Passes items in parenthesis as a tupule
# Default Parameters
# **kwargs            Passes items in parenthesis as a dictionary

#For unpacking tuples/lists, just use the * while passing the arguments in the function call. That will pass each element induvidually
import random
def coin_toss():
    """ DUCKUOMENTATION"""
    x=random.randint(0,1)
    if x==1:
        print("Heads!")
    else:
        print("Tails!")
    global meow
    print(meow)
meow = "HElo"
def fstring(name):
    return f"Your name is {name}"
coin_toss()
print(fstring("Thejus"))

def nest1():
    pop = "Hen"
    def nest2():
        def nest3():
            nonlocal pop
            print(pop)
        return nest3()
    return nest2()

nest1()
print(coin_toss.__doc__)
def add(a,b,c,d):
    print(a+b+c+d)
    return a+b+c+d
dict11 = dict(a=1,b=2,c=3,d=4)
print(add(**dict11))