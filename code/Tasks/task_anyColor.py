from color import Color
from dice import Dice
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player
from task import Task


class Task_anyColor(Task):

    def __init__(self ,numberOfInstances : int, allowed : bool) -> None:
        super().__init__(0)
        self.allowedToComplete = allowed
        self.numberOfInstances = numberOfInstances
        if (numberOfInstances < 3 and allowed):
            self.difficulty = Difficulty.EASY
        elif (numberOfInstances < 4):
            self.difficulty = Difficulty.MEDIUM
        else:
            self.difficulty = Difficulty.HARD
            

    def isCompleted(self, dice : Dice, player : Player) -> bool:
        allColors : list = Color.getAllColors()
        if(self.allowedToComplete):
            isTrue : bool = False
            for i in range(6):
                if (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfInstances):
                    isTrue = True
            return isTrue
        else:
            isTrue : bool = True
            for i in range(6):
                if (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfInstances):
                    isTrue = False
            return isTrue
        
    def getInfo(self) -> list[str]:
        if self.allowedToComplete:
            return [f"Get any color {Task.formatNumberOfInstances(self.numberOfInstances)}."]
        else:
            return [f"Don't get any color {Task.formatNumberOfInstances(self.numberOfInstances)}."]


#from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskNumber(self.numberOfInstances))
        paths.append(ImageHelper.getTaskOperator("*"))
        paths.append(ImageHelper.getAnyColor("any"))
        if(not self.allowedToComplete):
             paths.append(ImageHelper.getTaskBigNotAllowedOverlay())

        return paths


    def getIconDeviations(self) -> list[int]:
        if(self.allowedToComplete):
            return [0,50,100]
        else:
            return [0,50,100,0]
        
    def getIconWidth(self) -> int:
                return 150
