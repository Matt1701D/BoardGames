import random
from TicTacToe.TicTacToeBoard import TicTacToeBoard
from Game import Game

class TicTacToe(Game):

    #initialize game parameters through user input
    def __init__(self):   
        print("\nWelcome to Tic Tac Toe!")

        boardSize = Game.getBoardSize()
        self.numPlayers = Game.getGameMode()        
        self.difficulty = 0 if self.numPlayers == 2 else Game.getDifficulty()        

        delimeter = "_"
        turn = "X"
        self.X = self.Y = -1
        super().__init__(turn, boardSize, delimeter)

        self.board = TicTacToeBoard(boardSize, delimeter)

        self._playGame()

    @classmethod
    def init(cls, boardSize, difficulty, gameMode):
        obj = cls.__new__(cls)
        super(TicTacToe, obj).__init__("X", boardSize, "_")

        obj.numPlayers = gameMode
        obj.difficulty = difficulty
        obj.board = TicTacToeBoard(boardSize, obj.delimeter)        

        return obj

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "X":
                self.__getMoveHuman()
            else:
                self.getMoveCPU()

            self.board.makeMove(self.turn, [self.Y, self.X])
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == 2:
                print("It's a DRAW!\n")
            elif gameEnd:
                print(self.turn + " WINS!\n")
            else:
                self.turn = "X" if self.turn == "O" else "O"

    # PRIVATE METHODS

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
                    print("Already move made at coordinates:" + str(coord))
                else:
                    self.X = int(X)
                    self.Y = int(Y)
                    success = 1 

    # if cpu difficulty is 2 or greater always pick a winning or blocking move, else just random move
    def getMoveCPU(self):        
        if self.difficulty >= 2:
            self.__makeMoveWin()

        # choose random coord if Easy or not winning move for Medium/Hard
        if self.difficulty == 1 or self.Y == self.boardSize:
            X = random.randrange(self.boardSize)
            Y = random.randrange(self.boardSize)
            while (not(self.board.validateMove(self.turn, [Y, X]))):
                X = random.randrange(self.boardSize)
                Y = random.randrange(self.boardSize)
            self.X = X
            self.Y = Y

    # always have cpu pick coord to win or block a win
    def __makeMoveWin(self):
        X = Y = self.boardSize
        XCountR = OCountR = BCountR = 0
        XCountL = OCountL = BCountL = 0

        for i in range(self.boardSize):
            #check horizontal
            if (self.board.GameBoard[i].count(self.delimeter) == 1 and (self.board.GameBoard[i].count('O') == self.boardSize - 1 or (self.board.GameBoard[i].count('X') == self.boardSize - 1))):
                Y = i
                X = self.board.GameBoard[i].index(self.delimeter)

            #check vertical
            if (self.board.GameBoardT[i].count(self.delimeter) == 1 and (self.board.GameBoardT[i].count('O') == self.boardSize - 1 or (self.board.GameBoardT[i].count('X') == self.boardSize - 1))):
                Y = self.board.GameBoardT[i].index(self.delimeter)
                X = i

            #check diagonal right
            if self.board.GameBoard[i][i] == 'X':
                XCountR += 1
            elif self.board.GameBoard[i][i] == 'O':
                OCountR += 1
            else:
                BlankR = [i, i]
                BCountR += 1

            #check diagonal left
            XCoord = self.boardSize - 1 - i
            if self.board.GameBoard[XCoord][i] == 'X':
                XCountL += 1
            elif self.board.GameBoard[XCoord][i] == 'O':
                OCountL += 1
            else:
                BlankL = [XCoord, i]
                BCountL += 1

        if BCountR == 1 and ((XCountR == self.boardSize - 1) or (OCountR == self.boardSize - 1)):
            Y = BlankR[0]
            X = BlankR[1]
        elif BCountL == 1 and ((XCountL == self.boardSize - 1) or (OCountL == self.boardSize - 1)):
            Y = BlankL[0]
            X = BlankL[1]

        self.X = X
        self.Y = Y

if __name__ == '__main__':
    myTTT = TicTacToe()

