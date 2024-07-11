import unittest
import board

class Test(unittest.TestCase):

    def test_setColor(self):
        testBoard = board.Board(3)
        testBoard.setColor((0, 0))
        testBoard.setColor((1, 1))
        self.assertIsInstance(testBoard.board, list)
    
    def test_checkAvailable_any(self):
        testBoard = board.Board(3)
        colors = testBoard.checkAvailable((0,0))
        self.assertEqual(colors, [0, 1, 2, 3, 4, 5])

    def test_checkAvailable_1_0(self):
        testBoard = board.Board(3)
        testBoard.setColor((0, 0))
        colors = testBoard.checkAvailable((1,0))
        self.assertIsInstance(colors, list)

    def test_buildBoard(self):
        testBoard = board.Board(5)
        testBoard.buildBoard()

if __name__ == '__main__':
    unittest.main()