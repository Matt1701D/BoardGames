from Board import Board
import sys

class OthelloBoard(Board):

    def __init__(self, boardSize, delimeter):
        super().__init__(boardSize, delimeter)

        self.__pieceCount = {"B":2,"W":2,str(self._delimeter):(self._boardSize**2)-4}
        self.__tmpMove = []

        dirCoord = [-1,0,1]
        self.__dirList = [[x,y] for x in dirCoord for y in dirCoord if [x,y] != [0,0]]

        self._initBoard()

    # PROPERTIES

    @property
    def PieceCount(self):
        return self.__pieceCount

    @property
    def DirList(self):
        return self.__dirList

    @staticmethod
    def Opp(turn):
        return "B" if turn == "W" else "W"

    # PUBLIC METHODS

    # ensure move is valid
    def validateMove(self, turn, coord):
        if self.__tmpMove:
            return True
        else:
            Y = int(coord[0])
            X = int(coord[1])
        
            # invalid spot chosen
            if self._gameBoard[Y][X] != self._delimeter:
                return False 
            else:
                opp = self.Opp(turn)
            
                # check all directions for flips
                for dir in self.__dirList:
                    self.__isValidMoveDir(Y, X, dir, opp)

                return False if not self.__tmpMove else True

    # investigate chosen move and update if valid
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

    # Print out game board
    def printBoard(self):
        print(' '*2+' '.join([str(i) for i in range(0,self._boardSize)]))
        j = 0
        for row in self._gameBoard:
            print(str(j) + ' ' + ' '.join([str(s) for s in row]))
            j+=1
        print("\n")
        print("White = {}, Black = {}, Blank = {}".format(self.__pieceCount["W"], self.__pieceCount["B"], self.__pieceCount[self._delimeter]))

    # PROTECTED METHODS

    def _initBoard(self):
        super()._initBoard(1)

        # set initial position
        self._gameBoard[3][3] = self._gameBoard[4][4] = "W"
        self._gameBoard[3][4] = self._gameBoard[4][3] = "B"

    # update gameBoard
    def _updateBoard(self, coord, turn, isNewPos=False):
        if self.__tmpMove:
            Y = int(coord[0])
            X = int(coord[1])
            opp = self.Opp(turn)

            # set chosen spot and update counters
            self._gameBoard[Y][X] = turn
            self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
            self.__pieceCount[self._delimeter] = int(self.__pieceCount[self._delimeter]) - 1

            # do the flips and update counters
            for p in self.__tmpMove:
                Yp = p[0]
                Xp = p[1]
                self._gameBoard[Yp][Xp] = turn
                self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
                self.__pieceCount[opp] = int(self.__pieceCount[opp]) - 1                   

            # reset master flip list
            self.__tmpMove = []

    # PRIVATE METHODS

    # Check direction for valid move
    def __isValidMoveDir(self, Y, X, coordDir, opp):
        Yinc = int(coordDir[0])
        Xinc = int(coordDir[1])

        tmpMove = []
        myPieceFound = False        

        for i in range(1, self._boardSize-1):
            # set coordinate to check based on direction and incrementer
            Yj = (i * Yinc if Yinc != 0 else 0) + Y
            Xj = (i * Xinc if Xinc != 0 else 0) + X

            # make sure we are within board dimensions
            if Yj < self._boardSize and Xj < self._boardSize:
                # if peice is opponent save it to flip later
                if self._gameBoard[Yj][Xj] == opp:
                    tmpMove.append([Yj,Xj])
                # if first piece isnt opponent or piece is blank quit
                elif i == 1 or self._gameBoard[Yj][Xj] == self._delimeter:
                    break
                # found our piece so we have valid move
                else:
                    myPieceFound = True
                    break

        # add flips from this direction to master list of flips
        if myPieceFound and tmpMove:
            self.__tmpMove.extend(tmpMove)

