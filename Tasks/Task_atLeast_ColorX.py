import Color
import Task
import Dice
import Difficulty


class Task_min_nCX(Task): # mindestens n mal eine Farbe
    requiredNumberOfInstances : int


    def __init__(self, number):
        self.requiredNumberOfInstances = number
        self.difficulty = Difficulty.EASY
        self.colors = Color.getColors(1)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) <= self.requiredNumberOfInstances):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the Color {self.colors[0]} at least 2 times."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
