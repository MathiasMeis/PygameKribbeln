import Color
import Task
import Dice
import Difficulty


class Task_ColorX_greater_allOtherColors(Task):

    def __init__(self, numberOfFirstInstance, numberOfSecondInstance):
        self.difficulty = Difficulty.HARD

        self.colors = Color.getColors(1)

        
    def isCompleted(self, dice : Dice) -> bool:
        remainingColors : list = Color.getAllColors()
        remainingColors.remove(self.colors[0])
        isTrue : bool = True
        for i in range(len(remainingColors)-1):
            if (dice.getNumberOfColorInstances(self.colors[0]) <= dice.getNumberOfColorInstances(remainingColors[i])):
                return False
           
        return True

    def getInfo(self) -> str:
        return f"Get the color {self.colors[0]} more often than all the other colors."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()