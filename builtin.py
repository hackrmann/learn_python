iterable = (1,2,3,4,5)
iterable = [1,2,3,4,5]
iterable = dict([("abcd",1234),((1,2),"co-ordinates"),(True,"meh")])
char='a'
print(iterable)
print(ord(char))        #Get ASCII value of char 
print(chr(char))        #Show character of ASCII
print(any(iterable))    #Returns true if set is not empty or any ONE item in iterable give true
print(all(iterable))    #Returns True if set is empty or ALL items in iterable give truthy value