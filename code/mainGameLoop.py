import pygame
from pygame.locals import *
import os
import os.path
import MainScreen
import random
import Die
import Color

class Game:

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
            if MainScreen.inThrowButton(mouse[0],mouse[1]):
                number = random.randint(1,4)
                self.display.blit(pygame.image.load(os.path.join("assets", f"Die_green_{number}.png")),(50,50))

    def on_loop(self):
        mouse = pygame.mouse.get_pos()
        if MainScreen.inThrowButton(mouse[0],mouse[1]):
            pygame.draw.rect(self.display, (120,30,70), MainScreen.throwButton)
        else: 
            pygame.draw.rect(self.display, (120,120,120), MainScreen.throwButton)
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
