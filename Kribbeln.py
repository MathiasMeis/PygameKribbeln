import Player
import Dice
import Task
import ScoreBoard
import StartingScreen

#hier passiert die ganze magie, aber nichts mit ui. Die Spielefunktionen
class Kribbeln:
    players : list
    scoreboard : ScoreBoard 
    currentDice : Dice
    currentTask : Task
    currentPlayer: int
    currentRound: int

    def __init__(self, playerList): #hier werden die im startinscreen erstellen spieler übergeben
        self.players = playerList
        self.scoreboard = ScoreBoard(self.players)

    def getPlayer(self) -> Player:
        return self.players[self.currentPlayer]

    def nextTurn(self):
        self.currentDice.reroll()

    def addScore(self):
        if self.currentTask.isCompleted(self.currentDice):
            self.scoreboard.setpoints(self.getPlayer(),self.currentRound,self.currentDice.getValues())
        else: 
            self.scoreboard.setpoints(self.getPlayer(),self.currentRound,0)
    
    def nextPlayer(self) -> Player:
        self.currentPlayer = self.currentPlayer + 1
        return self.getPlayer()

    def nextRound(self):
        self.currentRound = self.currentRound +1
        self.currentTask = self.scoreboard.getNextTask()
        #sort players?
    