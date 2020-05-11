from Game import Game
from Othello.OthelloBoard import OthelloBoard

class Othello(Game):

    turn = "B"
    delimeter = "_"
    boardSize = 8

    def __init__(self):
        print("\nWelcome to Othello!")
        super().__init__(Othello.turn, Othello.boardSize, Othello.delimeter)

        self.numPlayers = Game.getGameMode()

        # initialize potential cpu moves and num of flips
        self.__cpuMoves = {}
        if self.numPlayers == 2:
            self.__cpuMoves["[4,2]"] = 1
            self.__cpuMoves["[2,4]"] = 1
            self.__cpuMoves["[3,5]"] = 1
            self.__cpuMoves["[5,3]"] = 1

        self.X = self.Y = -1

        self.board = OthelloBoard(self.boardSize,self.delimeter)

        self._playGame()

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        self.board.printBoard()

        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "B":
                self.__getMoveHuman()
            else:
                self.__getMoveCPU()
                print("{} placed piece at {} {}\n".format(self.turn, self.Y, self.X))

            self.board.makeMove(self.turn, [self.Y, self.X])
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == 2:
                print("It's a DRAW!\n")
            elif gameEnd:
                print(self.turn + " WINS!\n")
            else:
                self.turn = "B" if self.turn == "W" else "W"

    # PRIVATE METHODS

    # Player chooses next move
    def __getMoveHuman(self):
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

    # cpu always picks move with most flips
    def __getMoveCPU(self):        
        opp = "B" if self.turn == "W" else "W"

        # Get locations of pieces for turn
        oppList = [[y,x] for y in range(self.boardSize) for x in range(self.boardSize) if self.board.GameBoard[y][x] == self.turn]

        # for each existing piece, navigagte all directions and see if there is valid move
        # and store number of flips for that move
        for p in oppList:
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
                    if strXY not in self.__cpuMoves:
                        self.__cpuMoves[strXY] = flips
                    else:
                        self.__cpuMoves[strXY] = int(self.__cpuMoves[strXY]) + flips

        # find move with most flips
        cpuMove = [move for move in self.__cpuMoves if self.__cpuMoves[move] ==  max(self.__cpuMoves.values())]
        cpuMoveCoord = cpuMove[0]

        self.Y = int(cpuMoveCoord[0])
        self.X = int(cpuMoveCoord[2])

if __name__ == '__main__':
    myTTT = Othello()
