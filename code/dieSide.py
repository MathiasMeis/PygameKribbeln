from color import Color


class DieSide:

    def __init__(self, value : int, color : Color) -> None:
        self.value : int = value
        self.color : Color = color

    def getValue(self) -> int:
        return self.value
    
    def getColor(self) -> Color:
        return self.color





