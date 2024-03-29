from dice import Dice
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player
from task import Task

class Task_atLeast_ColorX(Task):
    requiredNumberOfInstances : int

    def __init__(self, number) -> None:
        super().__init__(1)
        self.requiredNumberOfInstances = number
        if(number < 3):
            self.difficulty = Difficulty.EASY
        else:
            self.difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (self.requiredNumberOfInstances <= dice.getNumberOfColorInstances(self.colors[0])):
            return True
        else:
            return False
        
    def getInfo(self) -> list[str]:
        return [f"Get the color {self.colors[0].value} at least {Task.formatNumberOfInstances(self.requiredNumberOfInstances)}."]

    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskMinPrefix())
        paths.append(ImageHelper.getTaskNumber(self.requiredNumberOfInstances))
        paths.append(ImageHelper.getTaskOperator("*"))
        paths.append(ImageHelper.getTaskColor(self.colors[0]))
        return paths

    def getIconDeviations(self) -> list[int]:
            return [0,100,150,200]
        
    def getIconWidth(self) -> int:
            return 250