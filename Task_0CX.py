import Task
import Difficulty
import Color
import Dice


class Task_0CX(Task): # 0 mal eine Farbe



    def __init__(self):
        self.difficulty = Difficulty.EASY
        self.colors = Color.getColors(1)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == 0):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the Color {self.colors[0]} 0 times."


    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
















