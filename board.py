from random import choice
import copy

class Board:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.board: list[list[int]] = [[-1] * (size) for _ in range(size-1)]
        self.colors: list[int] | None = None

    def printBoard(self) -> None:
        for row in self.board:
            print(row)
        print('\n')

    def getBoard(self) -> list[list[int]]:
        return self.board

    def setColor(self, pos: tuple[int, int]) -> None:
        if pos == (6, 0):
           avaliableColors: list[int] = self.checkAvailable(pos)
           if self.board[0][7] in avaliableColors:
               avaliableColors.remove(self.board[0][7])
           self.board[pos[0]][pos[1]] = choice(avaliableColors)
        else:
            self.board[pos[0]][pos[1]] = choice(self.checkAvailable(pos))

    def checkAvailable(self, pos : tuple[int, int]) -> list[int]:
        availableColors: list[int] = [0, 1, 2, 3, 4, 5]
        colorsToRemove: set[int] = set()
        # Check the cell to the left
        if pos[0] > 0:
            colorsToRemove.add(self.board[pos[0] - 1][pos[1]])

        # Check the cell above
        if pos[1] > 0:
            colorsToRemove.add(self.board[pos[0]][pos[1] - 1])

        output: list[int] = [ele for ele in availableColors if ele not in colorsToRemove]

        return output

    def buildBoard(self) -> None:
        for y in range(self.size):
            for x in range(self.size-1):
                self.setColor((x,y))

    def getBoardCopy(self) -> list[list[int]]:
        return copy.deepcopy(self.board)
