from board import Board
from player import Player
import minmax

boardSize = 8

gameBoard = Board(boardSize)

gameBoard.buildBoard()

player1 = Player((boardSize-1 ,0))
player2 = Player((0, boardSize-1))

player1.color = gameBoard.board[boardSize-1][0]
player2.color = gameBoard.board[0][boardSize-1]

while True:
    gameBoard.printBoard()
    playerInput = input()

    if playerInput == 'x':
        break

    if playerInput in {'0', '1', '2', '3', '4', '5'} and int(playerInput) != gameBoard.board[0][7]:
        player1.addPositionsWithColor(gameBoard, int(playerInput))
        
        minMaxClass = minmax.MinMax(gameBoard)

        best_path_colors, best_score = minMaxClass.evaluate_tree(gameBoard, 12)
        player2.addPositionsWithColor(gameBoard, best_path_colors[0][2])

        print("Player1: ", len(player1.positionsControlled), " Player2: ", len(player2.positionsControlled))
    else:
        print("Choose a valid color")

