import random
import time
# snake water gun game or rock paper scissors game

def gameWin(player1, player2):
    if (player1 == player2):
        return None
    elif (player1 == 'g'):
        if(player2 == 'w'):
            return True
        else:
            return False
    elif (player1 == 'w'):
        if(player2 == 'g'):
            return False
        else:
            return True
    else:
        if(player2 == 'w'):
            return False
        else:
            return True


# print("Computer's turn:")
comp = random.randint(1, 3)
if comp == 1:
    comp = 'g'
elif comp == 2:
    comp = 'w'
else:
    comp = 's'

you = input("Enter your input--> snake(s) water(w) or gun(g): ")
if you == 's':
    print("You chose Snake ")
elif you == 'w':
    print("You chose Water ")
else:
    print("You chose Gun")


if comp == 's':
    print("Computer chose Snake ")
elif comp == 'w':
    print("Computer chose Water ")
else:
    print("Computer chose Gun")



time.sleep(2)

if (gameWin(comp, you) == None):
    print("The game is a tie.")
elif(gameWin(comp, you)):
    print("You Won!!")
else:
    print("You Lost :(")