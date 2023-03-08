from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper
from player import Player


class Task_ColorXYZ_equal(Task):

    def __init__(self, equalOrUnequal : bool):
        super().__init__(3)
        self.equal : bool = equalOrUnequal
        self.difficulty : Difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if ((dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[1])) == self.equal):
            if ((dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[2])) == self.equal):
                if ((dice.getNumberOfColorInstances(self.colors[1]) == dice.getNumberOfColorInstances(self.colors[2])) == self.equal):
                    return True
        
        return False
        
    def getInfo(self) -> list[str]:
        if (self.equal):
            return [f"Get the colors {self.colors[0].value}, {self.colors[1].value}", f"and {self.colors[2].value} equally often."]
        else:
            return [f"Don't get the colors {self.colors[0].value}, {self.colors[1].value}", f"and {self.colors[2].value} equally often."]

    #from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskColor(self.colors[0]))
        paths.append(ImageHelper.getTaskColor(self.colors[1]))
        paths.append(ImageHelper.getTaskColor(self.colors[2]))
        if (self.equal):
            paths.append(ImageHelper.getTaskOperator("="))
            paths.append(ImageHelper.getTaskOperator("="))
        else:
            paths.append(ImageHelper.getTaskOperator("!="))
            paths.append(ImageHelper.getTaskOperator("!="))
            
        return paths


    def getIconDeviations(self) -> list[int]:
            return [0,100,200,50,150]
        
    def getIconWidth(self) -> int:
            return 250