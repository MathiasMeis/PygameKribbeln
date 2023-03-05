from color import Color
import pygame
import os


class ImageHelper:
    xCenter : int = 960

    def getDieBackgroundColor(color : Color) -> pygame.Surface:
        return ImageHelper.getImage("dice", f"dieColor{color.name}")

    def getDieNumberOverlay(value) -> pygame.Surface:
        return ImageHelper.getImage("dice", f"dieValue{value}")

    def getTaskColor(color : Color):
        return ImageHelper.getImage("tasks",f"Color{color.name}")

    def getTaskNotAllowedColor(color : Color):
        if (color == Color.BLACK):
            return ImageHelper.getImage("tasks", "NotOverlayBLACK")
        else:
            return ImageHelper.getImage("tasks", "NotOverlay")
        
    def getTaskNumber(number : int):
        return ImageHelper.getImage("tasks", f"Number{number}")
    
    def getCompletionIndicator(isCompleted : bool):
        #if(isCompleted):
        return ImageHelper.getImage("labels", f"taskCompletedIndicator{isCompleted}")

    def getTaskOperator(operator : str): #  * < > = != &
        if (operator == "&"):
            return ImageHelper.getImage("tasks", "OperatorAnd")
        elif (operator == "="):
            return ImageHelper.getImage("tasks", "OperatorEqual")
        elif (operator == "!="):
            return ImageHelper.getImage("tasks", "OperatorNotEqual")
        elif (operator == ">"):
            return ImageHelper.getImage("tasks", "OperatorGreater")
        elif (operator == "*"):
            return ImageHelper.getImage("tasks", "OperatorTimes")
        else:
            return ImageHelper.getImage("tasks", "error")
        
    def getAnyColor(color : str): #  * < > = != &
        if (color == "any"):
            return ImageHelper.getImage("tasks", "ColorAny")
        elif (color == "anyOther"):
            return ImageHelper.getImage("tasks", "ColorAnyOther")
        elif (color == "every"):
            return ImageHelper.getImage("tasks", "ColorEvery")
        elif (color == "1"):
            return ImageHelper.getImage("tasks", "Colors1")
        elif (color == "2"):
            return ImageHelper.getImage("tasks", "Colors2")
        elif (color == "3"):
            return ImageHelper.getImage("tasks", "Colors3")
        else:
            return ImageHelper.getImage("tasks", "error")

    def getTaskKribbel():
        None

    def getTaskBigNotAllowedOverlay():
        return ImageHelper.getImage("tasks", "notLong")
    
    def getTaskMinPrefix():
        return ImageHelper.getImage("tasks", "min")
    
    def getTaskTable():
        return ImageHelper.getImage("labels", "taskTable")
    
    def getUserIcon():
        return ImageHelper.getImage("tasks", "IconUser")

    def getEndPoints():
        None

    def getPoints(number):
        None

    def getNameLabel():
        None

    def getButton(name : str) -> str:
        return ImageHelper.getImage("buttons", name)

    def getExitButton() -> str:
        return ImageHelper.getImage("labels", "buttonExit")
    
    def getWhiteButton() -> str:
        return ImageHelper.getImage("labels", "buttonWhite")
    
    def getRedButton() -> str:
        return ImageHelper.getImage("labels", "buttonRed")

    def getMessageBoardIcon() -> str:
        return ImageHelper.getImage("labels", "messageBoard")

    def getBackground(name : str):
        return ImageHelper.getImage("background", name)

    def getImage(folder : str, fileName : str) -> str:
        return f"graphics\{folder}\{fileName}.png"
