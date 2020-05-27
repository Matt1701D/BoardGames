from abc import ABC, abstractmethod     # Abstract class module
from MyLogger.MyLogger import MyLogger  # Logger module

# Board interface to be used for game board logic and manipulation
class Board(ABC):

    # CONSTRUCTOR

    @MyLogger.log_decorator
    def __init__(self, boardSize, delimeter):
        self._boardSize = boardSize     # Size of board, boards are squared
        self._delimeter = delimeter     # delimter used in board printout for empty spaces
        self._gameBoard = []            # the board itself as a list (will be 2-dim)

    # PROPERTIES

    @property
    def GameBoard(self):
        return self._gameBoard

    # PROTECTED METHODS

    @abstractmethod
    @MyLogger.log_decorator
    def _initBoard(self, length=1):
        """
        Initialize the game board using delimeter. Can specify length for to set number of delimeters in a cell
        """
        self._gameBoard = [[self._delimeter*length] * self._boardSize for x in range(self._boardSize)]

    # update gameBoard
    @abstractmethod
    def _updateBoard(self, turn, move, isNewPos=False):
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

    # always have cpu pick coord to win or block a win.
    @abstractmethod
    def getBestMove(self, turn=0):
        pass

    @MyLogger.log_decorator
    def printBoard(self):
        """
        Print out game board
        """
        for row in self._gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")


