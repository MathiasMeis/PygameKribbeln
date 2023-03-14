from button import Button
from imageHelper import ImageHelper
import os.path
import pygame

class MessageBoard:
    xCoordinate = 660
    yCoordinate = 390
    width = 600
    height = 300

    def __init__(self, messages : list[str], hasCloseButton : bool = True, hasButton : bool = False, buttonText : str = " ", buttonFontColor = (0,0,0), buttenImageName : str = "buttonWhite") -> None:
        self.messages : list[str] = messages
        self.hasButton : bool = hasButton
        self.button1 : Button = None
        self.hasCloseButton : bool = hasCloseButton
        self.closeButton : Button = None
        if(self.hasButton == True):
            self.button1 : Button = Button(MessageBoard.xCoordinate+200, MessageBoard.yCoordinate+275, 200, 50, buttonText, imageName=buttenImageName, color=buttonFontColor)
        if(self.hasCloseButton == True):
            self.closeButton : Button = Button(MessageBoard.xCoordinate+550, MessageBoard.yCoordinate, 50, 50, "", imageName="close")
    
    def draw(self, display) -> None:
        display.blit(pygame.image.load(os.path.join(ImageHelper.getMessageBoardIcon())),(MessageBoard.xCoordinate, MessageBoard.yCoordinate))
        for i in range(len(self.messages)):
            pygame.font.init()
            messageFont  = pygame.font.SysFont("comicsans", 30)
            meassageLabel = messageFont.render(self.messages[i], 1, (0,0,0))
            centering : int = (self.width/2) - (meassageLabel.get_width() /2)
            deviation : int = 50*i
            display.blit(meassageLabel, [self.xCoordinate+centering,450+deviation])
        if(self.hasButton):
            self.button1.draw(display)
        if(self.hasCloseButton):
            self.closeButton.draw(display)

    def checkForMouseLocationOnButton(self, xCoord, yCoord) -> bool:
        if (self.hasButton):
            return self.button1.checkForMouseInput(xCoord, yCoord)
        else:
            return False
        
    def checkForMouseLocationOnCloseButton(self, xCoord, yCoord) -> bool:
        if (self.hasCloseButton):
            return self.closeButton.checkForMouseInput(xCoord, yCoord)
        else:
            return False