'''
Snake Water Gun
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
'''

import random

def winRes(a, b, c, res):
    if(compIndex == AnsMatrix[a][b]):
        print("You Won!!")
        res +=1
    elif(compIndex == AnsMatrix[a][c]):
        print("Computer Won!!")
        res -=1
    return res

res = 0
AnsMatrix = [0, 1, -1],[-1, 0, 1],[1, -1, 0]
compChoice = ("Snake", "Water", "Gun")
for i in range(5):
    userChoice = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun")) -2
    #invalid case
    if(userChoice > 1):
        print ("Wrong Input, Game over") 
        break
    else:
        comp = random.choice(compChoice)
        compIndex = -1 if(comp == "Snake") else 0 if(comp == "Water") else 1
        print(comp)
    #draw case
        if(userChoice == compIndex):
            print("Draw!!, Next Round!")
            #win cases
        else:
            if(userChoice == -1):
                winRes(0,0,1,res)
            elif(userChoice == 0):
                winRes(1,0,2,res)
            else:
                winRes(2,1,3,res)

print("You are winner!! Congratulations") if(res>0) else print ("It's a draw") if(res == 0) else print("Computer won, better luck next time")