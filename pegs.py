from typing import List


def Boolean_Array_Convertion(Board):
    convertedBoard = []
    for x in Board:
        if x == 'X':
            convertedBoard.append(True)
        elif x == 'o':
            convertedBoard.append(False)
    return convertedBoard
   
def Take_New_Game_Board():
    newGame = input('Enter Starting Sequence')
    newBoard = Boolean_Array_Convertion(newGame)
    return newBoard

def Possible_Moves(currentGame):
    possibleMoves = list()
    for x in len(currentGame):
        if currentGame[x] == True:
            # If a pin exists in the current position
            if x <= 1:
                #If the pin is in a starting positon
                if currentGame[x+2] == True:
                    continue
                else:
                    move = [x, 'R']
                    possibleMoves.append(move)
            elif x >= (currentGame.count() - 1):
                #If the pin is in a ending positon
                if currentGame[x-2] == True:
                    continue
                else:
                    move = [x, 'L']
                    possibleMoves.append(move)
            else:
                #If the pin is in a middle position
                if currentGame[x+2] == True:
                    continue
                else:
                    move = [x, 'R']
                    possibleMoves.append(move)
                if currentGame[x-2] == True:
                    continue
                else:
                    move = [x, 'L']
                    possibleMoves.append(move)
        else:
            continue
    return possibleMoves





def pegsSolution(gameBoard):
    currentGame = []
    solutionPath = list()
    if gameBoard == None:
        currentGame = Take_New_Game_Board
    else:
        currentGame = Boolean_Array_Convertion(gameBoard)
    while True:
        possibleMoves = Possible_Moves(currentGame)
        if possibleMoves == None:
            solutionPath = None
            break
        else:
            if possibleMoves.count() == 1:


   
    return solutionPath


    
    
   

   







   



if __name__ == '__main__':
   gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
   print(pegsSolution(gameBoard))
