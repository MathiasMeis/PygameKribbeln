from dice import Dice
from scoreBoard import ScoreBoard
from startingScreen import StartingScreen


class Game:
    playingDice : Dice = Dice()
    scoreBoard : ScoreBoard = ScoreBoard()
    currentPlayerIndex : int = 0 #ggfs def dafür
    currentRound : int = 0

    def start():
        print("Let's go")

    def showCurrentTask():
        print(Game.scoreBoard.tasks[Game.currentRound].getInfo())

    def enableAll():
        Game.playingDice.toReroll = [True, True, True, True, True, True]


def nextRound():
    if (Game.currentRound < len(ScoreBoard.tasks)):
        Game.currentRound += 1
    # end of game


def nextPlayer():
    setPoints()
    if (Game.currentPlayerIndex<StartingScreen.numberOfPlayers -1):
        Game.currentPlayerIndex += 1
    else:
        Game.currentPlayerIndex = 0
        Game.nextRound()

def setPoints():
    ScoreBoard.setPoints(Game.playingDice, Game.currentPlayerIndex, Game.currentRound)      


#print(Game.playingDice.getValues())
##print(Game.playingDice.dieBlack.currentSide.getColor().name)

#print("this is game")
#enableAll()
#Game.playingDice.show()
#Game.playingDice.reroll()
#Game.playingDice.show()
#Game.playingDice.toReroll = [True, True, True, False, False, False]
#Game.playingDice.reroll()
#Game.playingDice.show()


#print(Game.playingDice.dieBlack.currentSide.getColor().name)

#print(Game.playingDice.getValues())




