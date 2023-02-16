import Color
import Task
import Dice
import Difficulty


class Task_ColorXYZ_equal(Task):
    equal : bool

    def __init__(self, equalOrUnequal : bool):
        self.difficulty = Difficulty.HARD
        self.equal = equalOrUnequal
        self.colors = Color.getColors(2)


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