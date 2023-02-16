import Color
import Task
import Dice
import Difficulty


class Task_ColorX(Task): # n mal eine Farbe
    requiredNumberOfInstandes : int


    def __init__(self, number, difficuly):
        self.requiredNumberOfInstandes = number
        self.difficulty = difficuly
        self.colors = Color.getColors(1)


    def isCompleted(self, dice : Dice) -> bool:
        if (dice.getNumberOfColorInstances(self.colors[0]) == self.requiredNumberOfInstandes):
            return True
        else:
            return False
        
    def getInfo(self) -> str:
        if (self.requiredNumberOfInstandes == 1):
            return f"Get the Color {self.colors[0]} 1 time."
        else:
            return f"Get the Color {self.colors[0]} {self.requiredNumberOfInstandes} times."



    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()