a = input("Enter player 1's choice: ")
b = input("Enter player 2's choice: ")
if a and b:
    if a=='rock':
        if b=='paper':
            print("player 2 wins")
        elif b=='scissors':
            print('player 1 wins')
        elif b=='rock':
            print('draw')
        else:
            print('invalid choice')
    elif a=='paper':
        if b=='paper':
            print("draw")
        elif b=='scissors':
            print('player 2 wins')
        elif b=='rock':
            print('player 1 wins')
        else:
            print('invalid choice')
    elif a=='scissors':
        if b=='paper':
            print("player 1 wins")
        elif b=='scissors':
            print('draw')
        elif b=='rock':
            print('player 2 wins')
        else:
            print('invalid choice')
    else:
        print('invalid choice')