import unittest
from ChutesAndLadders.ChutesAndLaddersBoard import ChutesAndLaddersBoard

class Test_ChutesAndLadders(unittest.TestCase):

    #Test board size
    def test_BoardSize(self):
        #Arrange
        expBoardSize = 10        

        #Act
        myBoard = ChutesAndLaddersBoard(expBoardSize,'-',2)
        rowSize = len(myBoard.GameBoard)
        colSize = len(myBoard.GameBoard[1])

        #Assert
        self.assertEqual(expBoardSize,rowSize,"Row Size not "+str(expBoardSize))
        self.assertEqual(rowSize,colSize,"Row Size and Col Size not equal")

    #Test chutes and ladders board setup
    def test_BoardCandL(self):
        #Arrage
        expCandLCount = 19

        #Act
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        actCandLCount = len(myBoard.CandLmap)

        #Assert
        self.assertEqual(expCandLCount,actCandLCount,"CandLmap count is wrong")

    #Test players inital setup
    def test_Players(self):
        #Arrage
        playerNum = 2
        expPlayerLoc = {0: 0,1: 0}

        #Act
        myBoard = ChutesAndLaddersBoard(10,'-',playerNum)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player start point is wrong")

    #Test moving left to right on same line
    def test_MoveLeftToRight(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 5,1: 0}

        #Act
        myBoard.makeMove(0,5)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player initial move is wrong")
    
    #Test moving left to right and reach end of line
    def test_MoveLeftToRightUp(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 12,1: 0}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving left to right then up is wrong")
    
    #Test moving right to left on same line
    def test_MoveRightToLeft(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 18,1: 0}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving right to right is wrong")
    
    #Test moving right to left on same line
    def test_MoveRightToLeftUp(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 24,1: 0}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving right to right then up is wrong")

    #Test landing on chute top
    def test_Chute(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 6,1: 0}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,4)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player landing on chute is wrong")

    #Test landing on ladder bottom
    def test_Ladder(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expPlayerLoc = {0: 38,1: 0}

        #Act
        myBoard.makeMove(0,1)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player landing on ladder is wrong")   

    #Test winning game on exactly [0,0]
    def test_WinnerExact(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expWinner = 1

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,4)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,4)
        actWinner = myBoard.checkWinner(0)

        #Assert
        self.assertEqual(expWinner,actWinner,"Player landing on winning spot [0,0] is wrong")

    #Test winning game landing beyond winning spot
    def test_WinnerBeyond(self):
        #Arrage
        myBoard = ChutesAndLaddersBoard(10,'-',2)
        expWinner = 1

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,4)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actWinner = myBoard.checkWinner(0)

        #Assert
        self.assertEqual(expWinner,actWinner,"Player landing beyond winning spot [0,0] is wrong")

if __name__ == '__main__':
    unittest.main()
