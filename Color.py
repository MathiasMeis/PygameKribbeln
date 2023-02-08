from enum import Enum

class Color(Enum):
    BLACK = ("BLACK", "#000000")
    BLUE = ("BLUE", "#000000")
    GREEN = ("GREEN", "#000000")
    ORANGE = ("ORNAGE", "#000000")
    PINK = ("PINK", "#000000")
    YELLOW = ("YELLOW", "#000000")

    def getColors(numberOfColors) -> list:
        return [Color.BLACK,Color.YELLOW] #TODO random colors, length = numberOfColors

    def getPicture(self):
        print("kk")
        # über path bild bekommmen, name ist teil des path zB: d/users/xx/python/pics/Color_BLACK.png

    