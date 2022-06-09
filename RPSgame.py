import random
game = ['R','P','S']
userOpt = 'R'
compOpt= 'R'
while (userOpt == compOpt):
    print ()
    print('Rock-Paper-Scissors')
    print('use the following input methods for selection')
    print('input R for Rock')
    print('input P for Paper')
    print('input S for Scissors')
    print()

    userOpt = input('pick a game option: ')
    userOpt = userOpt.upper()

    if userOpt in game:

        compOpt = random.choice(game)

        if (compOpt=='R' and userOpt=='S'):
            print("computer wins")

        elif (compOpt=='P' and userOpt=='R'):
            print("computer wins")

        elif (compOpt=='S' and userOpt=='P'):
            print("computer wins")

        elif (compOpt == userOpt):
            print("TIE")

        else:
            print("YOU WIN")

    else:
        userOpt = 'R'
        print()
        print("Invalid Input")
        print("Pick a Valid Selection")

else:
    print ("Thank you for playing")
