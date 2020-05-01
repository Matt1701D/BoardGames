from ChutesAndLadders import ChutesAndLadders
from TicTacToe import TicTacToe

class BoardGames(object):

    #initialize game
    def __init__(self):
        myGameFactory = GameFactory()
        myGameFactory.registerGame(1, "TicTacToe", TicTacToe.TicTacToe)
        myGameFactory.registerGame(2, "ChutesAndLadders", ChutesAndLadders.ChutesAndLadders)

        choiceOutput = "Type the number of the game you would like to play or Q to Quit\n"
        for game in myGameFactory.GetGameNames:
            choice = str(game) + ") " + myGameFactory.GetGameNames[game] + "\n"
            choiceOutput += choice 
        choiceOutput += "Q) Quit\n" 

        validGame = False
        while(not(validGame)):
            game = input(choiceOutput)            

            if game == 'Q' or game == 'q':
                break
            elif (not(game.isdigit())):
                print("Choice is not a number")
            elif int(game) not in [1,2]:   
                print("Choice must be 1 or 2")   
            else:
                myGameFactory.getGame(int(game))

class GameFactory(object):
    def __init__(self):
        self.__games = {}
        self.__gameNames = {}

    @property
    def GetGameNames(self):
        return self.__gameNames

    def registerGame(self, gameID, gameName, creator):
        self.__games[gameID] = creator
        self.__gameNames[gameID] = gameName

    def getGame(self, gameID):
        creator = self.__games[gameID]
        if not creator:
            raise Exception("Invalid gameID: {}".format(gameID))
        return creator()
        
if __name__ == '__main__':
    myGame = BoardGames()

