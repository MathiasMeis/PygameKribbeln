import Color
import Task
import Dice
import Difficulty


class Task_2CX(Task): # 2 mal eine Farbe



    def __init__(self):
        self.difficulty = Difficulty.EASY
        self.colors = Color.getColors(1)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == 2):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the Color {self.colors[0]} 2 times."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
