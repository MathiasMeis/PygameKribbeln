from color import Color
import pygame
from imageHelper import ImageHelper


class DieSide:

    def __init__(self, value : int, color : Color) -> None:
        self.value : int = value
        self.color : Color = color

        self.colorPath : str = f"graphics\dice\dieColor{self.color.name}.png"
        self.valuePath : str = f"graphics\dice\dieValue{self.value}.png"
        self.image : pygame.Surface = ImageHelper.getDieNumberOverlay(self.value)
        #dieOverlay : pygame.surface.Surface = ImageHelper.getDieNumberOverlay(self.value)
        #self.image : pygame.image = ImageHelper.getDieBackgroundColor(self.color)
        #backgroundColor : pygame.surface.Surface = ImageHelper.getDieBackgroundColor(self.color)
        #backgroundColor.blit(dieOverlay, (0, 0))
        #self.image = backgroundColor
        #self.image : pygame.image = backgroundColor.copy()
        #self.image.blit(dieOverlay, (0,0))

    def getValue(self) -> int:
        return self.value
    
    def getColor(self) -> Color:
        return self.color

    def getImage(self) -> pygame.Surface:
        return self.image

