from Game import Game
from Othello.OthelloBoard import OthelloBoard

class Othello(Game):

    turn = "B"
    delimeter = "_"
    boardSize = 8

    # CONSTRUCTORS

    def __init__(self):
        print("\nWelcome to Othello!")
        super().__init__(Othello.turn, Othello.boardSize, Othello.delimeter)

        self.numPlayers = Game.getGameMode()

        tmpMove = {}
        self.X = self.Y = -1

        self.board = OthelloBoard(self.boardSize,self.delimeter)

        self._playGame()

    # ClassMethod constructor that does not call __init__
    # used for testing to get around user input
    # alternatively could use bit in __init__ to decide
    # who is instantiating (test or user)
    @classmethod
    def init(cls, numPlayers):
        objOT = cls.__new__(cls)
        super(Othello, objOT).__init__(Othello.turn, Othello.boardSize, Othello.delimeter)

        objOT.numPlayers = 2
        objOT.board = OthelloBoard(Othello.boardSize, Othello.delimeter)

        return objOT

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        self.board.printBoard()

        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "B":
                self._getMoveHuman()
            else:
                self._getMoveCPU()
                print("{} placed piece at {} {}\n".format(self.turn, self.Y, self.X))

            self.board.makeMove(self.turn, [self.Y, self.X])
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == "D":
                print("It's a DRAW!\n")
            elif gameEnd:
                print(gameEnd + " WINS!\n")
            else:
                self.turn = "B" if self.turn == "W" else "W"
    
    # Player chooses next move
    def _getMoveHuman(self):
        success = 0
        while (not(success)):
            userInput = input("Enter coordinates for " + self.turn + ": ")
            coord = userInput.split()

            if len(coord) != 2:
                print("You didnt enter 2 coordinates")
            else:
                Y = coord[0]
                X = coord[1]

                if (not(X.isdigit()) or int(X) >= self.boardSize):
                    print("First coordinate isnt an integer or less than " + str(self.boardSize))
                elif (not(Y.isdigit()) or int(Y) >= self.boardSize):
                    print("Second coordinate isnt an integer or less than " + str(self.boardSize))
                elif (not(self.board.validateMove(self.turn, coord))):
                    print("Invalid move at coordinates:" + str(coord))
                else:
                    self.X = int(X)
                    self.Y = int(Y)
                    success = 1 
    
    def _getMoveCPU(self):
        cpuMoves = {}
        opp = "B" if self.turn == "W" else "W"

        # List of all available spots to make a move
        blankList = [[y,x] for y in range(self.boardSize) for x in range(self.boardSize) if self.board.GameBoard[y][x] == self.delimeter]

        for b in blankList:
            Y = b[0]
            X = b[1]
            strXY = "{},{}".format(str(Y),str(X))

            # look in all directions of each possible move to count number of flips
            for coordDir in self.board.DirList:
                tmpMove = self.board.isValidMoveDir(Y, X, coordDir, opp)

                # add piece coord from this direction to master list and assign num of flips  
                if tmpMove:                                   
                    if strXY not in cpuMoves:
                        cpuMoves[strXY] = len(tmpMove)
                    else:
                        cpuMoves[strXY] = int(cpuMoves[strXY]) + len(tmpMove)

        # find move with most flips
        cpuMove = [move for move in cpuMoves if cpuMoves[move] ==  max(cpuMoves.values())]
        cpuMoveCoord = cpuMove[0]

        self.Y = int(cpuMoveCoord[0])
        self.X = int(cpuMoveCoord[2])

    # cpu always picks move with most flips
    def _getMoveCPUTwo(self):        
        tmpMove = {}
        opp = "B" if self.turn == "W" else "W"

        # Get locations of pieces for turn
        pieceList = [[y,x] for y in range(self.boardSize) for x in range(self.boardSize) if self.board.GameBoard[y][x] == self.turn]

        blankList = [[y,x] for y in range(self.boardSize) for x in range(self.boardSize) if self.board.GameBoard[y][x] == self.delimeter]


        # for each existing piece, navigagte all directions and see if there is valid move
        # and store number of flips for that move
        for p in pieceList:
            Y = p[0]
            X = p[1]
            
            # loop through all directions
            for coordDir in self.board.DirList:
                Yinc = int(coordDir[0])
                Xinc = int(coordDir[1])

                flips = 0
                myPieceFound = False        

                for i in range(1, self.boardSize-1):
                    # set coordinate to check based on direction and incrementer
                    Yj = (i * Yinc if Yinc != 0 else 0) + Y
                    Xj = (i * Xinc if Xinc != 0 else 0) + X

                    # make sure we are within board dimensions
                    if Yj < self.boardSize and Xj < self.boardSize:
                        # if peice is opponent save it to flip later
                        if self.board.GameBoard[Yj][Xj] == opp:
                            flips+=1
                        # if first piece isnt opponent or piece belongs to turn
                        elif i == 1 or self.board.GameBoard[Yj][Xj] == self.turn:
                            break
                        # found blank so we have valid move
                        else:
                            myPieceFound = True
                            break

                # add piece coord from this direction to master list and assign num of flips  
                if myPieceFound:                  
                    strXY = "{},{}".format(str(Yj),str(Xj))
                    if strXY not in tmpMove:
                        tmpMove[strXY] = flips
                    else:
                        tmpMove[strXY] = int(tmpMove[strXY]) + flips

        # find move with most flips
        cpuMove = [move for move in tmpMove if tmpMove[move] ==  max(tmpMove.values())]
        cpuMoveCoord = cpuMove[0]

        self.Y = int(cpuMoveCoord[0])
        self.X = int(cpuMoveCoord[2])

if __name__ == '__main__':
    myTTT = Othello()
