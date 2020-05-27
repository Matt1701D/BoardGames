from MyLogger.MyLogger import MyLogger      # Logger module
from Board import Board

class TicTacToeBoard(Board):

    # CONSTRUCTOR

    @MyLogger.log_decorator
    def __init__(self, boardSize, delimeter):
        """
        Create TicTacToe board of boardSize and populated with delimeter string
        """
        super().__init__(boardSize, delimeter)

        self.__turnsTaken = 0
        self.__gameBoardTranspose = []

        self._initBoard()

    # PROPERTIES

    @property
    def GameBoardT(self):
        return self.__gameBoardTranspose

    # PUBLIC METHODS

    # ensure move is valid
    @MyLogger.log_decorator
    def validateMove(self, turn, coord):
        """
        Ensure the move is valid for turn given a list of coord [Y,X]
        """
        Y = int(coord[0])
        X = int(coord[1])
        return self._gameBoard[Y][X] == self._delimeter

    # store turn in board and transposed board
    @MyLogger.log_decorator
    def makeMove(self, turn, coord):
        """
        Make the move for turn given a list of coord [Y,X]
        """
        if self.validateMove(turn, coord):
            self._updateBoard(turn, coord)
            self.__turnsTaken+=1

    # check for winner
    @MyLogger.log_decorator
    def checkWinner(self):
        """
        Check if the game is over (win or draw)
        """
        if self.__turnsTaken == self._boardSize * self._boardSize:
            return 2
        elif self.__checkGameWinner():
            return 1
        else:
            return 0
  
    # always have cpu pick coord to win or block a win
    @MyLogger.log_decorator
    def getBestMove(self):
        """
        Compute the best move by picking 1) a winning move 2) blocking a winning move. Returns coord [Y,X]
        """
        X = Y = self._boardSize
        XCountR = OCountR = BCountR = 0
        XCountL = OCountL = BCountL = 0

        for i in range(self._boardSize):
            #check horizontal
            if (self._gameBoard[i].count(self._delimeter) == 1 and (self._gameBoard[i].count('O') == self._boardSize - 1 or (self._gameBoard[i].count('X') == self._boardSize - 1))):
                Y = i
                X = self._gameBoard[i].index(self._delimeter)

            #check vertical
            if (self.__gameBoardTranspose[i].count(self._delimeter) == 1 and (self.__gameBoardTranspose[i].count('O') == self._boardSize - 1 or (self.__gameBoardTranspose[i].count('X') == self._boardSize - 1))):
                Y = self.__gameBoardTranspose[i].index(self._delimeter)
                X = i

            #check diagonal right
            if self._gameBoard[i][i] == 'X':
                XCountR += 1
            elif self._gameBoard[i][i] == 'O':
                OCountR += 1
            else:
                BlankR = [i, i]
                BCountR += 1

            #check diagonal left
            XCoord = self._boardSize - 1 - i
            if self._gameBoard[XCoord][i] == 'X':
                XCountL += 1
            elif self._gameBoard[XCoord][i] == 'O':
                OCountL += 1
            else:
                BlankL = [XCoord, i]
                BCountL += 1

        if BCountR == 1 and ((XCountR == self._boardSize - 1) or (OCountR == self._boardSize - 1)):
            Y = BlankR[0]
            X = BlankR[1]
        elif BCountL == 1 and ((XCountL == self._boardSize - 1) or (OCountL == self._boardSize - 1)):
            Y = BlankL[0]
            X = BlankL[1]

        return [Y,X]
        
    # PROTECTED METHODS

    #make transposed board to more quickly check for vertical moves and win
    @MyLogger.log_decorator
    def _initBoard(self):
        super()._initBoard()
        self.__gameBoardTranspose = [[self._delimeter] * self._boardSize for x in range(self._boardSize)]

    @MyLogger.log_decorator
    def _updateBoard(self, turn, coord, isNewPos=False):
        Y = int(coord[0])
        X = int(coord[1])
        self._gameBoard[Y][X] = turn
        self.__gameBoardTranspose[X][Y] = turn

    # PRIVATE METHODS

    # check for successfull tic tac toe
    @MyLogger.log_decorator
    def __checkGameWinner(self):
        sofarR = 1
        sofarL = 1
        sofarV = 1

        for i in range(self._boardSize):
            #check horizontal
            if (self._gameBoard[i] == ['X']*self._boardSize or self._gameBoard[i] == ['O']*self._boardSize):
                return 1

            #check vertical
            if (self.__gameBoardTranspose[i] == ['X']*self._boardSize or self.__gameBoardTranspose[i] == ['O']*self._boardSize):
                return 1

            #check diagonal right and left
            if sofarR and i != self._boardSize - 1:
                sofarR = (self._gameBoard[i][i] == self._gameBoard[i+1][i+1]) and (self._gameBoard[i][i] in ['X','O'])

            if sofarL and i != self._boardSize - 1:
                XCoord = self._boardSize - 1 - i
                sofarL = (self._gameBoard[XCoord][i] == self._gameBoard[XCoord-1][i+1]) and (self._gameBoard[XCoord][i] in ['X','O'])

        if sofarR or sofarL:
            return 1
        else:
            return 0

