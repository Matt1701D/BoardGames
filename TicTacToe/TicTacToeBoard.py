from Board import Board

class TicTacToeBoard(Board):

    def __init__(self, boardSize, delimeter):
        self.__turnsTaken = 0
        self.__gameBoardTranspose = []

        super().__init__(boardSize, delimeter)

        self._initBoard()

    # PROPERTIES

    @property
    def GameBoardT(self):
        return self.__gameBoardTranspose

    # PUBLIC METHODS

    # ensure move is valid
    def validateMove(self, turn, coord):
        Y = int(coord[0])
        X = int(coord[1])
        return self._gameBoard[Y][X] == self._delimeter

    # store turn in board and transposed board
    def makeMove(self, turn, coord):
        if self.validateMove(turn, coord):
            self._updateBoard(coord, turn)
            self.__turnsTaken+=1

    # check for winner
    def checkWinner(self):
        if self.__turnsTaken == self._boardSize * self._boardSize:
            return 2
        elif self.__checkGameWinner():
            return 1
        else:
            return 0
        
    # PROTECTED METHODS

    #make transposed board to more quickly check for vertical moves and win
    def _initBoard(self):
        super()._initBoard(1)
        self.__gameBoardTranspose = [[self._delimeter] * self._boardSize for x in range(self._boardSize)]

    def _updateBoard(self, coord, turn, isNewPos=False):
        Y = int(coord[0])
        X = int(coord[1])
        self._gameBoard[Y][X] = turn
        self.__gameBoardTranspose[X][Y] = turn

    # PRIVATE METHODS

    # check for successfull tic tac toe
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
