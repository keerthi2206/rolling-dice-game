print('ROLLING DICE GAME!!')
import random

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    total = dice1 + dice2
    print(total)


    if total == 12:
        print('you won the game')
        break

    elif total == 7:
        print('you get another chance')

    else:
        print('You lost the game')
        break

print('Game over')
    
    
 

