from color import Color
import pygame
import os


class ImageHelper:
    def getDieBackgroundColor(color : Color) -> pygame.Surface:
        ImageHelper.getImage("dice", f"dieColor{color.name}")

    def getDieNumberOverlay(value) -> pygame.Surface:
        ImageHelper.getImage("dice", f"dieValue{value}")

    def getTaskColor(color : Color):
        ImageHelper.getImage("tasks.colors", color.value)

    def getTaskNotAllowedColor(color : Color):
        None

    def getTaskNumber(number : int):
        None

    def getTaskOperator(operator : str): #  * < > = != &
        None

    def getTaskKribbel():
        None

    def getTaskNotAllowedOverlay():
        None

    def getEndPoints():
        None

    def getPoints(number):
        None

    def getNameLabel():
        None

    def getImage(folder : str, fileName : str) -> pygame.Surface:
        pygame.image.load(os.path.join(f"graphics\{folder}\{fileName}.png"))
