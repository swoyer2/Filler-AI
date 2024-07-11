import copy
from collections import defaultdict

class Player:
    def __init__(self, startingPos) -> None:
        self.positionsControlled = [startingPos]
        self.touching = []
        self.color = None
    
    def findPlayerPositions(self, board):
        toCheck = []
        for i in range(len(board.board[0])):
            for j in range(len(board.board[0])):
                if board.board[i][j] == board.board[self.positionsControlled[0][0]][self.positionsControlled[0][1]]:
                    toCheck.append((i, j))
        for ele in toCheck:
            relatives = {(ele[0] - 1, ele[1]), (ele[0] + 1, ele[1]), (ele[0], ele[1] - 1), (ele[0], ele[1] + 1)}
            for potenRelative in toCheck:
                if potenRelative in relatives:
                    if ele not in self.positionsControlled:
                        self.positionsControlled.append(ele)
        return self.positionsControlled

    def addPositionsWithColor(self, board, color):
        for pos in self.findPlayerPositions(board):
            board.board[pos[0]][pos[1]] = color
        
        return board

    def findTouching(self, boardSize):
        for pos in self.positionsControlled:
            if pos[0] > 0:
                self.touching.append((pos[0]-1, pos[1]))
            if pos[0] < boardSize - 1:
                self.touching.append((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                self.touching.append((pos[0], pos[1] - 1))
            if pos[1] < boardSize - 1:
                self.touching.append((pos[0], pos[1] + 1))

    def getScore(self):
        return len(self.positionsControlled)
