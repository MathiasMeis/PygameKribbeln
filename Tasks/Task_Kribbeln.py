import Color
import Task
import Dice
import Difficulty
import ScoreBoard
import Player

class Task_Kribbeln(Task): # 1 mal eine Farbe

    player : Player

    def __init__(self): #referenz auf player oder scoreboard
        self.difficulty = Difficulty.NONE

    def isCompleted(self, dice : Dice) -> bool:
        if (self.player.getHighestKribblePoints() < dice.getValues()):
            return True
        else:
            return False
        
    def setPlayer(self, playerRef):
        self.player = playerRef


    def getInfo(self) -> str:
        if (self.player is not None and self.player.getHighestKribblePoints() == 0):
            return "Get as many points as you want. But you need to top it later on."
        else:
            return f"Get at least {self.player.getHighestKribblePoints() + 1} points."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()