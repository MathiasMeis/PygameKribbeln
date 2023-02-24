from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_atLeast_ColorX(Task): # mindestens n mal eine Farbe
    requiredNumberOfInstances : int


    def __init__(self, number):
        super().__init__(1)
        self.requiredNumberOfInstances = number
        if(number < 3):
            self.difficulty = Difficulty.EASY
        else:
            self.difficulty = Difficulty.MEDIUM



    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) <= self.requiredNumberOfInstances):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the Color {self.colors[0]} at least {Task.formatNumberOfInstances(self.requiredNumberOfInstances)}."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
