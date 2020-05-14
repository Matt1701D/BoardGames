from Game import Game
from Othello.OthelloBoard import OthelloBoard

class Othello(Game):

    turn = "B"
    delimeter = "_"
    boardSize = 8

    # CONSTRUCTORS

    def __init__(self, **kwargs):
        print("\nWelcome to Othello!")

        # cant do kwargs.get("gameMode", self.getGameMode()) because method still runs to get default value
        self.numPlayers = self.getGameMode() if kwargs.get("gameMode", None) == None else kwargs["gameMode"]     

        self._initGame()

        if not kwargs:
            self._playGame()

    # ClassMethod constructor that does not call __init__
    # used for testing to get around user input
    # alternatively could call in __init__ with optional args
    @classmethod
    def init(cls, numPlayers):
        objOT = cls.__new__(cls)
        objOT.numPlayers = numPlayers
        #super(Othello, objOT).__init__(Othello.turn, Othello.boardSize, Othello.delimeter)        

        objOT._initGame()

        return objOT

    # PRIVATE METHODS

    # Method to init game parameters common to all constructors
    def _initGame(self):
        super().__init__(Othello.turn, Othello.boardSize, Othello.delimeter)
        self.board = OthelloBoard(self.boardSize,self.delimeter)

        self._addPlayer("B","Black")
        self._addPlayer("W","White")

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        self.board.printBoard()

        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "B":
                coord = self._getMoveHuman()
            else:
                coord = self._getMoveCPU()
                print("{} placed piece at {} {}\n".format(self.players[self.turn], coord[0], coord[1]))

            self.board.makeMove(self.turn, coord)
            self.board.printBoard()

            gameEnd = self.board.checkWinner()

            if gameEnd == "D":
                print("It's a DRAW!\n")
            elif gameEnd:
                print(self.players[gameEnd] + " WINS!\n")
            else:
                self.turn = self.board.Opp(self.turn)
    
    # Player chooses next move
    def _getMoveHuman(self):
        success = 0
        while (not(success)):
            userInput = input("Enter coordinates for " + self.players[self.turn] + ": ")
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
                    success = 1 

        return coord
    
    # get CPU move
    def _getMoveCPU(self):
        return self.board.getBestMove(self.turn)

if __name__ == '__main__':
    myTTT = Othello()
