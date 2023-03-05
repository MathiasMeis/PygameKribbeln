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

    replayButton = Button(200,870,200,100,"REPLAY")
    newGameButton = Button(800, 870, 200, 100,"NEW GAME")
    quitButton = Button(1400, 870, 200, 100,"QUIT")



    def on_event(event):
        if event.type == pygame.QUIT:
           Kribbeln.currentState = GameState.FINISHED

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if EndScreen.replayButton.mouseIsIn(mouse[0],mouse[1]):
                pass

            if EndScreen.newGameButton.mouseIsIn(mouse[0],mouse[1]) and GameSetup.numberOfPlayers > 1:
                pass

            if EndScreen.quitButton.mouseIsIn(mouse[0], mouse[1]):
                Kribbeln.currentState = GameState.FINISHED



    def on_loop(display):
        display.blit(EndScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        EndScreen.replayButton.drawWithMouse(display,mouse)
        EndScreen.newGameButton.drawWithMouse(display,mouse)
        EndScreen.quitButton.drawWithMouse(display,mouse)
        Kribbeln.scoreBoard.draw(display)
        
