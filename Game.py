from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, turn, boardSize, delimeter):
        self.turn = turn
        self.boardSize = boardSize
        self.delimeter = delimeter

        #self.board = globals()[boardClass]()

    @abstractmethod
    def _playGame(self):
        pass
