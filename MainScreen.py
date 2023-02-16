import pygame
#Hier wird der ui stuff für das Würfel
throwX = 300
throwY = 500
throwWeight = 200
throwHeight = 100
throwButton = [throwX, throwY, throwWeight, throwHeight]

def inThrowButton(x,y):
    if throwX <= x <= throwX+throwWeight and throwY <= y <= throwY+throwHeight: return True
    else: return False

pygame.font.init()
font  = pygame.font.SysFont("comicsans", 70)
label = font.render("Roll", 1, (255, 255, 255))