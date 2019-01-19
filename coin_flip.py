# Parameter Ordering:
# Parameters
# *args               Passes items in parenthesis as a tupule
# Default Parameters
# **kwargs            Passes items in parenthesis as a dictionary

#For unpacking tuples/lists, just use the * while passing the arguments in the function call. That will pass each element induvidually

# Code that doesn't work
# total = 0
# def increment():
#     total+=1      #Does not work
#     return total  #Does not work either
# increment()       #Does not work because function is looking for a local variable
# Code that does work
# total = 0
# def increment():
#     global total
#     total+=1
#     return total
# increment()
import random
def coin_toss():
    """DUCKUOMENTATION\n\nThis is an example of documentation"""
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
print(nest1()," ","Hello")
print(coin_toss.__doc__)        #No graphs here
print([1,2,3].pop.__doc__)       # double underscore. It works
def add(a,b,c,d):
    print(a+b+c+d)
    return a+b+c+d
dict11 = dict(a=1,b=2,c=3,d=4)
print(add(**dict11))