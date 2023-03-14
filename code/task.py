from color import Color
from difficulty import Difficulty
from imageHelper import ImageHelper
from player import Player

class Task:
    difficulty : Difficulty = Difficulty.NONE

    def __init__(self, numberOfRequiredColors : int):
        self.colors : list[Color] = Color.getColors(numberOfRequiredColors)

    def isCompleted(self, dice, player : Player) -> bool:
        return False
    
    def getInfo(self) -> list[str]:
        return " "

    def formatNumberOfInstances(number : int) -> str:
        if (number == 1):
            return f"{number} time"
        else: 
            return f"{number} times"
        
    def getIconPaths(self) -> list[str]:
        return [ImageHelper.getImage("tasks", "error")]

    def getIconDeviations(self) -> list[int]:
        return [0]
    
    def getIconWidth(self) -> int:
        return 50