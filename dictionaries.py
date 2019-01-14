three = [[1,2,3],[4,5,6],[7,8,9]]
empty=[]
([[empty.append(xy) for xy in ele] for ele in three])
print(empty)
dict1 = {
    "ob1": 1,
    "ob2": 1,
    "ob3": 1,
    "ob4": 1,
    "ob5": 1,
    "ob6": 1,
    "ob7": 1,
    "ob8": 1,
    "ob9": 1,
    "ob10": 1,
    12: 45,
}
print(dict1.items())
for ke,val in dict1.items():
    print(ke,val)
if 1 in dict1.values():
    print(True,dict1.get("ob5"))
dict1.clear()           #Clears the dictionary
print(dict1)
dict1.clear()
dict1.fromkeys([1,2,3,4],"unknown")
print(dict1," boo")
print("hello")