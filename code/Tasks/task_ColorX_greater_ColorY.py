from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorX_greater_ColorY(Task):

    def __init__(self):
        super().__init__(2)
        self.difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) > dice.getNumberOfColorInstances(self.colors[1])):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the color {self.colors[0]} more often than the color {self.colors[1]}."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()