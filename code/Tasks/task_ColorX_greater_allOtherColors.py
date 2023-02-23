from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorX_greater_allOtherColors(Task):

    def __init__(self):
        super().__init__(1)
        self.difficulty = Difficulty.HARD


        
    def isCompleted(self, dice : Dice) -> bool:
        remainingColors : list = Color.getAllColors()
        remainingColors.remove(self.colors[0])
        for i in range(len(remainingColors)-1):
            if (dice.getNumberOfColorInstances(self.colors[0]) <= dice.getNumberOfColorInstances(remainingColors[i])):
                return False
           
        return True

    def getInfo(self) -> str:
        return f"Get the color {self.colors[0]} more often than all the other colors."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()