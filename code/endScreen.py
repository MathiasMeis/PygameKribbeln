import pygame
from gameSetup import GameSetup
from kribbeln import Kribbeln
from gamestate import GameState
import os
from messageBoard import MessageBoard
from imageHelper import ImageHelper
from button import Button

class EndScreen:
    size = weight, height = 1920, 1080
    background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), size)

    pygame.font.init()
    smallFont  = pygame.font.SysFont("comicsans", 30)

    quitButton = Button(810, 900, 300, 100,"QUIT", imageName="300x100White")



    def on_event(event):
        if event.type == pygame.QUIT:
           Kribbeln.currentState = GameState.FINISHED

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if EndScreen.quitButton.checkForMouseInput(mouse[0], mouse[1]):
                Kribbeln.currentState = GameState.FINISHED



    def on_loop(display):
        display.blit(EndScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        EndScreen.quitButton.drawWithMouse(display,mouse)
        Kribbeln.scoreBoard.draw(display)
        
