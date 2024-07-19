from board import Board

class Player:
    def __init__(self, startingPos: tuple[int, int]) -> None:
        self.positionsControlled: list[tuple[int, int]] = [startingPos]
        self.touching: list[tuple[int, int]] = []
        self.color: int | None = None

    def findPlayerPositions(self, board: Board) -> list[tuple[int, int]]:
        toCheck: list[tuple[int, int]] = []
        for i in range(len(board.board[0])-1):
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

    def addPositionsWithColor(self, board: Board, color) -> Board:
        for pos in self.findPlayerPositions(board):
            board.board[pos[0]][pos[1]] = color

        return board

    def findTouching(self, boardSize: int) -> None:
        for pos in self.positionsControlled:
            if pos[0] > 0:
                self.touching.append((pos[0]-1, pos[1]))
            if pos[0] < boardSize - 1:
                self.touching.append((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                self.touching.append((pos[0], pos[1] - 1))
            if pos[1] < boardSize - 1:
                self.touching.append((pos[0], pos[1] + 1))

    def getScore(self) -> int:
        return len(self.positionsControlled)
