import unittest, copy
from Othello.OthelloBoard import OthelloBoard
from Othello.Othello import Othello
from MyLogger.MyExceptions import *

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

        expBoard = []
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","_","_","_","_","W","_","_"])
        expBoard.append(["W","_","W","W","W","_","_","_"])
        expBoard.append(["_","W","W","W","W","_","_","_"])
        expBoard.append(["W","W","W","W","W","_","_","_"])
        expBoard.append(["_","W","W","W","_","_","_","_"])
        expBoard.append(["W","_","W","_","W","_","_","_"])
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
        myBoard.PieceCount["_"] = 45
        expWinner = "W"

        #Act
        myBoard.makeMove("W",[5,2])
        actWinner = myBoard.checkWinner()

        #Assert
        self.assertEqual(expWinner, actWinner)

    def test_Winner2(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.GameBoard[0] = ["B","B","B","B","B","B","W","W"]
        myBoard.GameBoard[1] = ["B","B","B","B","B","B","W","W"]
        myBoard.GameBoard[2] = ["B","W","B","B","B","B","W","W"]
        myBoard.GameBoard[3] = ["W","B","B","W","B","B","W","W"]
        myBoard.GameBoard[4] = ["W","W","W","W","B","B","W","W"]
        myBoard.GameBoard[5] = ["B","W","W","W","W","B","W","B"]
        myBoard.GameBoard[6] = ["B","B","W","W","W","W","B","_"]
        myBoard.GameBoard[7] = ["B","B","B","B","B","B","B","B"]
        myBoard.PieceCount["W"] = 25
        myBoard.PieceCount["B"] = 38
        myBoard.PieceCount["_"] = 1
        expWinner = "B"

        #Act
        myBoard.makeMove("W",[6,7])
        actWinner = myBoard.checkWinner()

        #Assert
        self.assertEqual(expWinner, actWinner)

    def test_GameEnd(self):
        #Arrange
        myBoard = OthelloBoard(8,"_")
        myBoard.PieceCount["W"] = 32
        myBoard.PieceCount["B"] = 32
        myBoard.PieceCount["_"] = 0
        expWinner = "D"

        #Act
        actWinner = myBoard.checkWinner()

        #Assert
        self.assertEqual(expWinner, actWinner)

    def test_CPUMove(self):
        self.maxDiff = None
        gameMode = 2

        #Arrange
        myOT = Othello(gameMode,True)
        myOT.turn = "W"
        myBoard = myOT.board
        myBoard.GameBoard[0] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[1] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[2] = ["_","_","B","_","B","_","_","_"]
        myBoard.GameBoard[3] = ["_","_","_","B","B","_","_","_"]
        myBoard.GameBoard[4] = ["_","_","B","B","W","W","_","_"]
        myBoard.GameBoard[5] = ["_","_","_","W","_","_","_","_"]
        myBoard.GameBoard[6] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[7] = ["_","_","_","_","_","_","_","_"]
        myBoard.PieceCount["_"] = 55
        myBoard.PieceCount["W"] = 3
        myBoard.PieceCount["B"] = 6

        expBoard = []
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","_","B","W","B","_","_","_"])
        expBoard.append(["_","_","_","W","W","_","_","_"])
        expBoard.append(["_","_","B","W","W","W","_","_"])
        expBoard.append(["_","_","_","W","_","_","_","_"])
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expCnt = {"B":3,"W":7,"_":54}

        #Act
        coord = myOT._getMoveCPU()
        myOT.board.makeMove(myOT.turn, coord)
        actBoard = myOT.board.GameBoard
        actCnt = myOT.board.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "An invalid move made a move")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_CPUMoveCorner(self):
        self.maxDiff = None

        #Arrange
        gameMode = 2
        myOT = Othello(gameMode, True)
        myOT.turn = "W"
        myBoard = myOT.board
        myBoard.GameBoard[0] = ["_","_","_","_","_","_","_","_"]
        myBoard.GameBoard[1] = ["_","B","_","_","_","_","_","_"]
        myBoard.GameBoard[2] = ["_","_","B","_","B","W","_","_"]
        myBoard.GameBoard[3] = ["_","_","_","W","B","_","_","_"]
        myBoard.GameBoard[4] = ["_","B","B","B","B","B","W","_"]
        myBoard.GameBoard[5] = ["_","_","B","W","_","_","_","_"]
        myBoard.GameBoard[6] = ["_","B","_","_","_","_","_","_"]
        myBoard.GameBoard[7] = ["_","_","_","_","_","_","_","_"]
        myBoard.PieceCount["_"] = 50
        myBoard.PieceCount["W"] = 3
        myBoard.PieceCount["B"] = 11

        expBoard = []
        expBoard.append(["_","_","_","_","_","_","_","_"])
        expBoard.append(["_","B","_","_","_","_","_","_"])
        expBoard.append(["_","_","B","_","B","W","_","_"])
        expBoard.append(["_","_","_","W","W","_","_","_"])
        expBoard.append(["_","B","B","W","B","B","W","_"])
        expBoard.append(["_","_","W","W","_","_","_","_"])
        expBoard.append(["_","W","_","_","_","_","_","_"])
        expBoard.append(["W","_","_","_","_","_","_","_"])
        expCnt = {"B":7,"W":8,"_":49}

        #Act
        coord = myOT._getMoveCPU()
        myOT.board.makeMove(myOT.turn, coord)
        actBoard = myOT.board.GameBoard
        actCnt = myOT.board.PieceCount

        #Assert
        self.assertEqual(expBoard, actBoard, "An invalid move made a move")
        self.assertEqual(expCnt, actCnt, "Invalid piece count")

    def test_Params(self):
        #Arrange
        gameMode = 3

        #Act
        #Assert
        with(self.assertRaises(InvalidParameterException)):
            myOT = Othello(gameMode, True)
        
if __name__ == '__main__':

    unittest.main()
