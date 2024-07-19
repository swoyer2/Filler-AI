import pygame
from board import Board
from player import Player
import minmax
import pygame_widgets
from pygame_widgets.button import ButtonArray
import pygame.freetype

pygame.init()

# Toggle if you want the bots to fight each other
auto = False

# AI depth
DEPTH = 10

boardSize = 8
cellSize = 50
padding = 200
buttonSize = 60
score1 = 1
score2 = 1
evalScore = 0
selection = [0, 0]
tally = [0, 0, 0] # Player1, Player2, Tie
windowSize = boardSize * cellSize + 2 * padding
colors = [
    (242, 39, 113),
    (100, 70, 166),
    (68, 193, 242),
    (164, 217, 85),
    (242, 208, 39),
    (66, 64, 67)
]

pygame.font.init()
GAME_FONT = pygame.freetype.SysFont('Comic Sans MS', 30)

# Set up the display
screen = pygame.display.set_mode((windowSize, windowSize))
pygame.display.set_caption("Filler Engine")

# Initialize the game board and players
gameBoard = Board(boardSize)
gameBoard.buildBoard()

player1 = Player((boardSize - 2, 0))
player2 = Player((0, boardSize - 1))

player1.color = gameBoard.board[boardSize - 2][0]
player2.color = gameBoard.board[0][boardSize - 1]

# Function to draw the board
def draw_board():
    for row in range(boardSize-1):
        for col in range(boardSize):
            color = colors[gameBoard.board[row][col]]
            if selection == [col, row] and editing:
                pygame.draw.rect(screen, (0, 0, 0), (col * cellSize + padding, row * cellSize + padding, cellSize, cellSize))
                pygame.draw.rect(screen, color, (col * cellSize + padding + 5, row * cellSize + padding + 5, cellSize - 10, cellSize - 10))
            else:
                pygame.draw.rect(screen, color, (col * cellSize + padding, row * cellSize + padding, cellSize, cellSize))

    # # Score - Was not working, always 1 move behind, do not care to fix lol
    # GAME_FONT.render_to(screen, (300, 50), str(score1), colors[gameBoard.board[6][0]])
    # GAME_FONT.render_to(screen, (480, 50), str(score2), colors[gameBoard.board[0][7]])

    # Eval bar
    pygame.draw.rect(screen, colors[gameBoard.board[6][0]], (20, 150, 50, 450))
    if evalScore > 10:
        pygame.draw.rect(screen, colors[gameBoard.board[0][7]], (20, 150, 50, 450))
    elif evalScore < -10:
        pygame.draw.rect(screen, colors[gameBoard.board[0][7]], (20, 150, 50, 0))
    else:
        pygame.draw.rect(screen, colors[gameBoard.board[0][7]], (20, 150, 50, 225+22.5*evalScore))
    

# Draw buttons
buttonArray = ButtonArray(
    screen,  # Surface to place button array on
    220,  # X-coordinate
    650,  # Y-coordinate
    buttonSize * 6,  # Width
    buttonSize,  # Height
    (6, 1),  # Shape: 6 buttons wide, 1 buttons tall
    border=5,  # Distance between buttons and edge of array
    texts=('1', '2', '3', '4', '5', '6'),  # Sets the texts of each button
    inactiveColours=(colors[0], colors[1], colors[2], colors[3], colors[4], colors[5]),
    colour = (255, 255, 255),
    onClicks=(lambda: handle_player_input(1),
              lambda: handle_player_input(2),
              lambda: handle_player_input(3),
              lambda: handle_player_input(4),
              lambda: handle_player_input(5),
              lambda: handle_player_input(6))
)


# Function to handle player input
def handle_player_input(playerInput):
    global score1
    global score2
    global evalScore
    playerInput -= 1
    if playerInput != gameBoard.board[0][7] and playerInput != gameBoard.board[6][0]:
        player1.addPositionsWithColor(gameBoard, playerInput)
        
        draw_board()
        pygame.display.flip()


        minMaxClass = minmax.MinMax(gameBoard)
        best_path_colors, best_score = minMaxClass.evaluate_tree(gameBoard, DEPTH, 1)

        print(best_path_colors[0][2:])
        print(best_score)
        evalScore = best_score

        player2.addPositionsWithColor(gameBoard, best_path_colors[0][2])

        print("Player1: ", len(player1.positionsControlled), " Player2: ", len(player2.positionsControlled))
        score1 = str(len(player1.positionsControlled))
        score2 = str(len(player2.positionsControlled))
    else:
        print("Choose a valid color")
    
def handle_auto():
    global score1
    global score2
    global evalScore
    global tally
    minMaxClass = minmax.MinMax(gameBoard)
    best_path_colors1, best_score = minMaxClass.evaluate_tree(gameBoard, DEPTH, 0)
    player1.addPositionsWithColor(gameBoard, best_path_colors1[0][2])

    draw_board()
    pygame.display.flip()

    best_path_colors2, best_score = minMaxClass.evaluate_tree(gameBoard, DEPTH, 1)
    player2.addPositionsWithColor(gameBoard, best_path_colors2[0][2])
    evalScore = best_score

    positions = minMaxClass.findPlayerPositions(gameBoard.board)
    if len(positions[0]) > 23:
        tally[0] += 1
        restart()
    elif len(positions[1]) > 23:
        tally[1] += 1
        restart()
    elif len(positions[1]) == 23 and len(positions[0]) == 23:
        tally[2] += 1
        restart()

def restart():
    global gameBoard
    global player1
    global player2
    print(tally)
    gameBoard = Board(boardSize)
    gameBoard.buildBoard()

    player1 = Player((boardSize - 2, 0))
    player2 = Player((0, boardSize - 1))

    player1.color = gameBoard.board[boardSize - 2][0]
    player2.color = gameBoard.board[0][boardSize - 1]


# Main game loop
editing = False
running = True
while running and not auto:
    screen.fill((255, 255, 255))
    draw_board()
    events = pygame.event.get()
    pygame_widgets.update(events)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_e:
                if editing:
                    editing = False
                else:
                    editing = True
            elif event.key == pygame.K_LEFT and editing:
                if selection[0] > 0:
                    selection[0] -= 1
            elif event.key == pygame.K_RIGHT and editing:
                if selection[0] < 7:
                    selection[0] += 1
            elif event.key == pygame.K_UP and editing:
                if selection[1] > 0:
                    selection[1] -= 1
            elif event.key == pygame.K_DOWN and editing:
                if selection[1] < 6:
                    selection[1] += 1
            elif pygame.K_1 <= event.key <= pygame.K_6:
                if editing:
                    gameBoard.board[selection[1]][selection[0]] = event.key - pygame.K_0 - 1
                else:
                    playerInput = event.key - pygame.K_0
                    handle_player_input(playerInput)

    pygame.display.flip()

while running and auto:
    handle_auto()
    screen.fill((255, 255, 255))
    draw_board()

    pygame.display.flip()
pygame.quit()
