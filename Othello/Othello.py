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
    
    # get CPU move
    def _getMoveCPU(self):
        cpuMoveCoord = self.board.getBestMove(self.turn)

        self.Y = int(cpuMoveCoord[0])
        self.X = int(cpuMoveCoord[1])

if __name__ == '__main__':
    myTTT = Othello()
