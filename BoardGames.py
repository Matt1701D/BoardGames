import sys

from MyLogger.MyLogger import MyLogger

# Game modules
from ChutesAndLadders.ChutesAndLadders import ChutesAndLadders
from TicTacToe.TicTacToe import TicTacToe
from Othello.Othello import Othello

# STEPS TO ADD NEW GAME
#   0) Caveats: Make sure game module/class has same name as the game
#   1) Add game module to import as "from Package.Module import className"
#   2) Register game in main module using className of game

class BoardGames(object):

    # Display Game Menu with list of registered games
    @classmethod
    def ShowGameMenu(cls):
        MyLogger.TraceEnter(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

        choiceOutput = "Type the number of the game you would like to play or Q to Quit\n"
        for idx, game in enumerate(GameFactory.games):
            choice = str(idx+1) + ") " + game + "\n"
            choiceOutput += choice 
        choiceOutput += "Q) Quit\n" 

        validGame = False
        while(not(validGame)):
            game = input(choiceOutput)            

            if game == 'Q' or game == 'q':
                break
            elif (not(game.isdigit())):
                print("Choice is not a number")
            elif int(game) > len(GameFactory.games) or int(game) < 1:  
                print("Invalid choice")   
            else:                
                try:
                    gameClass = GameFactory.getGame(int(game)-1)
                    eval(gameClass)()
                except AssertionError as AssertEX:
                    MyLogger.myLog.exception(AssertEX)
                    print(AssertEX)
                except Exception as Ex:
                    strOutputError = "Could not load game. Check the registered game name matches the game's class name and the module has been " 
                    strOutputError += "imported as \'from Package.Module import className\'.\n"
                    print(strOutputError)

        MyLogger.TraceExit(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

# Game Factory class for list of games to play
class GameFactory(object):
    games = []  # our master games list
    
    @classmethod
    # Add game to game list if not already registered and sort list
    def registerGame(cls, game):      
        MyLogger.TraceEnter(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

        if game not in cls.games:
            cls.games.append(game)
            cls.games.sort()

        MyLogger.TraceExit(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

    @classmethod
    # Lookup game by sorted index and return name of game
    def getGame(cls, gameID):
        MyLogger.TraceEnter(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

        creator = cls.games[gameID]
        if not creator:
            strOutputError = "Invalid gameID({}) or game not found.\n".format(gameID)
            #logging.exception(strOutputError)
            raise AssertionError(strOutputError)

        MyLogger.TraceExit(cls.__qualname__ +"."+sys._getframe().f_code.co_name)

        return creator
        
if __name__ == '__main__':
    # start logging
    logFileName = "BoardGames.log"
    logFileMode = "w"
    logName = "BoardGames"
    logLevel = "INFO"
    MyLogger.getMyLogger(logFileName, logFileMode, logName, logLevel)

    # Register list of games using className here
    GameFactory.registerGame("")
    GameFactory.registerGame("ChutesAndLadders")
    GameFactory.registerGame("Othello")

    BoardGames.ShowGameMenu()

