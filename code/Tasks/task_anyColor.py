from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_anyColor(Task): #  mal beliebige Farbe
    allowedToComplete : bool
    numberOfInstances : int

    def __init__(self ,numberOfInstances : int, allowed : bool):
        super().__init__(0)
        self.allowedToComplete = allowed
        self.numberOfInstances = numberOfInstances
        if (numberOfInstances < 3 and allowed):
            self.difficulty = Difficulty.EASY
        elif (numberOfInstances < 4):
            self.difficulty = Difficulty.MEDIUM
        else:
            self.difficulty = Difficulty.HARD
            

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
