import pygame
import os
#Hier wird der ui stuff für das Würfel
throwButtonPos = [300, 500, 200, 100]
throwLabelPos = [340,500]
turnButtonPos = [600, 500, 350, 100]
turnLabelPos = [620,500]

pygame.font.init()
font  = pygame.font.SysFont("comicsans", 70)
throwLabel = font.render("Roll", 1, (255, 255, 255))
turnLabel = font.render("New Turn", 1, (255, 255, 255))

def inThrowButton(x,y):
    if throwButtonPos[0] <= x <= throwButtonPos[0]+throwButtonPos[2] and throwButtonPos[1] <= y <= throwButtonPos[1]+throwButtonPos[3]: return True
    else: return False

def inTurnButton(x,y):
    if turnButtonPos[0] <= x <= turnButtonPos[0]+turnButtonPos[2] and turnButtonPos[1] <= y <= turnButtonPos[1]+turnButtonPos[3]: return True
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

def drawDices(display,number):
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[0]}.png")),(150,100))
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[1]}.png")),(300,100))
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[2]}.png")),(450,100))
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[3]}.png")),(600,100))
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[4]}.png")),(750,100))
    display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number[5]}.png")),(900,100))

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