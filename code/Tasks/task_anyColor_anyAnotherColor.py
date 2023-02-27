from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper


class Task_anyColor_anyAnotherColor(Task):

    def __init__(self, first : int, second : int):
        super().__init__(0)
        self.numberOfFirstInstance : int = first
        self.numberOfSecondInstance : int = second
        self.difficulty : Difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice) -> bool:
        firstIsTrue : bool = False
        secondIsTrue : bool = False
        allColors : list = Color.getAllColors()
        for i in range(6):
            if (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfFirstInstance and not firstIsTrue):
                firstIsTrue = True
            elif (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfSecondInstance):
                secondIsTrue = True

        return firstIsTrue and secondIsTrue
        
    def getInfo(self) -> str:
        return f"Get any Color {Task.formatNumberOfInstances(self.numberOfFirstInstance)} and another Color {Task.formatNumberOfInstances(self.numberOfSecondInstance)}."

#from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskNumber(self.numberOfFirstInstance))
        paths.append(ImageHelper.getTaskOperator("*"))
        paths.append(ImageHelper.getAnyColor("any"))
        paths.append(ImageHelper.getTaskOperator("&"))
        paths.append(ImageHelper.getTaskNumber(self.numberOfSecondInstance))
        paths.append(ImageHelper.getTaskOperator("*"))
        paths.append(ImageHelper.getAnyColor("anyOther"))

        return paths


    def getIconDeviations(self) -> list[int]:
            return [0,50,100,150,200,250,300]
        
    def getIconWidth(self) -> int:
            return 350