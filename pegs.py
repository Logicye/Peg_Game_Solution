from typing import List
from os import system as sys
from time import sleep as slp
from random import randint as rng
   
def Clear_Terminal():
    sys('cls')

def Take_New_Game_Board():
    newBoard = None
    while Check_Game_Valid(newBoard) == False:
        newBoard = input("Enter new game string: \n\n\t")
        if Check_Game_Valid(newBoard) == False:
            print("\n\tPlease ensure the game string is at least 3 characters in length \n\tand all character are either \"X's\" or \"o's\" (case sensitive).\n")
            slp(7.25)
    return newBoard

def Generate_Random_Problem(problemLength):
    newGame = ""
    for i in range(int(problemLength)):
        a = rng(0,1)
        if a == 1:
            newGame +='X'
        elif a == 0:
            newGame +='o'
    return newGame

def Check_Game_Valid(gameInput):
    allowedInput = "Xo"
    if gameInput is None:
        return False
    if len(gameInput) < 3:
        return False
    for i in gameInput:
        if i in allowedInput:
            pass
        else:
            return False
    return True
    


def Possible_Moves(currentGame):
    possibleMoves = list()
    for i in range(len(currentGame)):
        if currentGame[i] == 'X':
            # If a pin exists in the current position
            if i <= 1:
                #If the pin is in a starting positon
                if currentGame[i+2] == 'X':
                    pass
                else:
                    move = [i, 'R']
                    possibleMoves.append(move)
            elif i >= (len(currentGame) - 2):
                #If the pin is in a ending positon
                if currentGame[i-2] == 'X':
                    pass
                else:
                    move = [i, 'L']
                    possibleMoves.append(move)
            else:
                #If the pin is in a middle position
                if currentGame[i+2] == 'X':
                    pass
                else:
                    move = [i, 'R']
                    possibleMoves.append(move)
                if currentGame[i-2] == 'X':
                    pass
                else:
                    move = [i, 'L']
                    possibleMoves.append(move)
        else:
            continue
    return possibleMoves





def pegsSolution(gameBoard=None):
    solutionPath = list()
    newGame = gameBoard
    if Check_Game_Valid(gameBoard) == False:
        if input("Would you like to generate new puzzle (y/n)?\n\n") == ('y' or 'Y'):
            print()
            problemLength = 0
            while problemLength<3:
                problemLength = int(input("How long should the problem be?\n\n"))
            newGame = Generate_Random_Problem(problemLength)
        else:
            newGame = Take_New_Game_Board()
    print()
    print(newGame)
    print()

    while newGame.count('X') > 1 or newGame.count('X') == len(newGame):
        currentlyAvailableMoves = Possible_Moves(newGame)
        for i in currentlyAvailableMoves:
            print(i)
        break
    
    return solutionPath






if __name__ == '__main__':
   gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
   pegsSolution(gameBoard)
