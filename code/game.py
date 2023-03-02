from dice import Dice
from scoreBoard import ScoreBoard
from gamestate import GameState
from player import Player


class Game:
    playingDice : Dice = Dice()
    scoreBoard : ScoreBoard = ScoreBoard()
    players : list[Player] = [Player("Player No. 1"), Player("Player No. 2")]
    numberOfPlayers : int = 2
    currentPlayerIndex : int = 0 #ggfs def dafür
    currentRound : int = 0
    currentState : GameState = GameState.STARTING
    remainingRorolls : int = 2



    def nextRound():
        if (Game.currentRound < len(ScoreBoard.tasks)):
            Game.currentRound += 1
        # end of game


    def nextPlayer():
        #Game.setPoints()
        if (Game.currentPlayerIndex<Game.numberOfPlayers -1):
            Game.currentPlayerIndex += 1
        else:
            Game.currentPlayerIndex = 0
            Game.nextRound()
        Game.remainingRorolls = 2 
        Game.playingDice.enableAllDice()
        Game.playingDice.reroll()

    def setPoints():
        ScoreBoard.setPoints(Game.playingDice, Game.currentPlayerIndex, Game.currentRound)      


    def getResultingPoints() -> int:
        if(ScoreBoard.tasks[Game.currentRound].isCompleted(Game.playingDice)):
            return Game.playingDice.getValues()
        else:
            return 0

    def getNextPlayerName() -> str:
        index = Game.currentPlayerIndex + 1
        if index >= Game.numberOfPlayers:
            index = 0
        return Game.players[index].getName()