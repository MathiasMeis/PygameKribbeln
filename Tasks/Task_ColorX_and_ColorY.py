import Color
import Task
import Dice
import Difficulty


class Task_nCX_mCY(Task): # 2 mal eine Farbe, 2 mal eine andere Farbe
    requiredNumberOfFirstInstance : int
    requiredNumberOfSecondInstance : int

    def __init__(self, numberOfFirstInstance, numberOfSecondInstance):
        self.difficulty = Difficulty.EASY
        self.requiredNumberOfFirstInstance = numberOfFirstInstance
        self.requiredNumberOfSecondInstance = numberOfSecondInstance

        self.colors = Color.getColors(2)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == 2, dice.getNumberOfColorInstances(self.colors[1]) == 2):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the color {self.colors[0]} 2 time and the color {self.colors[1]} 2 times."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()