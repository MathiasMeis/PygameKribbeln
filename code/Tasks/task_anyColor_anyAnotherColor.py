from color import Color
from dice import Dice
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player
from task import Task

class Task_anyColor_anyAnotherColor(Task):

    def __init__(self, first : int, second : int) -> None:
        super().__init__(0)
        self.numberOfFirstInstance : int = first
        self.numberOfSecondInstance : int = second
        self.difficulty : Difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        firstIsTrue : bool = False
        secondIsTrue : bool = False
        allColors : list = Color.getAllColors()
        for i in range(6):
            if (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfFirstInstance and not firstIsTrue):
                firstIsTrue = True
            elif (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfSecondInstance):
                secondIsTrue = True
        return firstIsTrue and secondIsTrue
        
    def getInfo(self) -> list[str]:
        return [f"Get any color {Task.formatNumberOfInstances(self.numberOfFirstInstance)}", f"and another color {Task.formatNumberOfInstances(self.numberOfSecondInstance)}."]

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