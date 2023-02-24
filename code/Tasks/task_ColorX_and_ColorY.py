from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorX_and_ColorY(Task):
    requiredNumberOfFirstInstance : int
    requiredNumberOfSecondInstance : int

    def __init__(self, numberOfFirstInstance, numberOfSecondInstance):
        super().__init__(2)
        self.requiredNumberOfFirstInstance = numberOfFirstInstance
        self.requiredNumberOfSecondInstance = numberOfSecondInstance
        if (numberOfFirstInstance < 2 and numberOfSecondInstance < 2):
            self.difficulty = Difficulty.EASY
        else:
            self.difficulty = Difficulty.MEDIUM

       


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == self.requiredNumberOfFirstInstance and dice.getNumberOfColorInstances(self.colors[1]) == self.requiredNumberOfSecondInstance):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the color {self.colors[0].value} {Task.formatNumberOfInstances(self.requiredNumberOfFirstInstance)} and the color {self.colors[1].value} {Task.formatNumberOfInstances(self.requiredNumberOfSecondInstance)}."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()

#from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        #paths.append(ImageHelper.getImage("tasks", "error"))
        return paths
        

    def getIconDeviations(self) -> list[int]:
        return [0]