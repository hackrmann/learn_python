age = input("Please enter an age: ")
if age:
    age = int(age)
    if age<18:
        print("Can't enter")
    #elif age>=18:
    else:
        if age<21:
            print("Can enter but need wristband")
        else:
            print("Good to go!")
else:
    print("Please enter age!")