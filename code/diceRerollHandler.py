from dice import Dice
import pygame
from game import Game

class DiceRerollHandler:

    index: int = 0

    directionDown : bool = True

    def lowerIndex():
        if (DiceRerollHandler.index > 0):
            DiceRerollHandler.index -= 1

    def raiseIndex():
        if (DiceRerollHandler.index < 5):
            DiceRerollHandler.index += 1

    def getIndex():
        return DiceRerollHandler.index

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

    def getImagePath() -> str:
        indicator : str
        if(Game.playingDice.toReroll[DiceRerollHandler.index] == True):
            indicator = "Down"
        else:
            indicator = "Up"
        path : str = f"graphics\dice\diceHandler{indicator}.png"
        return path
    
    def getHeightAddition():
        if(Game.playingDice.toReroll[DiceRerollHandler.index] == True):
            return 0
        else:
            return 300