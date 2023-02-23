from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_numberOfColors(Task): # 3 Farben
    


    def __init__(self, numberofAllowedColors : int):
        super().__init__(0)
        self.numberOfAllowedColors : int = numberofAllowedColors
        self.difficulty = Difficulty.MEDIUM


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberofColors == self.numberOfAllowedColors):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get {self.numberOfAllowedColors} Colors only."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
