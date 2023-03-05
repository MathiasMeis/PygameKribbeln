from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper


class Task_ColorXY_equal(Task):

    def __init__(self, equalOrUnequal : bool):
        super().__init__(2)
        self.equal : bool = equalOrUnequal
        self.difficulty : Difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[1])):
            return self.equal
        else:
            return not self.equal
        
    def getInfo(self) -> list[str]:
        if (self.equal):
            return [f"Get the color {self.colors[0].value} equally often as the color {self.colors[1].value}."]
        else:
            return [f"Don't get the color {self.colors[0].value} equally often as the color {self.colors[1].value}."]

    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskColor(self.colors[0]))
        paths.append(ImageHelper.getTaskColor(self.colors[1]))
        if (self.equal):
            paths.append(ImageHelper.getTaskOperator("="))
        else:
            paths.append(ImageHelper.getTaskOperator("!="))
            
        return paths


    def getIconDeviations(self) -> list[int]:
            return [0,100,50]
        
    def getIconWidth(self) -> int:
            return 150