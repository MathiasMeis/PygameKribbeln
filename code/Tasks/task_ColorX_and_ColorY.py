from dice import Dice
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player
from task import Task

class Task_ColorX_and_ColorY(Task):
    requiredNumberOfFirstInstance : int
    requiredNumberOfSecondInstance : int

    def __init__(self, numberOfFirstInstance, numberOfSecondInstance) -> None:
        super().__init__(2)
        self.requiredNumberOfFirstInstance = numberOfFirstInstance
        self.requiredNumberOfSecondInstance = numberOfSecondInstance
        if (numberOfFirstInstance < 2 and numberOfSecondInstance < 2):
            self.difficulty = Difficulty.EASY
        else:
            self.difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == self.requiredNumberOfFirstInstance and dice.getNumberOfColorInstances(self.colors[1]) == self.requiredNumberOfSecondInstance):
            return True
        else:
            return False
        
    def getInfo(self) -> list[str]:
        return [f"Get the color {self.colors[0].value} {Task.formatNumberOfInstances(self.requiredNumberOfFirstInstance)}", f"and the color {self.colors[1].value} {Task.formatNumberOfInstances(self.requiredNumberOfSecondInstance)}."]

    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        if (self.requiredNumberOfFirstInstance == 0):
            paths.append(ImageHelper.getTaskColor(self.colors[0]))
            paths.append(ImageHelper.getTaskNotAllowedColor(self.colors[0]))
        else:
            paths.append(ImageHelper.getTaskNumber(self.requiredNumberOfFirstInstance))
            paths.append(ImageHelper.getTaskOperator("*"))
            paths.append(ImageHelper.getTaskColor(self.colors[0]))
        paths.append(ImageHelper.getTaskOperator("&"))
        if (self.requiredNumberOfSecondInstance == 0):
            paths.append(ImageHelper.getTaskColor(self.colors[1]))
            paths.append(ImageHelper.getTaskNotAllowedColor(self.colors[1]))
        else:    
            paths.append(ImageHelper.getTaskNumber(self.requiredNumberOfSecondInstance))
            paths.append(ImageHelper.getTaskOperator("*"))
            paths.append(ImageHelper.getTaskColor(self.colors[1]))
        return paths

    def getIconDeviations(self) -> list[int]:
        if (self.requiredNumberOfFirstInstance == self.requiredNumberOfSecondInstance == 0):
            return [0,0,50,100,100]
        elif (self.requiredNumberOfFirstInstance == 0):
            return [0,0,50,100,150,200]
        elif (self.requiredNumberOfSecondInstance == 0):
            return [0,50,100,150,200,200]
        else:
            return [0,50,100,150,200,250,300]
        
    def getIconWidth(self) -> int:
        if (self.requiredNumberOfFirstInstance == self.requiredNumberOfSecondInstance == 0):
            return 150
        elif (self.requiredNumberOfFirstInstance == 0):
            return 250
        elif (self.requiredNumberOfSecondInstance == 0):
            return 250
        else:
            return 350