from dice import Dice
from imageHelper import ImageHelper
from player import Player
from task import Task

class Task_Kribbeln(Task):

    def __init__(self) -> None:
        super().__init__(0)

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (player.getHighestKribblePoints() < dice.getValues()):
            return True
        else:
            return False

    def getInfo(self) -> list[str]:
        return ["Get as many points as you want. If", "you already got points in a kribbeln task,", "you need to get even more points."]

    def getIconPaths(self) -> list[str]:
        return [ImageHelper.getImage("tasks", "kribbeln")]

    def getIconDeviations(self) -> list[int]:
        return [0]
    
    def getIconWidth(self) -> int:
        return 150