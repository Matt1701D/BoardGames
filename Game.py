from abc import ABC, abstractmethod     # Abstract class module
from re import search                   # RegEx module for input validation
from MyLogger.MyLogger import MyLogger  # Logger module
from MyLogger.MyExceptions import *     # Custom Exceptions

# Game interface for game setup and play
class Game(ABC):

    @MyLogger.log(["File"])
    def __init__(self, turn, boardSize, delimeter='_'):
        self.turn = turn                # whose first turn is it
        self.boardSize = boardSize      # Size of board, boards are squared
        self.delimeter = delimeter      # delimter used in board printout for empty spaces
        self.players = {}               # dictionary of player keys (number) and labels (names)

    # PUBLIC METHODS

    # Get player names as input
    @MyLogger.log(["File"])
    def getPlayers(self):
        players = []
        playersSuccess = False
        while(not playersSuccess):
            players = input("Enter unique name for players separated by comma: ")
            players = players.split(',')
            if len(players) == len(set(players)):
                playersSuccess = True
            else:
                print("Player names not unique!")

        for idx, player in enumerate(players):
            self._addPlayer(idx, player.strip())

    # PROTECTED METHODS

    # register player
    @MyLogger.log(["File"])
    def _addPlayer(self, playerKey, playerName):
        self.players[playerKey] = playerName

    # Method to init game parameters common to all constructors
    @abstractmethod
    def _initGame(self):
        pass

    # Method to perform gameplay operations
    @abstractmethod
    def _playGame(self):
        pass

    # Method to get a human player's move
    @abstractmethod
    def _getMoveHuman(self):
        pass
        
    # Method to determine cpu move
    @abstractmethod
    def _getMoveCPU(self):
        pass
    
    # STATIC METHODS

    # User input method for getting board size
    @staticmethod
    @MyLogger.log(["File"])
    def getBoardSize(boardSize, regEx, minSize=3, maxSize=9, oddSize=True):
        if boardSize is None:
            success = 0
            while(not(success)):
                question = f"Enter size of board (Min: {minSize}, Max {maxSize}, {'Odd' if oddSize==True else 'Even'}):"
                boardSize = input(question)
                if not search(regEx,boardSize): 
                    print(f"Board size must match {regEx}")
                else:
                    success = 1
        elif not search(regEx,str(boardSize)):
            raise InvalidParameterException("boardSize", boardSize, regEx) 

        return int(boardSize)

    # User input method for getting computer difficulty level
    @staticmethod
    @MyLogger.log(["File"])
    def getDifficulty(difficulty, regEx):
        if difficulty is None:
            success = 0
            while(not(success)):
                difficulty = input("Enter computer difficulty 1 (Easy), 2 (Medium), 3 (Hard): ")
                if not search(regEx,difficulty): 
                    print(f"Difficulty must match {regEx}")
                else:
                    success = 1
        elif not search(regEx,str(difficulty)):
            raise InvalidParameterException("difficulty", difficulty, regEx) 

        return int(difficulty)
    
    # User input method for getting human vs human or human vs cpu game mode
    @staticmethod
    @MyLogger.log(["File"])
    def getGameMode(numPlayers, regEx):
        if numPlayers is None:
            success = 0
            while(not(success)):
                numPlayers = input("Enter 1 to play against computer or 2 to play between humans: ")
                if not search(regEx,numPlayers):
                    print(f"Number of players must match {regEx}")
                else:
                    success = 1
        elif not search(regEx,str(numPlayers)):
            raise InvalidParameterException("gameMode", numPlayers, regEx) 

        return int(numPlayers)

