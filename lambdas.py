def square(num):    return num*num
def four(square):   return square*square
cube = lambda num: num**3
print(square(4)," ",cube(4))
print(four(square(4)))
oi = [1,2,3,4,5]
print(oi*2)
#Example of maps
mex = map(lambda op: op**3,oi)
print(list(mex))
print(list(mex))
les = ["lassie","colt","rusty"]
intended = list(map(lambda x: "Your instructor is "+x,filter(lambda le: len(le)<5,les)))
print(intended," ",les)