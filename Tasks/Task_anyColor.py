import Color
import Task
import Dice
import Difficulty


class Task_anyColor(Task): #  mal beliebige Farbe
    allowedToComplete : bool
    numberOfInstances : int

    def __init__(self ,numberOfInstances : int, allowed : bool):
        self.allowedToComplete = allowed
        self.numberOfInstances = numberOfInstances
        self.difficulty = Difficulty.EASY #change

    def isCompleted(self, dice : Dice) -> bool:
        isTrue : bool = False
        allColors : list = Color.getAllColors()
        for i in range(6):
            if (dice.getNumberOfColorInstances(allColors[i]) == 3):
                isTrue = True
        return isTrue
        
    def getInfo(self) -> str:
        if (self.allowedToComplete):
            return f"Get any Color {self.numberOfInstances} times."
        else:
            return f"Don't get any Color {self.numberOfInstances} times."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
