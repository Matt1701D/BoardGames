from Board import Board

class OthelloBoard(Board):

    def __init__(self, boardSize, delimeter):
        super().__init__(boardSize, delimeter)

        self.__pieceCount = {"B":2,"W":2,str(self._delimeter):(self._boardSize**2)-4}
        self.__tmpMove = []

        dirCoord = [-1,0,1]
        self.__dirList = [[x,y] for x in dirCoord for y in dirCoord]
        self.__dirList.remove([0,0])

        self._initBoard()

    # PROPERTIES

    @property
    def PieceCount(self):
        return self.__pieceCount

    @staticmethod
    def Opp(turn):
        return "B" if turn == "W" else "W"

    # PUBLIC METHODS

    # ensure move is valid
    def validateMove(self, turn, coord):
        Y = int(coord[0])
        X = int(coord[1])
        
        if self._gameBoard[Y][X] != self._delimeter:
            return False 
        else:
            opp = self.Opp(turn)
            tmpMove = []
            
            for dir in self.__dirList:
                self.__isValidMoveDir(Y, X, dir, opp)

            return False if not self.__tmpMove else True

    # store turn in board and transposed board
    def makeMove(self, turn, coord):
        if self.validateMove(turn, coord):
            self._updateBoard(coord, turn)

    # check for winner
    def checkWinner(self):
        if 0 in self.__pieceCount.values():
            if self.__pieceCount["B"] > self.__pieceCount["W"] :
               return 0
            elif self.__pieceCount["B"] < self.__pieceCount["W"]:
              return 1
            else:
              return 2

    # PROTECTED METHODS

    def _initBoard(self):
        super()._initBoard(1)

        self._gameBoard[3][3] = self._gameBoard[4][4] = "W"
        self._gameBoard[3][4] = self._gameBoard[4][3] = "B"

    # update gameBoard
    def _updateBoard(self, coord, turn, isNewPos=False):
        if self.__tmpMove:
            Y = int(coord[0])
            X = int(coord[1])

            self._gameBoard[Y][X] = turn
            self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
            self.__pieceCount[self._delimeter] = int(self.__pieceCount[self._delimeter]) - 1

            opp = "B" if turn == "W" else "W"
            for p in self.__tmpMove:
                self._gameBoard[p[0]][p[1]] = turn
                self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
                self.__pieceCount[opp] = int(self.__pieceCount[opp]) - 1

            self.__tmpMove = []

    # PRIVATE METHODS
    def __isValidMoveDir(self, Y, X, coordDir, opp):
        Yinc = int(coordDir[0])
        Xinc = int(coordDir[1])

        tmpMove = []
        myPieceFound = False
        
        for i in range(1, self._boardSize-1):
            Yj = (i * Yinc if Yinc != 0 else 0) + Y
            Xj = (i * Xinc if Xinc != 0 else 0) + X

            if Yj < self._boardSize and Xj < self._boardSize:
                if self._gameBoard[Yj][Xj] == opp:
                    tmpMove.append([Yj,Xj])
                elif self._gameBoard[Yj][Xj] == self._delimeter:
                    break
                else:
                    myPieceFound = True

        if myPieceFound and tmpMove:
            self.__tmpMove.extend(tmpMove)
