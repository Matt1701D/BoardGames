import unittest, copy
from Othello.OthelloBoard import OthelloBoard

class Test_Othello(unittest.TestCase):
    def test_ValidVertDown(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[2][3] = "B"
        expBoard[3][3] = "B"
        expCnt = {"B":4,"W":1,"_":59}

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
        expCnt = {"B":4,"W":1,"_":59}

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
        expCnt = {"B":4,"W":1,"_":59}

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
        expCnt = {"B":4,"W":1,"_":59}

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
        myBoard.PieceCount["_"] = 59
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[4][3] = "W"
        expBoard[3][4] = "W"
        expBoard[5][2] = "W"
        expCnt = {"B":0,"W":6,"_":58}

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
        myBoard.PieceCount["_"] = 59
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[3][3] = "B"
        expBoard[4][4] = "B"
        expBoard[5][5] = "B"
        expCnt = {"B":6,"W":0,"_":58}

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
        myBoard.PieceCount["_"] = 59
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[3][3] = "B"
        expBoard[4][4] = "B"
        expBoard[2][2] = "B"
        expCnt = {"B":6,"W":0,"_":58}

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
        myBoard.PieceCount["_"] = 59
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[4][3] = "W"
        expBoard[3][4] = "W"
        expBoard[2][5] = "W"
        expCnt = {"B":0,"W":6,"_":58}

        #Act
        myBoard.makeMove("W",[2,5])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_ValidFourDir(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[0] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[1] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[2] = ["_","_","_","_","_","W","_","_"]
        myBoard.GameBoard[3] = ["W","_","W","W","B","_","_","_"]
        myBoard.GameBoard[4] = ["_","B","B","B","W","_","_","_"]
        myBoard.GameBoard[5] = ["W","B","_","B","W","_","_","_"]
        myBoard.GameBoard[6] = ["_","B","B","B","_","_","_","_"]
        myBoard.GameBoard[7] = ["W","_","W","_","W","_","_","_"]
        myBoard.PieceCount["W"] = 10
        myBoard.PieceCount["B"] = 9
        myBoard.PieceCount["_"] = 45
        expBoard = copy.deepcopy(myBoard.GameBoard)

        expBoard[0] = ["_","_","_","_","_","_","_","_"]
        expBoard[1] = ["_","_","_","_","_","_","_","_"]
        expBoard[2] = ["_","_","_","_","_","W","_","_"]
        expBoard[3] = ["W","_","W","W","W","_","_","_"]
        expBoard[4] = ["_","W","W","W","W","_","_","_"]
        expBoard[5] = ["W","W","W","W","W","_","_","_"]
        expBoard[6] = ["_","W","W","W","_","_","_","_"]
        expBoard[7] = ["W","_","W","_","W","_","_","_"]
        expCnt = {"B":0,"W":20,"_":44}

        #Act
        myBoard.makeMove("W",[5,2])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "Invalid board")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_MakeMoveInvalid(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        expBoard = copy.deepcopy(myBoard.GameBoard)
        expCnt = {"B":2,"W":2,"_":60}

        #Act
        myBoard.makeMove("B",[5,3])
        actBoard = myBoard.GameBoard  
        actCnt = myBoard.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "An invalid move made a move")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_Winner(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[0] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[1] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[2] = ["_","_","_","_","_","W","_","_"]
        myBoard.GameBoard[3] = ["W","_","W","W","B","_","_","_"]
        myBoard.GameBoard[4] = ["_","B","B","B","W","_","_","_"]
        myBoard.GameBoard[5] = ["W","B","_","B","W","_","_","_"]
        myBoard.GameBoard[6] = ["_","B","B","B","_","_","_","_"]
        myBoard.GameBoard[7] = ["W","_","W","_","W","_","_","_"]
        myBoard.PieceCount["W"] = 10
        myBoard.PieceCount["B"] = 9
        expWinner = 1

        #Act
        myBoard.makeMove("W",[5,2])
        actWinner = myBoard.checkWinner()

        #Assert
        self.assertEqual(expWinner, actWinner)

    def test_GameEnd(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        #myBoard.GameBoard = [["B"]*8 for x in range(0,4)]
        #myBoard.GameBoard.extend([["W"]*8 for x in range(0,4)])
        myBoard.PieceCount["_"] = 0
        myBoard.PieceCount["W"] = 32
        myBoard.PieceCount["B"] = 32
        expWinner = 2

        #Act
        #myBoard.makeMove("W",[5,2])
        actWinner = myBoard.checkWinner()

        #Assert
        self.assertEqual(expWinner, actWinner)
        
if __name__ == '__main__':

    unittest.main()
