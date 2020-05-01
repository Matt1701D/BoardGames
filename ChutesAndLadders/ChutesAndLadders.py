import random
from ChutesAndLadders.ChutesAndLaddersBoard import ChutesAndLaddersBoard
from Game import Game

class ChutesAndLadders(Game):

    #initialize game
    def __init__(self):
        super().__init__(0, 10, "_")
        self.maxSpin = 6
        self.players = self.getPlayers()
        self.board = ChutesAndLadders(self.boardSize, self.delimeter, len(self.players))

        self._playGame()

    #get player names
    def getPlayers(self):
        print("\nWelcome to Chutes and Ladders!")

        players = []
        playersSuccess = False
        while(not playersSuccess):
            players = input("Enter unique name for players separated by comma: ")
            players = players.split(',')
            if len(players) == len(set(players)):
                playersSuccess = True
            else:
                print("Player names not unique!")
        
        return players

    # PROTECTED METHODS

    #have players spin and move
    def _playGame(self):
        playerCnt = len(self.players)

        gameWon = False
        while(not(gameWon)):
            input(self.players[self.turn] + " press Enter to spin")
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

