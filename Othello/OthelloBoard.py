from operator import itemgetter
import sys

from MyLogger.MyLogger import MyLogger                  # Logger module
from Board import Board


class OthelloBoard(Board):

    # CONSTRUCTOR 

    @MyLogger.log(["File"])
    def __init__(self, boardSize, delimeter):
        """
        Create Othello board of boardSize and populated with delimeter string
        """
        super().__init__(boardSize, delimeter)

        # initial setup of 2 black and white pieces
        self.__pieceCount = {"B":2,"W":2,str(self._delimeter):(self._boardSize**2)-4}
        self.__tmpMove = []

        # 8 way directional list to look for peices to flip
        dirCoord = [-1,0,1]
        self.__dirList = [[x,y] for x in dirCoord for y in dirCoord if [x,y] != [0,0]]

        # Corner list for CPU moves to choose as a default over other moves
        self.__cornerTup = ((0,0),(0,self._boardSize-1),(self._boardSize-1,0),(self._boardSize-1,self._boardSize-1))

        self._initBoard()

    # PROPERTIES

    @property
    def PieceCount(self):
        return self.__pieceCount

    @staticmethod
    def Opp(turn):
        return "B" if turn == "W" else "W"

    # PUBLIC METHODS

    @MyLogger.log(["File"])
    def validateMove(self, turn, coord):
        """
        Ensure the move is valid for turn given a list of coord [Y,X]
        """

        # If we have list of moves already then already validated
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
                    tmpMove = self.__isValidMoveDir(coord, dir, opp)

                    if tmpMove:
                        self.__tmpMove.extend(tmpMove)

                return True if self.__tmpMove else False

    @MyLogger.log(["File"])
    def makeMove(self, turn, coord):
        """
        Make the move for turn given a list of coord [Y,X]
        """
        if self.validateMove(turn, coord):
            self._updateBoard(turn, coord)

    @MyLogger.log(["File"])
    def checkWinner(self):
        """
        Check if the game is over (win or draw)
        """
        if 0 in self.__pieceCount.values():
            if self.__pieceCount["B"] > self.__pieceCount["W"] :
               return "B"
            elif self.__pieceCount["B"] < self.__pieceCount["W"]:
              return "W"
            else:
              return "D"
        else:
            return 0

    @MyLogger.log(["File"])
    def printBoard(self):
        """
        Overridden print board method for Othello
        """
        print(' '*2+' '.join([str(i) for i in range(0,self._boardSize)]))

        for idx, row in enumerate(self._gameBoard):
            print(str(idx) + ' ' + ' '.join([str(s) for s in row]))

        print("\n")
        print(f"White = {self.__pieceCount['W']}, Black = {self.__pieceCount['B']}, Blank = {self.__pieceCount[self._delimeter]}")

    @MyLogger.log(["File"])
    def getBestMove(self, turn):
        """
        Compute the best move for turn in flip count unless corner move possible. Returns coord [Y,X]
        """
        bestMoves = {}
        opp = self.Opp(turn)

        # List of all available spots to make a move, using tuple here as dict key since dict key cant be mutable so no list
        blankList = [(y,x) for y in range(self._boardSize) for x in range(self._boardSize) if self._gameBoard[y][x] == self._delimeter]

        for b in blankList:
            # look in all directions of each possible move to count number of flips
            for coordDir in self.__dirList:
                tmpMove = self.__isValidMoveDir(list(b), coordDir, opp)

                # add piece coord from this direction to master list and assign num of flips  
                if tmpMove:                                   
                    if b not in bestMoves:
                        bestMoves[b] = len(tmpMove)
                    else:
                        bestMoves[b] = int(bestMoves[b]) + len(tmpMove)                       

        # find move with most flips, choosing corner move with highest priority
        bestMove = sorted(bestMoves.items(), key=self.__sortBestMove, reverse=True)[0]                 
        #bestMove = [list(move) for move in bestMoves if bestMoves[move] ==  max(bestMoves.values())]

        return bestMove[0]
    
    # PROTECTED METHODS

    @MyLogger.log(["File"])
    def _initBoard(self):
        super()._initBoard()

        # Half board size
        hB = int(self._boardSize / 2)

        # set initial position
        self._gameBoard[hB-1][hB-1] = self._gameBoard[hB][hB] = "W"
        self._gameBoard[hB-1][hB] = self._gameBoard[hB][hB-1] = "B"

    # update gameBoard
    @MyLogger.log(["File"])
    def _updateBoard(self, turn, coord, isNewPos=False):
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

    # Sorting method to return move with most flips for corner moves first else other moves
    # added boardsize^2 since no move could have more than that num of flips
    @MyLogger.log(["File"])
    def __sortBestMove(self,move):        
        if move[0] in self.__cornerTup:
            return move[1] + (self._boardSize**2)
        else:
            return move[1]

    # Check direction for valid move
    @MyLogger.log(["File"])
    def __isValidMoveDir(self, coord, coordDir, opp):
        Y = int(coord[0])
        X = int(coord[1])

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

        return tmpMove if myPieceFound else []

