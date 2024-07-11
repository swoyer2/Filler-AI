from random import choice
import copy

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]
        self.colors = None
    
    def printBoard(self):
        for row in self.board:
            print(row)
        print('\n')
    
    def getBoard(self):
        return self.board
    
    def setColor(self, pos):
        self.board[pos[0]][pos[1]] = choice(self.checkAvailable(pos))
    
    def checkAvailable(self, pos):
        availableColors = [0, 1, 2, 3, 4, 5]
        colorsToRemove = set()
        # Check the cell to the left
        if pos[0] > 0 and self.board[pos[0] - 1][pos[1]] is not None:
            colorsToRemove.add(self.board[pos[0] - 1][pos[1]])
        
        # Check the cell above
        if pos[1] > 0 and self.board[pos[0]][pos[1] - 1] is not None:
            colorsToRemove.add(self.board[pos[0]][pos[1] - 1])

        output = [ele for ele in availableColors if ele not in colorsToRemove]
        
        return output
    
    def buildBoard(self):
        for y in range(self.size):
            for x in range(self.size):
                self.setColor((x,y))

    def getBoardCopy(self):
        return copy.deepcopy(self.board)