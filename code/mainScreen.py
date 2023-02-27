import pygame
import os
from scoreBoard import ScoreBoard
from color import Color
from game import Game
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper
#Hier wird der ui stuff für das Würfel
throwButtonPos = [300, 800, 200, 100]
throwLabelPos = [340,800]
turnButtonPos = [600, 800, 350, 100]
turnLabelPos = [620,800]
closeButtonPos = [1800, 50, 100, 100]
closeLabelPos = [1825,50]
scoreButtonPos = [1700, 550, 200, 100]
scoreLabelPos = [1700,550]

pygame.font.init()
font  = pygame.font.SysFont("comicsans", 70)
smallFont  = pygame.font.SysFont("comicsans", 30)
throwLabel = font.render("Roll", 1, (255, 255, 255))
turnLabel = font.render("New Turn", 1, (255, 255, 255))
closeLabel = font.render("X", 1, (255, 255, 255))
scoreLabel = font.render("Score", 1, (255, 255, 255))

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
    
def inScoreButton(x,y):
    if scoreButtonPos[0] <= x <= scoreButtonPos[0]+scoreButtonPos[2] and scoreButtonPos[1] <= y <= scoreButtonPos[1]+scoreButtonPos[3]: return True
    else: return False

def inCloseButton(x,y):
    if closeButtonPos[0] <= x <= closeButtonPos[0]+closeButtonPos[2] and closeButtonPos[1] <= y <= closeButtonPos[1]+closeButtonPos[3]: return True
    else: return False


def drawThrowButton(display,mouse):
    if inThrowButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), throwButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), throwButtonPos)
    display.blit(throwLabel, throwLabelPos)
    #Hier später einfach Bild von Button Neuer Wurf rein

def drawNewTurnButton(display,mouse):
    if inTurnButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), turnButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), turnButtonPos)
    display.blit(turnLabel, turnLabelPos)
    #Hier später einfach Bild von Button Neuer Zug rein


def drawScoreButton(display,mouse):
    if inScoreButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), scoreButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), scoreButtonPos)
    display.blit(scoreLabel, scoreLabelPos)
    #Hier später einfach Bild von Button Neuer Zug rein


def drawCloseButton(display,mouse):
    if inCloseButton(mouse[0],mouse[1]):
        pygame.draw.rect(display, (120,30,70), closeButtonPos)
    else: 
        pygame.draw.rect(display, (120,120,120), closeButtonPos)
    display.blit(closeLabel, closeLabelPos)
    #Hier später einfach Bild von Button Neuer Zug rein


def drawDice(display,mouse):
    drawDices(display)
    drawDiceHover(display,mouse)

def drawDices(display):
    for i in range(6):
        xCoordinate = DiceRerollHandler.baseDicePos[0] + i*DiceRerollHandler.diceDistance
        yCoordinate = DiceRerollHandler.baseDicePos[1]
        if(Game.playingDice.toReroll[i] == False):
            yCoordinate += 300
        display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getColorPath())),(xCoordinate, yCoordinate))
        display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getValuePath())),(xCoordinate, yCoordinate))

def drawDiceHover(display, mouse):
    if DiceRerollHandler.isInDice(DiceRerollHandler,mouse):
        display.blit(pygame.image.load(os.path.join(DiceRerollHandler.getImagePath())),DiceRerollHandler.getHoverPosition(DiceRerollHandler))

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


def on_loop(display):
    mouse = pygame.mouse.get_pos()
    drawThrowButton(display,mouse)
    drawNewTurnButton(display,mouse)
    drawDice(display,mouse)
    drawTaskIndicator(display)
    drawTaskIcon(display)
    drawTask(display)
    drawCloseButton(display,mouse)
    drawScoreButton(display,mouse)