# 4. Make a program that randomly chooses a number to guess and then the user will have a few chances to guess the number correctly.
# In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.

import random
a = int(input("Guess a number between 0 and 100\n"))
b = random.randint(0, 100)
while True:
    if a == b:
        print("You are correct")
        break
    elif a > b:
        print("The number is less than", a)
        a = int(input())
    else:
        print("The number is greater than", a)
        a = int(input())

            
