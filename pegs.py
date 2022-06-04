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


def Perform_Move(game, move):
    outputGame = ""
    print('--------------')
    print(game)
    print(move)
    print('--------------')
    if move[1] == 'R':
        outputGame = game[:move[0]]+'ooX'+game[(move[0]+3):]
    elif move[1] == 'L':
        outputGame = game[:(move[0]-2)]+'Xoo'+game[(move[0]+1):]
    return outputGame

def Undo_Move(previousGameState):
    return previousGameState

def Print_Game_Progression(gameStack):
    for i in gameStack:
        print(gameStack[i])


def pegsSolution(gameBoard=None):
    solutionPath = list()
    solutionStack = list()
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
    while newGame.count('X') > 1:
        slp(2)
        if newGame == solutionStack[len(solutionStack)-1][0] and len(solutionStack[len(solutionStack)-1][1]):
            pass
        else:
            currentlyAvailableMoves = Possible_Moves(newGame)
            solutionStack.append(newGame, currentlyAvailableMoves)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #print()
        #print(newGame)
        #currentlyAvailableMoves = Possible_Moves(newGame)
        #for i in currentlyAvailableMoves:
        #    print(i)
        #if len(currentlyAvailableMoves) == 1:
        #    solutionStack.append((newGame, currentlyAvailableMoves[0]))
        #    newGame = Perform_Move(newGame, currentlyAvailableMoves[0])
        #    #print(solutionStack)
        #    print(newGame)
        #elif len(currentlyAvailableMoves) == 0:
        #    print(newGame)
        #    newGame = Undo_Move(solutionStack[len(solutionStack)][0])
        #    print(newGame)
        #else:
        #    pass 
        #print(solutionStack)
        #print(solutionStack[0][1][1])

        #-----------------------------
        #-----Real-Solution-Start-----
        #-----------------------------------------------------------------------------------
        #currentlyAvailableMoves = Possible_Moves(newGame)
        #solutionStack.append((newGame, currentlyAvailableMoves))
        #if len(solutionStack[0][1]) == 1:
        #    solutionStack.append((newGame, None))
        #    newGame = Perform_Move(newGame, currentlyAvailableMoves[0])
        #    #print(solutionStack)
        #    print(newGame)
        #elif len(current):
        #    pass
        

        
        currentlyAvailableMoves = Possible_Moves(newGame)
        solutionStack()
        if newGame == solutionStack[len(solutionStack)-1][0]:
            Perform_Move()
            solutionStack.append((newGame, currentlyAvailableMoves))
            

        if len(currentlyAvailableMoves)>0:
            newGame = Perform_Move(currentlyAvailableMoves[0])
            solutionStack.append((newGame,))
        else:
            print(newGame)
            #Undo_Move(solutionStack[len(SolutionStack)-1][1][len(solutionStack)])
            #solutionStack[len(SolutionStack)-1][0]
            Undo_Move(solutionStack[len(SolutionStack)-1][0])
            print(newGame)
    print('You Won')
    slp(3)





        #-----------------------------------------------------------------------------------


    #for i in solutionStack:
    #    solutionPath.append(i[1])
    return solutionPath






if __name__ == '__main__':
   gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
   print(pegsSolution(gameBoard))
