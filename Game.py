from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, turn, boardSize, delimeter):
        self.turn = turn
        self.boardSize = boardSize
        self.delimeter = delimeter
        self.players = {}

    # PUBLIC METHODS

    def getPlayers(self):
        players = []
        playersSuccess = False
        while(not playersSuccess):
            players = input("Enter unique name for players separated by comma: ")
            players = players.split(', ')
            if len(players) == len(set(players)):
                playersSuccess = True
            else:
                print("Player names not unique!")

        for idx, player in enumerate(players):
            self._addPlayer(idx, player)

    # PROTECTED METHODS

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

    # User input methods for game parameters
    @staticmethod
    def getBoardSize(minSize=2, maxSize=10, oddSize=1):
        success = 0
        while(not(success)):
            question = "Enter size of board (Min: {}, Max {}, {}):".format(minSize,maxSize,"Even" if oddSize==0 else "Odd")
            boardSize = input(question)
            if (not(boardSize.isdigit())):
                print("Board size not a number")
            elif int(boardSize) < minSize:
                print("Board size must be greater than {}".format(minSize))
            elif int(boardSize) > maxSize:
                print("Board size must be less than {}".format(maxSize))
            elif int(boardSize) % 2 != oddSize:   
                print("Board size must be {}".format("even" if oddSize==0 else "odd"))
            else:
                success = 1
        return int(boardSize)

    @staticmethod
    def getDifficulty():
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
    
    @staticmethod
    def getGameMode():
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

