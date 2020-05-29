import unittest
from GameCenter import GameFactory
from ChutesAndLadders.ChutesAndLadders import ChutesAndLadders

class Test_GameCenter(unittest.TestCase):
    def test_AddGame(self):
        #Arrange
        expCount = 1

        #Act
        GameFactory.registerGame("test")
        actCount = len(GameFactory.games)

        #Assert
        self.assertEqual(actCount,expCount,"Wrong count of board games")

    def test_LoadGame(self):
        #Arrange
        expGame = "ChutesAndLadders"

        #Act
        GameFactory.registerGame(expGame)
        actGame = GameFactory.getGame(0)

        #Assert
        self.assertEqual(actGame,expGame,"Game name not correct")
        self.assertIn(expGame, globals(),"Could not find game class")

if __name__ == '__main__':
    unittest.main()
