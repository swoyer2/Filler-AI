from board import Board
from anytree import Node as AnyNode, RenderTree
import copy

def getAvailableMoves(board):
    moves = [0,1,2,3,4,5]
    moves.remove(board[7][0])
    moves.remove(board[0][7])
    return moves

def findPlayerPositions(board):
    player1 = [(7,0)]
    player2 = [(0,7)]

    def helper(playerPositions):
        toCheck = []
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] == board[playerPositions[0][0]][playerPositions[0][1]]:
                    toCheck.append((i,j))
        for ele in toCheck:
            relatives = {(ele[0]-1, ele[1]), (ele[0]+1, ele[1]), (ele[0], ele[1]-1), (ele[0], ele[1]+1)}
            for potenRelative in toCheck:
                if potenRelative in relatives:
                    if ele not in playerPositions:
                        playerPositions.append(ele)
        return playerPositions

    return helper(player1), helper(player2)

def simulate(colors, player1, board):
    try:
        for color in colors:
            if player1:
                player1 = False
                for pos in findPlayerPositions(board)[0]:
                    board[pos[0]][pos[1]] = color
            else:
                player1 = True
                for pos in findPlayerPositions(board)[1]:
                    board[pos[0]][pos[1]] = color
        if player1:
            return len(findPlayerPositions(board)[0])
        else:
            return len(findPlayerPositions(board)[1])
    except:
        if player1:
                player1 = False
                for pos in findPlayerPositions(board)[0]:
                    board[pos[0]][pos[1]] = colors
        else:
            player1 = True
            for pos in findPlayerPositions(board)[1]:
                board[pos[0]][pos[1]] = colors
        if player1:
            return len(findPlayerPositions(board)[0])
        else:
            return len(findPlayerPositions(board)[1])

def expand_node(parent_node, player1):
    # Example logic to generate child nodes based on available moves
    children = []
    for move in [0, 1, 2, 3, 4, 5]:
        child_node = AnyNode(name=f"{parent_node.name + str(move)}", parent=parent_node, moveSeq=move)
        children.append(child_node)
    
    return children

def generateTree(board, maxDepth):
    depth = 0
    topNode = AnyNode(name="Top", board=board, score=0, colors=[board[0][7], board[7][0]])  # Initialize topNode with initial state (board, score)

    current_level = [topNode]  # Start with topNode at depth 0

    while depth < maxDepth:
        next_level_nodes = []

        for node in current_level:
            # Expand current node and add its children to next level nodes
            if depth % 2:
                children = expand_node(node, False)
            else:
                children = expand_node(node, True)
            node.children = children  # Link current node to its children
            next_level_nodes.extend(children)  # Add children to next level nodes list

        # Move to the next depth level
        current_level = next_level_nodes
        depth += 1

    # At this point, topNode will contain the root of the tree with its expanded children up to maxDepth
    # Example: Print the tree structure
    # for pre, _, node in RenderTree(topNode):
    #     print("%s%s Score: %s" % (pre, node.name, node.score))

    return topNode

def minMax(node, depth, a, b, maximizing_player, gameBoard):
    if depth == 0 or len(node.children) == 0:
        if maximizing_player:
            return [node.name], simulate(node.moveSeq, maximizing_player, gameBoard)
        else:
            return [node.name], simulate(node.moveSeq, maximizing_player, gameBoard)
    
    if maximizing_player:
        maxEval = float('-inf')
        best_path = []
        for child in node.children:
            path, eval = minMax(child, depth - 1, a, b, False, gameBoard)
            if eval > b:
                break
            if eval > maxEval:
                best_path = [node.name] + path  # Prepend current node's name to the best path found
                maxEval = eval
        return best_path, maxEval
    else:
        minEval = float('inf')
        best_path = []
        for child in node.children:
            path, eval = minMax(child, depth - 1, a, b, True, gameBoard)
            if eval < a:
                break
            if eval < minEval:
                best_path = [node.moveSeq] + path  # Prepend current node's name to the best path found
                minEval = eval
        return best_path, minEval


def evaluate_tree(tree, maxDepth, gameBoard):
    root = tree.root
    best_score = minMax(root, maxDepth, float('-inf'), float('inf'), True, gameBoard)
    return best_score


gameBoard = Board(8)
gameBoard.buildBoard()

print("Creating Tree")
tree = generateTree(gameBoard.getBoardCopy(), 3)
print("Evaluating Tree")

# Evaluate the tree using Minimax to find the best score
best_score = evaluate_tree(tree, 3, gameBoard.getBoardCopy())
print(f"Best moves found using Minimax were: {best_score[0][-1][3:]} with score of: {best_score[1]}")

gameBoard.printBoard()
