import Player
import Task
import ScoreBoard

#hier passiert die ganze magie, aber nichts mit ui
class Kribbeln:
    players : list
    scoreboard : ScoreBoard 

    def __init__(self, playerList): #hier werden die im startinscreen erstellen spieler übergeben
        self.players = playerList
        self.scoreboard = ScoreBoard(self.players)
