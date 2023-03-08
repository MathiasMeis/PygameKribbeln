from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper
from player import Player


class Task_anyColor(Task): #  mal beliebige Farbe

    def __init__(self ,numberOfInstances : int, allowed : bool):
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
        return [f"Get any Color {Task.formatNumberOfInstances(self.numberOfInstances)}."]


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
            return [0,50,100,-25]
        
    def getIconWidth(self) -> int:
            if self.allowedToComplete:
                return 150
            else:
                return 200
