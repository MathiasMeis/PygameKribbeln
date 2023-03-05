from dice import Dice
from scoreBoard import ScoreBoard
from gamestate import GameState
from player import Player


class Kribbeln:
    playingDice : Dice = Dice()
    players : list[Player] = [Player("Player No. 1"), Player("Player No. 2"), Player("Player No. 3")]
    scoreBoard : ScoreBoard = ScoreBoard(players)
    numberOfPlayers : int = len(players)
    currentPlayerIndex : int = 0
    currentRound : int = 0
    currentState : GameState = GameState.STARTING
    remainingRorolls : int = 2


    def lowerRerollCounter():
        Kribbeln.remainingRorolls -= 1

    def getRemainigRerolls() -> int:
        return Kribbeln.remainingRorolls

    def hasRemainingRerolls() -> bool:
        return Kribbeln.remainingRorolls > 0


    def nextRound():
        Kribbeln.scoreBoard.updateResultingPoints(Kribbeln.currentRound)
        Kribbeln.scoreBoard.updateScore(Kribbeln.currentRound)
        if (Kribbeln.currentRound < len(Kribbeln.scoreBoard.tasks) - 1):
            Kribbeln.currentRound += 1
        else:
            Kribbeln.currentState = GameState.ENDING
        # end of game


    def nextPlayer():
        Kribbeln.setPoints()
        if (Kribbeln.currentPlayerIndex<Kribbeln.numberOfPlayers -1):
            Kribbeln.currentPlayerIndex += 1
        else:
            Kribbeln.currentPlayerIndex = 0
            Kribbeln.nextRound()
        Kribbeln.remainingRorolls = 2 
        Kribbeln.playingDice.enableAllDice()
        Kribbeln.playingDice.reroll()

    def setPoints():
        Kribbeln.scoreBoard.setPoints(Kribbeln.playingDice, Kribbeln.currentPlayerIndex, Kribbeln.currentRound)
        print(Kribbeln.scoreBoard.points)    


    def getResultingPoints() -> int:
        if(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice)):
            return Kribbeln.playingDice.getValues()
        else:
            return 0

    def getNextPlayerName() -> str:
        index = Kribbeln.currentPlayerIndex + 1
        if index >= Kribbeln.numberOfPlayers:
            index = 0
        return Kribbeln.players[index].getName()