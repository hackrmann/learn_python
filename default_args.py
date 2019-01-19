def add(x,y=100):
    return x+y
def sub(x,y=100):
    return x-y
def power(x,y=10):
    return x**y
def nothing(x,y="zoiks"):
    return f"The 2 numbers are {x} and {y}"
def operation(x,y,func=nothing):
    return func(x)
# def sub_dup(x=100,y):     This is illegal,"non-default argument follows default argument"
def add_dup(x=22,y=55,z=111):
    return x+y+z

print(operation(2,7))
print(operation(5,6,add))
print(operation(7,9,power))
print(add_dup(z=1))
print(add_dup(3,4,5))
print(add_dup(y=4,x=3,z=5))