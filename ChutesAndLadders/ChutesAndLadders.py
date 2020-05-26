import random

from MyLogger.MyLogger import MyLogger                  # Logger module
from ChutesAndLadders.ChutesAndLaddersBoard import ChutesAndLaddersBoard
from Game import Game

class ChutesAndLadders(Game):

    turn = 0
    delimeter = "_"
    boardSize = 10

    # CONSTRUCTOR

    #initialize game
    @MyLogger.log_decorator
    def __init__(self):
        print("\nWelcome to Chutes and Ladders!")      
        self.maxSpin = 6        

        super().__init__(ChutesAndLadders.turn, ChutesAndLadders.boardSize, ChutesAndLadders.delimeter)
        self.getPlayers()
        self.board = ChutesAndLaddersBoard(self.boardSize, self.delimeter, len(self.players))

        self._playGame()

    # PROTECTED METHODS

    def _initGame(self):
        pass

    #have players spin and move
    @MyLogger.log_decorator
    def _playGame(self):
        playerCnt = len(self.players)

        gameWon = False
        while(not(gameWon)):
            input(self.players[self.turn] + " ("+str(self.turn)+") press Enter to spin")
            print("\n")

            spin = random.randint(1,self.maxSpin)
            print("You spun a " + str(spin))

            self.board.makeMove(self.turn, spin)
            print("\n")
            self.board.printBoard()

            gameWon = self.board.checkWinner(self.turn)
            if gameWon:
                print("\n")
                print(self.players[self.turn] + " wins!\n")
            else:
                self.turn = 0 if self.turn+1 > playerCnt-1 else self.turn+1

    # Method to get a human player's move
    def _getMoveHuman(self):
        pass
        
    # Method to determine cpu move
    def _getMoveCPU(self):
        pass

if __name__ == '__main__':
    ChutesAndLadders()