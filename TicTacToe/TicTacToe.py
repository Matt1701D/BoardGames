import random

from MyLogger.MyLogger import MyLogger                  # Logger module
from MyLogger.MyExceptions import *                     # Custom Exceptions
from TicTacToe.TicTacToeBoard import TicTacToeBoard     
from Game import Game

class TicTacToe(Game):

    turn = "X"
    delimeter = "_"

    # CONSTRUCTORS

    @MyLogger.log_decorator
    def __init__(self, boardSize=None, gameMode=None, difficulty=None, skipPlay=False):   
        """
        Create TicTacToe game class. Optional to pass in boardSize, gameMode (1 to play vs CPU, 2 to play vs Humans)
        and difficulty 1 (Easy), 2 (Medium), 3 (Hard). Skip parameters to use user prompt instead
        """
        print("\nWelcome to Tic Tac Toe!")
        
        # Get and validate game parameters from user or init
        try:
            self.boardSize = self.getBoardSize(boardSize, '^[3|5|7|9]$')
            self.numPlayers = self.getGameMode(gameMode, '^[1-2]$')  
            self.difficulty = self.getDifficulty(difficulty, '^[1-3]$')      
        except InvalidParameterException as IPEx:
            # Log and Quit
            MyLogger.logException(IPEx)
            print(IPEx)
            raise
        
        self._initGame()

        # For testing dont want to start user prompts so skip
        if not skipPlay:
            self._playGame()

    # DEPRECATED, use __init__ with kwargs, leaving for info purposes only
    # ClassMethod constructor that does not call __init__
    # used for testing to get around user input
    @classmethod
    @MyLogger.log_decorator
    def init(cls, boardSize, difficulty, gameMode):
        """
        Alternate TicTacToe constructor to pass in boardSize, gameMode (1 to play vs CPU, 2 to play vs Humans)
        and difficulty 1 (Easy), 2 (Medium), 3 (Hard)
        """
        objTTT = cls.__new__(cls)
        objTTT.boardSize = boardSize
        objTTT.numPlayers = gameMode
        objTTT.difficulty = difficulty
        # cant do kwargs.get("boardSize", self.getBoardSize()) because method still runs to get default value
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
                print(f"{self.turn} WINS!\n")
            else:
                self.turn = "X" if self.turn == "O" else "O"

    # Player chooses next move
    @MyLogger.log_decorator
    def _getMoveHuman(self):
        success = 0
        while (not(success)):
            userInput = input(f"Enter coordinates for {self.turn}: ")
            coord = userInput.split()

            if len(coord) != 2:
                print("You didnt enter 2 coordinates")
            else:
                Y = coord[0]
                X = coord[1]

                if (not(X.isdigit()) or int(X) >= self.boardSize):
                    print(f"First coordinate isnt an integer or less than {str(self.boardSize)}")
                elif (not(Y.isdigit()) or int(Y) >= self.boardSize):
                    print(f"Second coordinate isnt an integer or less than {str(self.boardSize)}")
                elif (not(self.board.validateMove(self.turn, coord))):
                    print(f"Already move made at coordinates: {str(coord)}")
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

