demo_list = [1,"2",True,"Hello mortals!",44]
len(demo_list)                  #Gives the length of the list
list_of_nos = list(range(1,11)) #Makes list of numbers 1 to 10. Example of using list as a function

print(list_of_nos)
print(str(list_of_nos)[0])
print(demo_list[-1])
string_list = list(demo_list[3])
print(string_list)

if "2" in demo_list:
    print("The 'is' keyword in python checks if an object is in the list")
if "H" in demo_list[3]:
    print("Characters can be used by if keyword as if string is a list")
    
for i in demo_list:                 #i takes the values of all variables in the list
    print(i,end=" ")
print()

list_of_nos.sort()                  #Sorts the list. It's a list METHOD
list_of_nos.append(11)              #appends a number to the end of the list
list_of_nos.extend([12,13,14])        #Can pass n arguments to the end of the list, but as an array    
list_of_nos.insert(0,0)             #Inserts 'object' as index 'i' as list.insert(i,object)
print(list_of_nos)

demo_list.clear()                   #Clears the list of all elements
demo_list.extend([1,2,3,4,5])
demo_list.pop()                     #Returns last element
demo_list.pop(1)                    # returns element at index 1
print(demo_list)
demo_list.remove(3)                 #Does not remove. Different from del
print(demo_list)

print(list_of_nos.index(4))         #Return the index of 4 in the list "list_of_nos"
print(list_of_nos.index(4,1))       #Returns the index of 4 after the index of 1 (inclusive of 1)
demo_list.extend([5,6,9,7,411])
print(demo_list.index(5,0,3))       #Does not return index 3
dum = str(list_of_nos)
print(dum[5])                       #Returns a ,
print(list_of_nos.reverse())
print(list_of_nos)
new_st = '-'.join(list_of_nos)