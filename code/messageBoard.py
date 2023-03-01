
from imageHelper import ImageHelper


class MessageBoard:


    def __init__(self, message : str, button1 : str, button2 : str = None, firstInRed : bool = False):
        self.message : str = message
        self.firstButton : str = button1
        self.secondButton : str = button2
        self.firstButtonIsRed : bool = firstInRed
        self.onlyOneButton : bool = False
        if(self.secondButton == None):
            self.onlyOneButton = True

    def getIconPaths(self) -> list[str]:
        paths : list[str] = []
        if(self.firstButtonIsRed):
            paths.append(ImageHelper.getRedButton())
        else:
            paths.append(ImageHelper.getWhiteButton())
        if(not self.onlyOneButton):
            paths.append(ImageHelper.getWhiteButton())
        return paths

    def getIconDeviation(self) -> list[int]:
        if(self.onlyOneButton):
            return [0]
        else:
            return [-150,150]
        
    def getButtonLabels(self) -> list[str]:
        labels : list[str] = []
        labels.append(self.firstButton)
        if(not self.onlyOneButton):
            labels.append(self.secondButton)
        return labels

    def getNumberOfButtons(self) -> int:
        if(self.secondButton == None):
            return 1
        else:
            return 2
    
    



        









