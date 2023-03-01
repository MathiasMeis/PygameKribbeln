import pygame
from pygame.locals import *
import os
import os.path
import mainScreen
import random
import game
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper

class Game:

    def __init__(self):
        self._running = True
        self.display = None
        self.size = self.weight, self.height = 1920, 980
        #self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), self.size)
        self.background = pygame.transform.scale(pygame.image.load(ImageHelper.getBackground("concept")), self.size)

 
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.display.blit(self.background, (0,0))
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if mainScreen.inThrowButton(mouse[0],mouse[1]):
                game.Game.playingDice.reroll()           
            if mainScreen.inTurnButton(mouse[0],mouse[1]):
                game.Game.currentRound += 1
            if DiceRerollHandler.isInDice(DiceRerollHandler,mouse):
                DiceRerollHandler.switchReroll()
        if event.type ==  pygame.KEYDOWN:
            if (DiceRerollHandler.isArrowKey(event.key)):
                DiceRerollHandler.handleKeyInput(event.key)

            

    def on_loop(self):
        self.display.blit(self.background, (0,0))
        mainScreen.on_loop(self.display)
    def on_render(self):
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()

    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__" :
    mainGame = Game()
    mainGame.on_execute()
