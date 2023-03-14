from dice import Dice
from gamestate import GameState
from player import Player
from scoreBoard import ScoreBoard

class Kribbeln:
    playingDice : Dice = Dice()
    players : list[Player] = [Player("Player 1"), Player("Player 2"), Player("Player 3")]
    scoreBoard : ScoreBoard = ScoreBoard(players)
    numberOfPlayers : int = len(players)
    currentPlayerIndex : int = 0
    currentRound : int = 0
    currentState : GameState = GameState.STARTING
    remainingRorolls : int = 2

    def lowerRerollCounter() -> None:
        Kribbeln.remainingRorolls -= 1

    def getRemainigRerolls() -> int:
        return Kribbeln.remainingRorolls

    def hasRemainingRerolls() -> bool:
        return Kribbeln.remainingRorolls > 0

    def reinit() -> None:
        Kribbeln.scoreBoard = ScoreBoard(Kribbeln.players)
        Kribbeln.playingDice.reroll()

    def addPlayer() -> None:
        Kribbeln.numberOfPlayers += 1
        Kribbeln.players.append(Player(f"Player {Kribbeln.numberOfPlayers}"))

    def removePlayer(index) -> None:
        Kribbeln.numberOfPlayers -= 1
        Kribbeln.players.remove(Kribbeln.players[index])

    def nextRound() -> None:
        Kribbeln.scoreBoard.updateResultingPoints(Kribbeln.currentRound)
        Kribbeln.scoreBoard.updateScore(Kribbeln.currentRound)
        if (Kribbeln.currentRound < len(Kribbeln.scoreBoard.tasks) - 1):
            Kribbeln.currentRound += 1
        else:
            Kribbeln.currentState = GameState.ENDING

    def nextPlayer() -> None:
        Kribbeln.setPoints()
        if (Kribbeln.currentPlayerIndex<Kribbeln.numberOfPlayers -1):
            Kribbeln.currentPlayerIndex += 1
        else:
            Kribbeln.currentPlayerIndex = 0
            Kribbeln.nextRound()
        Kribbeln.remainingRorolls = 2 
        Kribbeln.playingDice.enableAll()
        Kribbeln.playingDice.reroll()

    def setPoints() -> None:
        Kribbeln.scoreBoard.setPoints(Kribbeln.playingDice, Kribbeln.currentPlayerIndex, Kribbeln.currentRound)

    def getResultingPoints() -> int:
        if(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice, Kribbeln.players[Kribbeln.currentPlayerIndex])):
            return Kribbeln.playingDice.getValues()
        else:
            return 0

    def getNextPlayerName() -> str:
        index = Kribbeln.currentPlayerIndex + 1
        if index >= Kribbeln.numberOfPlayers:
            index = 0
        return Kribbeln.players[index].getName()