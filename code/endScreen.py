from button import Button
from gamestate import GameState
from kribbeln import Kribbeln
from imageHelper import ImageHelper
import pygame
import os

class EndScreen:
    size = weight, height = 1920, 1080
    background = pygame.transform.scale(pygame.image.load(ImageHelper.getBackground("endScreen")), size)
    quitButton = Button(810, 900, 300, 100,"QUIT", imageName="300x100White")

    def on_event(event) -> None:
        if event.type == pygame.QUIT:
           Kribbeln.currentState = GameState.FINISHED
        mouse = pygame.mouse.get_pos()
        if EndScreen.quitButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
            Kribbeln.currentState = GameState.FINISHED

    def getHighestScore() -> int:
        points : int = 0
        for index in range(len(Kribbeln.players)):
            if (Kribbeln.scoreBoard.scores[index][2] > points):
                points = Kribbeln.scoreBoard.scores[index][2]
        return points

    def drawWinnerIndicator(display) -> None:
        highestPoints : int = EndScreen.getHighestScore()
        numberOfPlayers : int = len(Kribbeln.players)
        width : int = 150 * (numberOfPlayers + 1)
        baseX : int = 960 - (width/2) + 150
        for index in range(numberOfPlayers):
            if (Kribbeln.scoreBoard.scores[index][2] == highestPoints):
                display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "winner"))),(baseX+(150*index), 50))

    def on_loop(display) -> None:
        display.blit(EndScreen.background, (0,0))
        EndScreen.quitButton.draw(display)
        Kribbeln.scoreBoard.draw(display)
        EndScreen.drawWinnerIndicator(display)