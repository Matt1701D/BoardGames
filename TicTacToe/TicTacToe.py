import random
from TicTacToe.TicTacToeBoard import TicTacToeBoard
from Game import Game

class TicTacToe(Game):

    turn = "X"
    delimeter = "_"

    # CONSTRUCTORS

    #initialize game parameters through user input
    def __init__(self):   
        print("\nWelcome to Tic Tac Toe!")
        super().__init__(turn=TicTacToe.turn, boardSize=Game.getBoardSize(), delimeter=TicTacToe.delimeter)

        self.numPlayers = Game.getGameMode()        
        self.difficulty = 0 if self.numPlayers == 2 else Game.getDifficulty()        
        self.X = self.Y = -1        

        self.board = TicTacToeBoard(self.boardSize, self.delimeter)

        self._playGame()

    # ClassMethod constructor that does not call __init__
    # used for testing to get around user input
    # alternatively could use bit in __init__ to decide
    # who is instantiating (test or user)
    @classmethod
    def init(cls, boardSize, difficulty, gameMode):
        objTTT = cls.__new__(cls)
        super(TicTacToe, objTTT).__init__(TicTacToe.turn, boardSize, TicTacToe.delimeter)

        objTTT.X = objTTT.Y = -1
        objTTT.numPlayers = gameMode
        objTTT.difficulty = difficulty
        objTTT.board = TicTacToeBoard(boardSize, objTTT.delimeter)        

        return objTTT

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "X":
                self._getMoveHuman()
            else:
                self._getMoveCPU()

            self.board.makeMove(self.turn, [self.Y, self.X])
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == 2:
                print("It's a DRAW!\n")
            elif gameEnd:
                print(self.turn + " WINS!\n")
            else:
                self.turn = "X" if self.turn == "O" else "O"

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
                    print("Already move made at coordinates:" + str(coord))
                else:
                    self.X = int(X)
                    self.Y = int(Y)
                    success = 1 

    # if cpu difficulty is 2 or greater always pick a winning or blocking move, else just random move
    def _getMoveCPU(self):        
        if self.difficulty >= 2:
            cpuMoveCoord = self.board.getBestMove()

            self.Y = int(cpuMoveCoord[0])
            self.X = int(cpuMoveCoord[1])

        # choose random coord if Easy or not winning move for Medium/Hard
        if self.difficulty == 1 or self.Y == self.boardSize:
            X = random.randrange(self.boardSize)
            Y = random.randrange(self.boardSize)
            while (not(self.board.validateMove(self.turn, [Y, X]))):
                X = random.randrange(self.boardSize)
                Y = random.randrange(self.boardSize)

            self.X = X
            self.Y = Y

if __name__ == '__main__':
    myTTT = TicTacToe()

