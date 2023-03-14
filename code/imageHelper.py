from color import Color

class ImageHelper:
    xCenter : int = 960

    def getDieBackgroundColor(color : Color) -> str:
        return ImageHelper.getImage("dice", f"dieColor{color.name}")

    def getDieNumberOverlay(value) -> str:
        return ImageHelper.getImage("dice", f"dieValue{value}")

    def getTaskColor(color : Color) -> str:
        return ImageHelper.getImage("tasks",f"Color{color.name}")

    def getTaskNotAllowedColor(color : Color) -> str:
        if (color == Color.BLACK):
            return ImageHelper.getImage("tasks", "NotOverlayBLACK")
        else:
            return ImageHelper.getImage("tasks", "NotOverlay")
        
    def getTaskNumber(number : int) -> str:
        return ImageHelper.getImage("tasks", f"Number{number}")
    
    def getCompletionIndicator(isCompleted : bool) -> str:
        return ImageHelper.getImage("labels", f"taskCompletedIndicator{isCompleted}")

    def getTaskOperator(operator : str) -> str:
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
        
    def getAnyColor(color : str) -> str:
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

    def getTaskBigNotAllowedOverlay() -> str:
        return ImageHelper.getImage("tasks", "notLong")
    
    def getTaskMinPrefix() -> str:
        return ImageHelper.getImage("tasks", "min")
    
    def getTaskTable() -> str:
        return ImageHelper.getImage("labels", "taskTable")
    
    def getUserIcon() -> str:
        return ImageHelper.getImage("tasks", "IconUser")

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
