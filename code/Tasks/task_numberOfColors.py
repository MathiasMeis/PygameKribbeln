from dice import Dice
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player
from task import Task

class Task_numberOfColors(Task):

    def __init__(self, numberofAllowedColors : int) -> None:
        super().__init__(0)
        self.numberOfAllowedColors : int = numberofAllowedColors
        self.difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (dice.getNumberOfColors() == self.numberOfAllowedColors):
            return True
        else:
            return False
        
    def getInfo(self) -> list[str]:
        return [f"Get {self.numberOfAllowedColors} colors only."]

    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getAnyColor("1"))
        if (self.numberOfAllowedColors == 3):
            paths.append(ImageHelper.getAnyColor("2"))
        paths.append(ImageHelper.getAnyColor("3"))
        return paths

    def getIconDeviations(self) -> list[int]:
        if (self.numberOfAllowedColors == 3):
            return [0,50,100]
        else:
            return [0,50]
        
    def getIconWidth(self) -> int:
        if (self.numberOfAllowedColors == 3):
            return 150
        else:
            return 100