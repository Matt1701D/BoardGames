from ChutesAndLadders import ChutesAndLadders
from TicTacToe import TicTacToe

class BoardGames(object):

    #initialize game
    def __init__(self):
        validGame = False
        while(not(validGame)):
            game = input("Which game would you like to play?\nTicTacToe: Enter 1\nChutes and Ladders: Enter 2\nQuit: Enter Q\nChoice: ")

            if game == 'Q' or game == 'q':
                break
            elif (not(game.isdigit())):
                print("Choice is not a number")
            elif int(game) not in [1,2]:   
                print("Choice must be 1 or 2")    
            elif int(game) == 1:
                myGame = TicTacToe.TicTacToe()
            else:
                myGame = ChutesAndLadders.ChutesAndLadders()

if __name__ == '__main__':
    myGame = BoardGames()

