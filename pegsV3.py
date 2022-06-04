from typing import List
from os import system as sys
from time import sleep as slp
from random import randint as rng

class Node:
    def __init__(self,nodeId,parentNodeId,boardPositions,moveToAchieve):
        self.nodeId = nodeId
        self.parentNodeId = parentNodeId
        self.boardPositions = boardPositions
        self.moveToAchieve = moveToAchieve

    def Is_Node_Repeat(self):
        if (node+(node + self.parentNodeId).parentNodeId).boardPositions == self.boardPostions:
            pass


class Node_Handler():
    numberOfNodes = 0
    nodeReg = list()


    @classmethod
    def New_Problem(cls,startingBoard):
        cls.numberOfNodes = 0
        nodeReg = list()
        cls.New_Node(startingBoard, cls.numberOfNodes)

    @classmethod
    def Check_Win(cls, currentBoard):
        if currentBoard.boardPositions.count('X') > 1:
            return False
        else:
            return True

    @staticmethod
    def Next_Board_States(current):
        pass


    @classmethod
    def New_Node(cls,boardPositions,parentNodeId = None,moveToAchieve = None):
        if parentNodeId == None:
            parentNodeId = cls.numberOfNodes-1
        nodeName = "node"+str(cls.numberOfNodes)
        nodeName = Node(cls.numberOfNodes,parentNodeId,boardPositions,moveToAchieve)
        cls.nodeReg.append(nodeName)
        cls.numberOfNodes += 1

    @classmethod
    def List_All_Nodes(cls):
        print()
        for i in cls.nodeReg:
            print()
            print(i.nodeId)
            print(i.boardPositions)
            print(i.moveToAchieve)
            print(i.parentNodeId)
            print()
        print()
        return cls.nodeReg

    @classmethod
    def Current_Node(cls):
        return cls.nodeReg[-1]

    @classmethod
    def Find_Next_Node(cls):
        if 

  


def Take_New_Game_Board():
    newBoard = None
    while Check_Game_Valid(newBoard) == False:
        newBoard = input("Enter new game string: \n\n\t")
        if Check_Game_Valid(newBoard) == False:
            print("\n\tPlease ensure the game string is at least 3 characters in length \n\tand all character are either \"X's\" or \"o's\" (case sensitive).\n")
            slp(3)
            newBoard = None
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
    if gameInput is None or len(gameInput) < 3:
        return False
    elif gameInput.count('X') == len(gameInput):
        print("\n\tGame board input has no solution: " + str(gameInput))
        return False
    else:
        for i in gameInput:
            if i in allowedInput:
                pass
            else:
                return False
    return True

def pegsSolution(game):
    if game == None:
        pass


Node_Handler.New_Problem(Take_New_Game_Board())
while Node_Handler.Check_Win(Node_Handler.Current_Node()) == False:
    print("problem not solved")
print('problem solved')
slp(2)
