from board import Board
from anytree import Node as AnyNode
import cProfile


class MinMax:
    def __init__(self, gameBoard) -> None:
        self.gameBoard = gameBoard

    def getAvailableMoves(self, color1, color2):
        moves = [0, 1, 2, 3, 4, 5]
        moves.remove(color1)
        moves.remove(color2)
        return moves

    def findPlayerPositions(self, board):
        player1 = set([(0, 7)])
        player2 = set([(6, 0)])

        def helper(playerPositions):
            toCheck = set(playerPositions)
            new_positions = set(playerPositions)

            while new_positions:
                next_positions = set()
                for pos in new_positions:
                    neighbors = {
                        (pos[0] - 1, pos[1]),
                        (pos[0] + 1, pos[1]),
                        (pos[0], pos[1] - 1),
                        (pos[0], pos[1] + 1)
                    }
                    for neighbor in neighbors:
                        if neighbor not in toCheck and 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0]):
                            if board[neighbor[0]][neighbor[1]] == board[pos[0]][pos[1]]:
                                next_positions.add(neighbor)
                toCheck.update(next_positions)
                new_positions = next_positions

            return list(toCheck)

        return helper(player1), helper(player2)

    def simulate(self, colors, player1, origBoard):
        board = origBoard.getBoardCopy()
        for color in colors[2:]:
            positions = self.findPlayerPositions(board)
            if player1:
                player1 = False
                for pos in positions[0]:
                    board[pos[0]][pos[1]] = color
            else:
                player1 = True
                for pos in positions[1]:
                    board[pos[0]][pos[1]] = color
        if player1:
            positions = self.findPlayerPositions(board)
            if len(positions[0]) > 28:
                return 100 + len(positions[0])
            elif len(positions[1]) > 28:
                return -100 -  len(positions[1])
            score = len(positions[0]) - len(positions[1])
            return score

    def generateTree(self, board, maxDepth, depth, a, b, maximizing_player):
        if depth == maxDepth:
            return None, self.simulate(board.colors, maximizing_player, self.gameBoard), [board.colors]

        best_path = None
        best_eval = float('-inf') if maximizing_player else float('inf')
        best_path_colors = None

        for move in self.getAvailableMoves(board.colors[-2], board.colors[-1]):
            newColors = board.colors.copy()
            newColors.append(move)
            child_node = AnyNode(name=f"{board.name}{move}", parent=board, colors=newColors)

            # Evaluate the child node using Minimax
            _, eval, path = self.generateTree(child_node, maxDepth, depth + 1, a, b, not maximizing_player)

            if maximizing_player:
                if eval > best_eval:
                    best_eval = eval
                    best_path = child_node
                    best_path_colors = path + [child_node.colors]
                    a = max(a, eval)
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_path = child_node
                    best_path_colors = path + [child_node.colors]
                    b = min(b, eval)

            if b <= a:
                break  # Alpha-beta pruning

        return best_path, best_eval, best_path_colors

    def evaluate_tree(self, board, maxDepth):
        root = AnyNode(name="Root", colors=[board.board[6][0], board.board[0][7]])
        best_path, best_score, best_path_colors = self.generateTree(root, maxDepth, 0, float('-inf'), float('inf'), True)
        return best_path_colors, best_score


# def main():
#     test = Board(8)
#     test.buildBoard()
#     testClass = MinMax(test)
#
#     print("Creating and Evaluating Tree")
#
#     # Evaluate the tree using Minimax to find the best score
#     best_path_colors, best_score = testClass.evaluate_tree(test, 12)
#     print(f"Best moves found using Minimax were: {best_path_colors[0][2:]} with score of: {best_score}")
#
#     test.printBoard()
#
# cProfile.run("main()")
