from color import Color
from dice import Dice
from difficulty import Difficulty
from task import Task
from imageHelper import ImageHelper


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
        
    def getInfo(self) -> list[str]:
        return [f"Get the color {self.colors[0].value} {Task.formatNumberOfInstances(self.requiredNumberOfInstandes)}."]



    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()


    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        if (self.requiredNumberOfInstandes == 0):
            paths.append(ImageHelper.getTaskColor(self.colors[0]))
            paths.append(ImageHelper.getTaskNotAllowedColor(self.colors[0]))
        else:
            paths.append(ImageHelper.getTaskNumber(self.requiredNumberOfInstandes))
            paths.append(ImageHelper.getTaskOperator("*"))
            paths.append(ImageHelper.getTaskColor(self.colors[0]))
            
        return paths


    def getIconDeviations(self) -> list[int]:
        if (self.requiredNumberOfInstandes == 0):
            return [0,0]
        else:
            return [0,50,100]
        
    def getIconWidth(self) -> int:
        if (self.requiredNumberOfInstandes == 0):
            return 50
        else:
            return 150
