# 2.  The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the user can
# play again and again to get a number from the dice until the user decides to quit the program.

import random
while True:
    a = input("Press x to roll a dice and y to quit\n")
    if a == 'x':
        b = random.randint(1, 6)
        print("Dice shows", b)
    elif a == 'y':
        break


