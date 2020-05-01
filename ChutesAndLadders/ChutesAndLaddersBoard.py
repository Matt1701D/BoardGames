from Board import Board

class ChutesAndLaddersBoard(Board):

    def __init__(self, boardSize, delimeter, playerNum):
        self.__playerNum = playerNum
        self.__CandLmap = {}
        self.__player_loc = {}

        super().__init__(boardSize, delimeter)

        self._initBoard()

    # PROPERTIES

    @property
    def CandLmap(self):
        return self.__CandLmap

    @property
    def PlayerLoc(self):
        return self.__player_loc

    # PUBLIC METHODS

    # Compute the location for current move and move player
    def makeMove(self, turn, spin):
        # get player pos
        pos_current = self.__player_loc[turn]
        pos_new = 100 if pos_current + spin > 100 else pos_current + spin

        # check for chute or ladder
        pos_new = self.__CandLmap.get(pos_new,pos_new)

        # remove old player location
        if pos_current > 0:
            self._updateBoard(pos_current, turn, False)
        
        # update player location
        self.__player_loc[turn] = pos_new
        self._updateBoard(pos_new, turn, True)

    # ensure move is valid
    def validateMove(self, turn, coord):
        pass

    # check for winner
    def checkWinner(self,turn):
        return self.__player_loc[turn] == 100

    # PROTECTED METHODS

    # initialize the game board and players
    def _initBoard(self):
        cellLength = 4 + self.__playerNum
        super()._initBoard(cellLength)

        # set players off the board
        for i in range(self.__playerNum):
            self.__player_loc[i] = 0
        
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
        
            self._updateBoard(key, labelKey)
            self._updateBoard(value, labelValue)

    # convert position into grid coordinates and update gameBoard
    def _updateBoard(self,position,label,isNewPos=False):
        gridCoord = self.__posToGrid(position)
        y = gridCoord[0]
        x = gridCoord[1]

        # if updating previous player position, look for player number to replace, 
        # else for new player position replace right most '-' with player number
        if str(label).isnumeric():
            if isNewPos:
                delimeter = self._delimeter
            else:
                delimeter = str(label)
                label = self._delimeter

            labelCur = self._gameBoard[y][x]

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
    def __posToGrid(self,position):
        # convert position to grid coordinates (remember board starts at (9,0), moves Left to Right and Up
        # and then Right to Left and Up
        y = self._boardSize - 1 - int((position-1) / self._boardSize)
        x = (position-1) % self._boardSize if y%2 else self._boardSize - 1 - ((position-1) % self._boardSize)

        return [y, x]

        
