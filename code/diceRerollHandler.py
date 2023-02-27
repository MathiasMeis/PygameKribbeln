from dice import Dice
import pygame
from game import Game

class DiceRerollHandler:

    index: int = 0

    baseDicePos : int = [200,300]
    diceDistance : int = 250

    directionDown : bool = True

    def lowerIndex():
        if (DiceRerollHandler.index > 0):
            DiceRerollHandler.index -= 1

    def raiseIndex():
        if (DiceRerollHandler.index < 5):
            DiceRerollHandler.index += 1

    def getIndex():
        return DiceRerollHandler.index
    
    def setIndex(i):
        DiceRerollHandler.index = i

    def isArrowKey(key) -> bool:
        if key == pygame.K_UP:
            return True
        elif key == pygame.K_DOWN:
            return True
        elif key == pygame.K_LEFT:
            return True
        elif key == pygame.K_RIGHT:
            return True
        else:
            return False

    def handleKeyInput(key) -> None:
        if key == pygame.K_UP:
            Game.playingDice.toReroll[DiceRerollHandler.index] = True
        elif key == pygame.K_DOWN:
            Game.playingDice.toReroll[DiceRerollHandler.index] = False
        elif key == pygame.K_LEFT:
            DiceRerollHandler.lowerIndex()
        elif key == pygame.K_RIGHT:
            DiceRerollHandler.raiseIndex()

    def isInDice(self,mouse) -> bool:
        for i in range(6):
            xCoordinate : int = self.baseDicePos[0] + i*self.diceDistance
            yCoordinate : int = self.baseDicePos[1]  #TODO: hier irgendwas mit DiceRerollHandler.getIndex???
            if(Game.playingDice.toReroll[i] == False):
                yCoordinate += 300
            if xCoordinate <= mouse[0] <= xCoordinate+100 and yCoordinate <= mouse[1] <= yCoordinate+100:
                self.index = i
                return True
        return False
        
    def switchReroll():
        Game.playingDice.switchReroll(DiceRerollHandler.index)

    def getImagePath() -> str:
        indicator : str
        if(Game.playingDice.toReroll[DiceRerollHandler.index] == True):
            indicator = "Down"
        else:
            indicator = "Up"
        path : str = f"graphics\dice\diceHandler{indicator}.png"
        return path
    
    def getHoverPosition(self):
        xPos = self.baseDicePos[0] + self.index*self.diceDistance -50
        yPos = self.baseDicePos[1] + self.getHeightAddition() -100
        return [xPos,yPos]
    
    def getHeightAddition():
        if(Game.playingDice.toReroll[DiceRerollHandler.index] == True):
            return 0
        else:
            return 300