import Color
import Task
import Dice
import Difficulty


class Task_ColorX_greater_ColorY(Task):

    def __init__(self, numberOfFirstInstance, numberOfSecondInstance):
        self.difficulty = Difficulty.HARD
        self.requiredNumberOfFirstInstance = numberOfFirstInstance
        self.requiredNumberOfSecondInstance = numberOfSecondInstance

        self.colors = Color.getColors(2)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) > dice.getNumberOfColorInstances(self.colors[1])):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the color {self.colors[0]} more often than the color {self.colors[1]}."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()