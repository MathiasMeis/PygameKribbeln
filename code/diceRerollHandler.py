from dice import Dice
import pygame
from kribbeln import Kribbeln

class DiceRerollHandler:

    index: int = 0

    baseDicePos : int = [550,420]
    diceDistance : int = 200

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
            Kribbeln.playingDice.toReroll[DiceRerollHandler.index] = True
        elif key == pygame.K_DOWN:
            Kribbeln.playingDice.toReroll[DiceRerollHandler.index] = False
        elif key == pygame.K_LEFT:
            DiceRerollHandler.lowerIndex()
        elif key == pygame.K_RIGHT:
            DiceRerollHandler.raiseIndex()

    def setIndexWithMouse(mouse) -> bool:
        for i in range(6):
            xCoordinate : int = DiceRerollHandler.baseDicePos[0] + i*DiceRerollHandler.diceDistance
            yCoordinate : int = DiceRerollHandler.baseDicePos[1]
            if(Kribbeln.playingDice.toReroll[i] == False):
                yCoordinate += 300
            if xCoordinate <= mouse[0] <= xCoordinate+100 and yCoordinate <= mouse[1] <= yCoordinate+100:
                DiceRerollHandler.index = i
                return True
        return False
        
    def switchReroll():
        Kribbeln.playingDice.switchReroll(DiceRerollHandler.index)

    def getImagePath() -> str:
        indicator : str
        if(Kribbeln.playingDice.toReroll[DiceRerollHandler.index] == True):
            indicator = "Down"
        else:
            indicator = "Up"
        path : str = f"graphics\dice\diceHandler{indicator}.png"
        return path
    
    def getHoverPosition():
        xPos = DiceRerollHandler.baseDicePos[0] + DiceRerollHandler.index*DiceRerollHandler.diceDistance -50
        yPos = DiceRerollHandler.baseDicePos[1] + DiceRerollHandler.getHeightAddition() -100
        return [xPos,yPos]
    
    def getHeightAddition():
        if(Kribbeln.playingDice.toReroll[DiceRerollHandler.index] == True):
            return 0
        else:
            return 300