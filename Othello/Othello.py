from MyLogger.MyLogger import MyLogger                  # Logger module
from MyLogger.MyExceptions import *                     # Custom Exceptions
from Othello.OthelloBoard import OthelloBoard
from Game import Game

class Othello(Game):

    turn = "B"
    delimeter = "_"
    boardSize = 8

    # CONSTRUCTORS

    @MyLogger.log_decorator
    def __init__(self, gameMode=None, skipPlay=False):
        """
        Create Othello game class. Optional to pass in gameMode (1 to play vs CPU, 2 to play vs Humans), dont't pass for user prompt
        """
        print("\nWelcome to Othello!")
        
        # Get and validate game parameters from user or init
        try:     
            self.numPlayers = self.getGameMode(gameMode, '^[1-2]$')   
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
    def init(cls, gameMode):
        """
        Alternate Othello constructor to pass in gameMode (1 to play vs CPU, 2 to play vs Humans)
        """
        objOT = cls.__new__(cls)
        objOT.numPlayers = gameMode
        # cant do kwargs.get("gameMode", self.getGameMode()) because getGameMode method still runs to get default value  
        #super(Othello, objOT).__init__(Othello.turn, Othello.boardSize, Othello.delimeter)        

        objOT._initGame()

        return objOT

    # PROTECTED METHODS

    # Method to init game parameters common to all constructors
    @MyLogger.log_decorator
    def _initGame(self):
        super().__init__(Othello.turn, Othello.boardSize, Othello.delimeter)
        self.board = OthelloBoard(self.boardSize,self.delimeter)

        self._addPlayer("B","Black")
        self._addPlayer("W","White")

    # get next move from user or generate for cpu until game has ended
    @MyLogger.log_decorator
    def _playGame(self):
        self.board.printBoard()

        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "B":
                coord = self._getMoveHuman()
            else:
                coord = self._getMoveCPU()

            print(f"{self.players[self.turn]} placed piece at {coord[0]} {coord[1]}\n")

            self.board.makeMove(self.turn, coord)
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == "D":
                print("It's a DRAW!\n")
            elif gameEnd:
                print(f"{self.players[gameEnd]} WINS!\n")
            else:
                self.turn = self.board.Opp(self.turn)
    
    # Player chooses next move
    @MyLogger.log_decorator
    def _getMoveHuman(self):
        success = 0
        while (not(success)):
            userInput = input(f"Enter coordinates for {self.players[self.turn]}: ")
            coord = userInput.split()

            if len(coord) != 2:
                print("You didnt enter 2 coordinates")
            else:
                Y = coord[0]
                X = coord[1]

                if (not(X.isdigit()) or int(X) >= self.boardSize):
                    print(f"First coordinate is not an integer or less than {str(self.boardSize)}")
                elif (not(Y.isdigit()) or int(Y) >= self.boardSize):
                    print(f"Second coordinate is not an integer or less than {str(self.boardSize)}")
                elif (not(self.board.validateMove(self.turn, coord))):
                    print(f"Invalid move at coordinates: {str(coord)}")
                else:                    
                    success = 1 

        return coord
    
    # get CPU move
    @MyLogger.log_decorator
    def _getMoveCPU(self):
        return self.board.getBestMove(self.turn)

if __name__ == '__main__':
    Othello()
