from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper
from player import Player

class Task_ColorX_greater_ColorY(Task):

    def __init__(self):
        super().__init__(2)
        self.difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) > dice.getNumberOfColorInstances(self.colors[1])):
            return True
        else:
            return False
        
    def getInfo(self) -> list[str]:
        return [f"Get the color {self.colors[0].value} more often", f"than the color {self.colors[1].value}."]


#from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskColor(self.colors[0]))
        paths.append(ImageHelper.getTaskOperator(">"))
        paths.append(ImageHelper.getTaskColor(self.colors[1]))

        return paths


    def getIconDeviations(self) -> list[int]:
            return [0,50,100]
        
    def getIconWidth(self) -> int:
            return 150