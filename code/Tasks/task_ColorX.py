from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task


class Task_ColorX(Task): # n mal eine Farbe
    requiredNumberOfInstandes : int


    def __init__(self, number):
        super().__init__(1)
        self.requiredNumberOfInstandes = number
        if(number < 3):
            self.difficulty = Difficulty.EASY
        else:
            self.difficulty = Difficulty.MEDIUM



    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == self.requiredNumberOfInstandes):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        return f"Get the Color {self.colors[0]} {Task.formatNumberOfInstances(self.requiredNumberOfInstandes)}."



    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()