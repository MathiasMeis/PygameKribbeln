import Color
import Task
import Dice
import Difficulty


class Task_anyColor_anyAnotherColor(Task):
    numberOfFirstInstance :int
    numberOfSecondInstance :int


    def __init__(self, first, second):
        self.numberOfFirstInstance = first
        self.numberOfSecondInstance = second
        self.difficulty = Difficulty.EASY

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
