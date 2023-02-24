from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorXYZ_equal(Task):

    def __init__(self, equalOrUnequal : bool):
        super().__init__(2)
        self.equal : bool = equalOrUnequal
        self.difficulty : Difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[1]) == self.equal):
            if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[2]) == self.equal):
                if (dice.getNumberOfColorInstances(self.colors[1]) == dice.getNumberOfColorInstances(self.colors[2]) == self.equal):
                    return True
        
        return False
        
    def getInfo(self) -> str:
        if (self.equal):
            return f"Get the colors {self.colors[0].value}, {self.colors[1].value} and {self.colors[2].value} equally often."
        else:
            return f"Don't get the colors {self.colors[0].value}, {self.colors[1].value} and {self.colors[2].value} equally often."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()