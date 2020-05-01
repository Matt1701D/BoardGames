from abc import ABC, abstractmethod

class Board(ABC):

    def __init__(self, boardSize, delimeter):
        self._boardSize = boardSize
        self._delimeter = delimeter
        self._gameBoard = []

        super().__init__()

    # PROPERTIES

    @property
    def GameBoard(self):
        return self._gameBoard

    # PROTECTED METHODS

    # initialize the game board and players
    @abstractmethod
    def _initBoard(self, length):
        self._gameBoard = [[self._delimeter*length] * self._boardSize for x in range(self._boardSize)]

    # update gameBoard
    @abstractmethod
    def _updateBoard(self, move, turn, isNewPos=False):
        pass

    # PUBLIC METHODS

    # make move on board
    @abstractmethod
    def makeMove(self, turn, move):
        pass

    # check if move is valid
    @abstractmethod
    def validateMove(turn, move):
        pass

    # check if game is won
    @abstractmethod
    def checkWinner(self, turn=0):
        pass

    # Print out game board
    def printBoard(self):
        for row in self._gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")


