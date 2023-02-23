import pygame
from pygame.locals import *
import os
import os.path
import mainScreen
import random

class Game:

    numbers = [1,1,1,1,1,1]

    def __init__(self):
        self._running = True
        self.display = None
        self.size = self.weight, self.height = 1280, 720
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), self.size)

 
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
                self.numbers = [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]           
            if mainScreen.inTurnButton(mouse[0],mouse[1]):
                self.numbers = [1,1,1,1,1,1]

    def on_loop(self):
        mainScreen.on_loop(self.display,self.numbers)
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
