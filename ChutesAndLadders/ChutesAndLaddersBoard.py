from MyLogger.MyLogger import MyLogger      # Logger module
from Board import Board

class ChutesAndLaddersBoard(Board):

    # CONSTRUCTOR

    @MyLogger.log(["File"])
    def __init__(self, boardSize, delimeter, playerNum):
        """
        Create ChutesAndLadders board of boardSize and populated with delimeter string and number of players playerNum
        """
        super().__init__(boardSize, delimeter)

        self.__playerNum = playerNum    # num of players in game
        self.__CandLmap = {}            # map of chutes/ladders locations to destinations
        self.__player_loc = {}          # map of player locations

        self._initBoard()

    # PROPERTIES

    @property
    def CandLmap(self):
        return self.__CandLmap

    @property
    def PlayerLoc(self):
        return self.__player_loc

    # PUBLIC METHODS

    @MyLogger.log(["File"])
    def makeMove(self, turn, spin):
        """
        Make the move for turn given a spin integer
        """
        # get player pos
        pos_current = self.__player_loc[turn]
        pos_new = 100 if pos_current + spin > 100 else pos_current + spin

        # check for chute or ladder else keep same position
        pos_new = self.__CandLmap.get(pos_new,pos_new)

        # remove old player location if not first turn
        if pos_current > 0:
            self._updateBoard(turn, pos_current, False)
        
        # update player location
        self.__player_loc[turn] = pos_new
        self._updateBoard(turn, pos_new, True)

    @MyLogger.log(["File"])
    def validateMove(self, turn, position):
        """
        Ensure the move is valid. Not necessary to call since game board logic ensures moves within game board
        """
        return position > 0 and position <= 100

    # check for winner
    @MyLogger.log(["File"])
    def checkWinner(self,turn):
        """
        Check if the game is over by a player at or past 100 spot
        """
        return self.__player_loc[turn] == 100

    # get best cpu move, no computer play in this game so just pass
    def getBestMove(self, turn):
        pass

    # PROTECTED METHODS

    # initialize the game board and players
    @MyLogger.log(["File"])
    def _initBoard(self):
        # set cell width according to number of players and taking into account chutes/ladders labels
        cellLength = 4 + self.__playerNum
        super()._initBoard(cellLength)

        # set players off the board
        for i in range(self.__playerNum):
            self.__player_loc[i] = 0
        
        # init our chutes and ladders locations and destinations
        self.__CandLmap = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44,
                            48:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                            71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

        # make Chutes and Ladder labels and place on board
        ladderCount = chuteCount = 0
        delimString = self._delimeter*(cellLength-3)
        for item in self.__CandLmap:
            key = item
            value = self.__CandLmap[item]

            if key > value:
                labelKey = 'CT'+str(chuteCount)+delimString
                labelValue = 'CB'+str(chuteCount)+delimString
                chuteCount += 1
            else:
                labelKey = 'LB'+str(ladderCount)+delimString
                labelValue = 'LT'+str(ladderCount)+delimString
                ladderCount += 1
        
            self._updateBoard(labelKey, key)
            self._updateBoard(labelValue, value)

    # convert position into grid coordinates and update gameBoard
    @MyLogger.log(["File"])
    def _updateBoard(self,label,position,isNewPos=False):
        gridCoord = self.__posToGrid(position)
        y = gridCoord[0]
        x = gridCoord[1]

        # if setting player new or old position, else we are just setting chute/ladder lablel during init
        if str(label).isnumeric():
            # if setting player's new position replace right most delimeter with player number 
            # else updating player's former position so look for player number to remove
            if isNewPos:
                delimeter = self._delimeter
            else:
                delimeter = str(label)
                label = self._delimeter

            # get current label at this location so not to overwrite a chute/ladder label or another player
            labelCur = self._gameBoard[y][x]

            # loop through cell contents until we find a spot to place the label
            playerFound = False
            cellLength = 4 + self.__playerNum
            while(not(playerFound)):
                if labelCur[cellLength-1] == delimeter:
                    label = labelCur[:cellLength-1] + str(label) + labelCur[cellLength:]
                    playerFound = True
                else:
                    cellLength-=1
            
        self._gameBoard[y][x] = label

    # PRIVATE METHODS
        
    # convert position into grid coordinates and update gameBoard
    @MyLogger.log(["File"])
    def __posToGrid(self,position):
        # convert position to grid coordinates (remember board starts at (9,0), moves Left to Right and Up
        # and then Right to Left and Up
        y = self._boardSize - 1 - int((position-1) / self._boardSize)
        x = (position-1) % self._boardSize if y%2 else self._boardSize - 1 - ((position-1) % self._boardSize)

        return [y, x]

      