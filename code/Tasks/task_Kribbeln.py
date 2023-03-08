from dice import Dice
from imageHelper import ImageHelper
from task import Task
from player import Player

#from player import Player

class Task_Kribbeln(Task): # 1 mal eine Farbe
    minimumPoints : int = 0

   # player : Player

    def __init__(self): #referenz auf player oder scoreboard
        super().__init__(0)

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (player.getHighestKribblePoints() < dice.getValues()):
            return True
        else:
            return False
        
    #def setPlayer(self, playerRef : Player):
    #    self.player = playerRef


    def getInfo(self) -> list[str]:
        return ["Get as many points as you want. If", "you already got points in a kribbeln task,", "you need to get even more points."]

    def getIconPaths(self) -> list[str]:
        return [ImageHelper.getImage("tasks", "kribbeln")]


    def getIconDeviations(self) -> list[int]:
        return [0]
    
    def getIconWidth(self) -> int:
        return 150