import random
from TicTacToe.TicTacToeBoard import TicTacToeBoard
from Game import Game

class TicTacToe(Game):

    #initialize game parameters through user input
    def __init__(self):    
        super().__init__("X", self.getBoardSize(), "_")

        self.numPlayers = self.gameMode()
        self.difficulty = 0 if self.numPlayers == 2 else self.gameDifficulty()
        self.board = TicTacToeBoard(self.boardSize, self.delimeter)
        self.X = self.Y = -1

        self._playGame()
    
    def getBoardSize(self):
        print("\nWelcome to Tic Tac Toe!")
        success = 0
        while(not(success)):
            boardSize = input("Enter size of board (odd number): ")
            if (not(boardSize.isdigit())):
                print("Board size not a number")
            elif int(boardSize) < 3 or int(boardSize) % 2 == 0:   
                print("Board size less than 3 or not odd")
            else:
                success = 1
        return int(boardSize)

    def gameDifficulty(self):
        success = 0
        while(not(success)):
            difficulty = input("Enter computer difficulty 1 (Easy), 2 (Medium), 3 (Hard): ")
            if (not(difficulty.isdigit())):
                print("Difficulty is not a number")
            elif int(difficulty) not in [1,2,3]:   
                print("Difficulty must be 1, 2 or 3")
            else:
                success = 1
        return int(difficulty)
    
    def gameMode(self):
        success = 0
        while(not(success)):
            numPlayers = input("Enter 1 to play against computer or 2 to play between humans: ")
            if (not(numPlayers.isdigit())):
                print("Number of players is not a number")
            elif int(numPlayers) not in [1,2]:   
                print("Number of players must be 1 or 2")
            else:
                success = 1
        return int(numPlayers)

    # PROTECTED METHODS

    # get next move from user or generate for cpu until game has ended
    def _playGame(self):
        gameEnd = 0
        while(not(gameEnd)):
            if self.numPlayers == 2 or self.turn == "X":
                self.getMoveHuman()
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

    def getMoveHuman(self):
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
            self.makeMoveWin()

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
    def makeMoveWin(self):
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
            X = BlankR[0]
            Y = BlankR[1]
        elif BCountL == 1 and ((XCountL == self.boardSize - 1) or (OCountL == self.boardSize - 1)):
            X = BlankL[0]
            Y = BlankL[1]

        self.X = X
        self.Y = Y

if __name__ == '__main__':
    myTTT = TicTacToe()

