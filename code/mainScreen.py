import pygame
import os
from scoreBoard import ScoreBoard
from color import Color
from game import Game
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper
#Hier wird der ui stuff für das Würfel
throwButtonPos = [300, 500, 200, 100]
throwLabelPos = [340,500]
turnButtonPos = [600, 500, 350, 100]
turnLabelPos = [620,500]

pygame.font.init()
font  = pygame.font.SysFont("comicsans", 70)
smallFont  = pygame.font.SysFont("comicsans", 30)
throwLabel = font.render("Roll", 1, (255, 255, 255))
turnLabel = font.render("New Turn", 1, (255, 255, 255))

def inThrowButton(x,y):
    if throwButtonPos[0] <= x <= throwButtonPos[0]+throwButtonPos[2] and throwButtonPos[1] <= y <= throwButtonPos[1]+throwButtonPos[3]: return True
    else: return False

def inTurnButton(x,y):
    if turnButtonPos[0] <= x <= turnButtonPos[0]+turnButtonPos[2] and turnButtonPos[1] <= y <= turnButtonPos[1]+turnButtonPos[3]: return True
    else: return False

def mightBeDieStateChange(x,y) -> bool:
    if():
        return True
    else:
        return False
    





def drawThrowButton(display,mouse):
    if inThrowButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), throwButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), throwButtonPos)
    display.blit(throwLabel, throwLabelPos)
    #Hier später einfach Bild von Button Neuer Wurf rein

def drawNewTurnButton(display,mouse): # kann erstmal für testzecke so bleiben
    if inTurnButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), turnButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), turnButtonPos)
    display.blit(turnLabel, turnLabelPos)
    #Hier später einfach Bild von Button Neuer Zug rein

def drawDices(display,number):
    baseXCoordinate : int = 500
    baseYCoordinate : int = 400
    deviation : int = 250
    for i in range(6):
        xCoordinate = baseXCoordinate + i*deviation
        yCoordinate = baseYCoordinate
        if(Game.playingDice.toReroll[i] == False):
            yCoordinate += 300
        display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getColorPath())),(xCoordinate, yCoordinate))
        display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getValuePath())),(xCoordinate, yCoordinate))
    xCo : int = baseXCoordinate + deviation*DiceRerollHandler.getIndex() - 50
    yCo : int = baseYCoordinate + DiceRerollHandler.getHeightAddition() -100
    display.blit(pygame.image.load(os.path.join(DiceRerollHandler.getImagePath())),(xCo, yCo))

def drawTask(display):
    taskLabel = smallFont.render(ScoreBoard.tasks[Game.currentRound].getInfo(), 1, (255, 255, 255))
    display.blit(taskLabel, [800,150])

def drawTaskIcon(display): #TODO default x,y anpassen, breite des icons berücksichtigen(in Task funktion anbieten) 
    paths : list[str] = ScoreBoard.tasks[Game.currentRound].getIconPaths()
    dev : list[int] = ScoreBoard.tasks[Game.currentRound].getIconDeviations()
    for i in range(len(paths)):
        OGpic = pygame.image.load(os.path.join(paths[i]))
        width : int = 2*OGpic.get_width()
        hight : int = 2*OGpic.get_height()
        pic = pygame.transform.scale(OGpic,(width,hight))
        display.blit(pic,(870+2*dev[i], 50))
        #display.blit(pygame.image.load(os.path.join(paths[i])),(870+dev[i], 50))
    

def drawTaskIndicator(display): # Final
        isCompleted : bool = ScoreBoard.tasks[Game.currentRound].isCompleted(Game.playingDice)
        display.blit(pygame.image.load(os.path.join(ImageHelper.getCompletionIndicator(isCompleted))),(810, -150))


def drawDice(display,mouse,dice):
    drawDices(display,dice)
    #if inDice1(mouse[0],mouse[1]):
    #    drawDiceHover1(display)
    #if inDice2(mouse[0],mouse[1]):
    #    drawDiceHover2(display)
    #if inDice3(mouse[0],mouse[1]):
    #    drawDiceHover3(display)
    #if inDice4(mouse[0],mouse[1]):
    #    drawDiceHover4(display)
    #if inDice5(mouse[0],mouse[1]):
    #    drawDiceHover5(display)
    #if inDice6(mouse[0],mouse[1]):
    #    drawDiceHover6(display)

def on_loop(display, dice):
    mouse = pygame.mouse.get_pos()
    drawThrowButton(display,mouse)
    drawNewTurnButton(display,mouse)
    drawDice(display,mouse,dice)
    drawTaskIndicator(display)
    drawTaskIcon(display)
    drawTask(display)
