from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorXY_equal(Task):

    def __init__(self, equalOrUnequal : bool):
        super().__init__(2)
        self.equal : bool = equalOrUnequal
        self.difficulty : Difficulty = Difficulty.HARD


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[1]) == self.equal):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        if (self.equal):
            return f"Get the color {self.colors[0]} equally often as the color {self.colors[1]}."
        else:
            return f"Don't get the color {self.colors[0]} equally often as the color {self.colors[1]}."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()