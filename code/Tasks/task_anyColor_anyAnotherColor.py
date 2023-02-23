from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_anyColor_anyAnotherColor(Task):

    def __init__(self, first : int, second : int):
        super().__init__(0)
        self.numberOfFirstInstance : int = first
        self.numberOfSecondInstance : int = second
        self.difficulty : Difficulty = Difficulty.MEDIUM

    def isCompleted(self, dice : Dice) -> bool:
        firstIsTrue : bool = False
        secondIsTrue : bool = False
        allColors : list = Color.getAllColors()
        for i in range(6):
            if (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfFirstInstance):
                firstIsTrue = True
            elif (dice.getNumberOfColorInstances(allColors[i]) == self.numberOfSecondInstance):
                secondIsTrue = True

        return firstIsTrue and secondIsTrue
        
    def getInfo(self) -> str:
        return f"Get any Color {self.numberOfFirstInstance} times and another Color {self.numberOfSecondInstance} times."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()
