from enum import Enum
import random

class Color(Enum):
    BLACK : str = "black"
    BLUE : str = "blue"
    GREEN : str = "green"
    ORANGE : str = "orange"
    PINK : str = "pink"
    YELLOW : str = "yellow"

    def getColors(numberOfColors) -> list:
        remainingColors : list = Color.getAllColors()
        colors : list = []
        index : int 
        for i in range(numberOfColors):
            index = random.randint(0, len(remainingColors)-1)
            colors.append(remainingColors[index])
            remainingColors.remove(remainingColors[index])
        return colors

    def getAllColors() -> list:
        return [Color.BLACK, Color.BLUE, Color.GREEN, Color.ORANGE, Color.PINK, Color.YELLOW]

    def getNumberOfColorInAllColors(color) -> int:
        allColors : list = Color.getAllColors()
        for i in range(6):
            if (allColors[i] == color):
                return i
        return -1