class gameBoard():
    def __init__(self, gameString):
        self.gameString = gameString

    def __repr__(self):
        return self.gameString

    def __len__(self, boardPositions):
        return len(self.gameStringArray)

def pegsSolution(newGameBoard=None):
    if newGameBoard is None:
        newGameBoard = input("Enter Game String: ")
        newGame = gameBoard(newGameBoard)
    else:
        newGame = gameBoard(newGameBoard)


    
if __name__ == '__main__':
   gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
   pegsSolution()