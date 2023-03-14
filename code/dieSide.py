from color import Color
from imageHelper import ImageHelper
import pygame

class DieSide:

    def __init__(self, value : int, color : Color) -> None:
        self.value : int = value
        self.color : Color = color
        self.colorPath : str = f"graphics\dice\dieColor{self.color.name}.png"
        self.valuePath : str = f"graphics\dice\dieValue{self.value}.png"
        self.image : pygame.Surface = ImageHelper.getDieNumberOverlay(self.value)

    def getValue(self) -> int:
        return self.value
    
    def getColor(self) -> Color:
        return self.color

    def getImage(self) -> pygame.Surface:
        return self.image