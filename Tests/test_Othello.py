import unittest, copy
from Othello.OthelloBoard import OthelloBoard

class Test_Othello(unittest.TestCase):
    def test_ValidVertDown(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[2][3] = "B"
        expBoard[3][3] = "B"
        expCnt = {"B":4,"W":1}

        #Act
        myBoard.makeMove("B",[2,3])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidVertUp(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[5][4] = "B"
        expBoard[4][4] = "B"
        expCnt = {"B":4,"W":1}

        #Act
        myBoard.makeMove("B",[5,4])
        actBoard = myBoard.GameBoard   
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidHoriztR(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[3][2] = "B"
        expBoard[3][3] = "B"
        expCnt = {"B":4,"W":1}

        #Act
        myBoard.makeMove("B",[3,2])
        actBoard = myBoard.GameBoard    
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidHorizL(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[4][5] = "B"
        expBoard[4][4] = "B"
        expCnt = {"B":4,"W":1}

        #Act
        myBoard.makeMove("B",[4,5])
        actBoard = myBoard.GameBoard   
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidDiagUpR(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[2][5] = "W"
        myBoard.PieceCount["W"] = 3
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[4][3] = "W"
        expBoard[3][4] = "W"
        expBoard[5][2] = "W"
        expCnt = {"B":0,"W":6}

        #Act
        myBoard.makeMove("W",[5,2])
        actBoard = myBoard.GameBoard   
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidDiagUpL(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[2][2] = "B"
        myBoard.PieceCount["B"] = 3
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[3][3] = "B"
        expBoard[4][4] = "B"
        expBoard[5][5] = "B"
        expCnt = {"B":6,"W":0}

        #Act
        myBoard.makeMove("B",[5,5])
        actBoard = myBoard.GameBoard   
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidDiagDnR(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[5][5] = "B"
        myBoard.PieceCount["B"] = 3
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[3][3] = "B"
        expBoard[4][4] = "B"
        expBoard[2][2] = "B"
        expCnt = {"B":6,"W":0}

        #Act
        myBoard.makeMove("B",[2,2])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidDiagDnL(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[5][2] = "W"
        myBoard.PieceCount["W"] = 3
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[4][3] = "W"
        expBoard[3][4] = "W"
        expBoard[2][5] = "W"
        expCnt = {"B":0,"W":6}

        #Act
        myBoard.makeMove("W",[2,5])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_MakeMoveInvalid(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)
        expCnt = {"B":2,"W":2}

        #Act
        myBoard.makeMove("B",[4,6])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "An invalid move made a move")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

if __name__ == '__main__':
    unittest.main()
