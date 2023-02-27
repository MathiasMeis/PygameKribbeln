from difficulty import Difficulty
from color import Color
from imageHelper import ImageHelper

# Oberklasse für alle Tasks, namensgebung für unterklassen noch fragwürdig
# unterklassen sollten alle 4 mothoden überschreiben, letztere kann erstmal warten
class Task:
    difficulty : Difficulty = Difficulty.NONE

    def __init__(self, numberOfRequiredColors : int):
        self.colors : list[Color] = Color.getColors(numberOfRequiredColors)

    def isCompleted(self, dice) -> bool: #override
        return False
    
    def getInfo(self) -> str: #falls wir nen infopanel zum drüberhovern machen sollten, oben im default screen, nicht unbedingt scoreboard
        return " "

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        pass

    def formatNumberOfInstances(number : int) -> str:
        if (number == 1):
            return f"{number} time"
        else: 
            return f"{number} times"
        
    def getIconPaths() -> list[str]:
        return [ImageHelper.getImage("tasks", "error")]


    def getIconDeviations() -> list[int]:
        return [0]
    
    def getIconWidth() -> int:
        return 50