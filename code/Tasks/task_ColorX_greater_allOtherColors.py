from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper
from player import Player


class Task_ColorX_greater_allOtherColors(Task):

    def __init__(self):
        super().__init__(1)
        self.difficulty = Difficulty.HARD


        
    def isCompleted(self, dice : Dice, player : Player) -> bool:
        remainingColors : list = Color.getAllColors()
        remainingColors.remove(self.colors[0])
        for i in range(len(remainingColors)-1):
            if (dice.getNumberOfColorInstances(self.colors[0]) <= dice.getNumberOfColorInstances(remainingColors[i])):
                return False
           
        return True

    def getInfo(self) -> list[str]:
        return [f"Get the color {self.colors[0].value} more often than all the other colors."]


#from imageHelper import ImageHelper
    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        paths.append(ImageHelper.getTaskColor(self.colors[0]))
        paths.append(ImageHelper.getTaskOperator(">"))
        paths.append(ImageHelper.getAnyColor("every"))

        return paths


    def getIconDeviations(self) -> list[int]:
            return [0,50,100]
        
    def getIconWidth(self) -> int:
            return 150