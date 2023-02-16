import Color
import Task
import Dice
import Difficulty


class Task_min2CX(Task): # 3 Farben
    


    def __init__(self):
        self.difficulty = Difficulty.MEDIUM


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberofColors == 3):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return "Get 3 Colors only."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
