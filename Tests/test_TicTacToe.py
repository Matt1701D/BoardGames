import unittest
from TicTacToe import TicTacToeBoard

class Test_TicTacToe(unittest.TestCase):
    def test_BoardSize(self):
        #Arrange
        myBoardSize = 3

        #Act
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoardData = myBoard.GameBoard[0]
        myBoardLength = len(myBoardData)
        
        #Assert
        self.assertEqual(myBoardLength,myBoardSize)
        self.assertEqual(myBoardData,['_']*3)

    def test_BoardMoveValid(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')

        #Act        
        myBoard.makeMove("X",[0,0])
        
        #Assert
        self.assertEqual(myBoard.GameBoard[0],['X','_','_'])

    def test_BoardMoveInvalid(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])

        #Act        
        myBoard.makeMove("O",[0,0])
        
        #Assert
        self.assertEqual(myBoard.GameBoard[0],['X','_','_'])

    def test_BoardMoveWinHorizontal(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[0,1])

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[0,2])

    def test_BoardMoveWinVertical(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[1,0])

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,0])

    def test_BoardMoveWinDiagonalRight(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[1,1])

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,2])

    def test_BoardMoveWinDiagonalLeft(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,2])
        myBoard.makeMove("X",[1,1])

        #Act        
        result = myBoard.makeMoveWin()
        
        #Assert
        self.assertEqual(result,[2,0])

    def test_BoardGameWinHorizontal(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[0,1])
        myBoard.makeMove("X",[0,2])

        #Act        
        result = myBoard.checkWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinVertical(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[1,0])
        myBoard.makeMove("X",[2,0])

        #Act        
        result = myBoard.checkWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinDiagonalRight(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,0])
        myBoard.makeMove("X",[1,1])
        myBoard.makeMove("X",[2,2])

        #Act        
        result = myBoard.checkWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardGameWinDiagonalLeft(self):
        #Arrange
        myBoardSize = 3
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,2])
        myBoard.makeMove("X",[1,1])
        myBoard.makeMove("X",[2,0])

        #Act        
        result = myBoard.checkWinner()
        
        #Assert
        self.assertEqual(result,1)

    def test_BoardMoveCPUEasy(self):
        #Arrange
        myBoardSize = 3
        difficulty = 1
        turn = "X"
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,2])
        myBoard.makeMove("X",[1,1])

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        while(result == [2,0]):
            myBoard.GameBoard[2][0] = '_'
            result = myBoard.getMoveCPU(difficulty,turn)
        
        #Assert
        self.assertNotEqual(result,[2,0])

    def test_BoardMoveCPUHard2(self):
        #Arrange
        myBoardSize = 3
        difficulty = 3
        turn = "O"
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,2])

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        myBoard.makeMove(result[0],result[1],turn)
        
        #Assert
        self.assertEqual(myBoard.GameBoard[result[0]][result[1]],turn)

    def test_BoardMoveCPUHard(self):
        #Arrange
        myBoardSize = 3
        difficulty = 3
        turn = "X"
        myBoard = TicTacToeBoard.TicTacToeBoard(myBoardSize, '_')
        myBoard.makeMove("X",[0,2])
        myBoard.makeMove("X",[1,1])

        #Act        
        result = myBoard.getMoveCPU(difficulty,turn)
        
        #Assert
        self.assertEqual(result,[2,0])

if __name__ == '__main__':
    unittest.main()
