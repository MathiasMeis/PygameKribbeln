import Color
import Task
import Dice
import Difficulty


class Task_ColorXYZ_equal(Task):
    equal : bool

    def __init__(self, equalOrUnequal : bool):
        self.difficulty = Difficulty.HARD
        self.equal = equalOrUnequal
        self.colors = Color.getColors(3)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[1]) == self.equal):
            if (dice.getNumberOfColorInstances(self.colors[0]) == dice.getNumberOfColorInstances(self.colors[2]) == self.equal):
                if (dice.getNumberOfColorInstances(self.colors[1]) == dice.getNumberOfColorInstances(self.colors[2]) == self.equal):
                    return True
        
        return False
        
    def getInfo(self) -> str:
        if (self.equal):
            return f"Get the colors {self.colors[0]}, {self.colors[1]} and {self.colors[2]} equally often."
        else:
            return f"Don't get the colors {self.colors[0]}, {self.colors[1]} and {self.colors[2]} equally often."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()