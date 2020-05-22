import random
from MyLogger.MyLogger import MyLogger      # Logger module

from TicTacToe.TicTacToeBoard import TicTacToeBoard
from Game import Game

class TicTacToe(Game):

    turn = "X"
    delimeter = "_"

    # CONSTRUCTORS

    #initialize game parameters through user input
    @MyLogger.log_decorator
    def __init__(self, **kwargs):   
        print("\nWelcome to Tic Tac Toe!")

        # cant do kwargs.get("boardSize", self.getBoardSize()) because method still runs to get default value
        self.boardSize = self.getBoardSize() if kwargs.get("boardSize", None) == None else kwargs["boardSize"]
        self.numPlayers = self.getGameMode() if kwargs.get("gameMode", None) == None else kwargs["gameMode"]     
        self.difficulty = 1 if self.numPlayers == 2 else self.getDifficulty() if kwargs.get("difficulty", None) == None else kwargs["difficulty"]      
        
        self._initGame()

        if not kwargs:
            self._playGame()

    # DEPRECATED, use __init__ with kwargs, leaving for info purposes only
    # ClassMethod constructor that does not call __init__
    # used for testing to get around user input
    @classmethod
    def init(cls, boardSize, difficulty, gameMode):
        objTTT = cls.__new__(cls)
        objTTT.boardSize = boardSize
        objTTT.numPlayers = gameMode
        objTTT.difficulty = difficulty
        #super(TicTacToe, objTTT).__init__(TicTacToe.turn, boardSize, TicTacToe.delimeter)

        objTTT._initGame()        

        return objTTT

    # PROTECTED METHODS

    # Method to init game parameters common to all constructors
    @MyLogger.log_decorator
    def _initGame(self):
        super().__init__(TicTacToe.turn, self.boardSize, TicTacToe.delimeter)
        self.board = TicTacToeBoard(self.boardSize, self.delimeter)

        self._addPlayer("X","X")
        self._addPlayer("O","O")

    # get next move from user or generate for cpu until game has ended
    @MyLogger.log_decorator
    def _playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "X":
                coord = self._getMoveHuman()
            else:
                coord = self._getMoveCPU()

            self.board.makeMove(self.turn, coord)
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == 2:
                print("It's a DRAW!\n")
            elif gameEnd:
                print(self.turn + " WINS!\n")
            else:
                self.turn = "X" if self.turn == "O" else "O"

    # Player chooses next move
    @MyLogger.log_decorator
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
                    success = 1 

        return coord

    # if cpu difficulty is 2 or greater always pick a winning or blocking move, else just random move
    @MyLogger.log_decorator
    def _getMoveCPU(self):        
        if self.difficulty >= 2:
            coord = self.board.getBestMove()

        # choose random coord if Easy or not winning move for Medium/Hard
        if self.difficulty == 1 or coord[0] == self.boardSize:
            X = random.randrange(self.boardSize)
            Y = random.randrange(self.boardSize)
            while (not(self.board.validateMove(self.turn, [Y, X]))):
                X = random.randrange(self.boardSize)
                Y = random.randrange(self.boardSize)
            coord = [Y,X]

        return coord

if __name__ == '__main__':
    TicTacToe()

