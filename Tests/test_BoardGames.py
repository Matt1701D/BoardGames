import unittest
from BoardGames import GameFactory
from ChutesAndLadders.ChutesAndLadders import ChutesAndLadders

class Test_BoardGames(unittest.TestCase):
    def test_AddGame(self):
        #Arrange
        expCount = 1

        #Act
        GameFactory.registerGame(1,"Test")
        actCount = len(GameFactory.games)

        #Assert
        self.assertEqual(actCount,expCount,"Wrong count of board games")

if __name__ == '__main__':
    unittest.main()
