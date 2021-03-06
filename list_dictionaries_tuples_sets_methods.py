list1 = [1,2,3]         #Comprehension:   []
set1 = {1,2,3}          #Comprehension    {}
tuple1 = (1,2,3)        #Comprehension    ()            Odd man out, values can't be changed
dictionary1 = dict(a=1,b=2)             #Comprehesion {}

# Example given for lists (By 3 I mean not tuple)
# .copy()           Common for all 3
# .clear()          Common for all 3 
# .remove()         Common for all 3, not dictionary

list1.append(4)
list1.clear()
list2 = list1.copy()
list1.extend([1,2,3,4])
list1.index(2)
list1.pop()
list1.pop(1)
list1.reverse()
list1.sort()
list1.remove(1)
list1.count(3)

set1.add(4)
set1.discard(3)     #Use instead of remove, it does not give an error
set1.update(set1)
set1.pop()
set1 | set1     #Union of 2 sets
set1 & set1     #Intersection of 2 sets

#Tuple is imutable, i.e it cannot be changed once declared
tuple1.count(2)
tuple1.index(1)

dictionary1.fromkeys([2,3,4],"Bye")
dictionary1.items()
dictionary1.keys()
dictionary1.values()
dictionary1.pop(keyvalue)
dictionary1.popitem()
dictionary1.update(dictionary1)
dictionary1.get("a")