from imageHelper import ImageHelper
import pygame
import os.path

class Button:
    pygame.font.init()
    bigFont  = pygame.font.SysFont("comicsans", 50)
    mediumFont  = pygame.font.SysFont("comicsans", 30)
    smallFont  = pygame.font.SysFont("comicsans", 20)



    def __init__(self, xCoordinate : int, yCoordinate : int, width : int, height : int, label : str, imageName : str = "buttonWhite" , color = (0,0,0), scale : float = 1, fontSize : str = 30):
        self.xCoordinate : int = xCoordinate
        self.yCoordinate : int = yCoordinate
        self.width : int = width
        self.height : int = height
        self.label : str = label
        self.color = color
        self.scale : float = 1.0
        self.imagePath = ImageHelper.getButton(imageName)
        self.fontSize : int = fontSize



    def draw(self, display) -> None:
        halfScale : float = (self.scale/2) - 0.5
        OGpic = pygame.image.load(os.path.join(self.imagePath))
        pic = pygame.transform.scale(OGpic,(self.width*self.scale,self.height*self.scale))
        display.blit(pic,(self.xCoordinate-(self.width*(halfScale)), self.yCoordinate-(self.height*(halfScale))))

        pygame.font.init()
        xfont  = pygame.font.SysFont("comicsans", int(self.fontSize*self.scale))
        buttonLabel = xfont.render(self.label, 1, self.color)
        xCentering : int = (self.width/2) - (buttonLabel.get_width() /2)
        yCentering : int = (self.height/2) - (buttonLabel.get_height() /2)
        display.blit(buttonLabel, [self.xCoordinate+xCentering,self.yCoordinate+yCentering])

        #display.blit(pygame.image.load(os.path.join(self.imagePath)),(self.xCoordinate, self.yCoordinate))


    def mouseIsIn(self, xCoord : int, yCoord : int) -> bool:
        if (self.xCoordinate-(self.width*(self.scale-1)) <= xCoord <= self.xCoordinate+(self.width*(self.scale))):
            if(self.yCoordinate-(self.height*(self.scale-1)) <= yCoord <= self.yCoordinate+(self.height*(self.scale))):
                self.scale = 1.1
                return True

        self.scale = 1.0
        return False

