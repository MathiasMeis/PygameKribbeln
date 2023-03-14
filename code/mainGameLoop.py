from endScreen import EndScreen
from gamestate import GameState
from kribbeln import Kribbeln
from mainScreen import MainScreen
from startingScreen import StartingScreen
from pygame.locals import *
import pygame

class mainGameLoop:
    size = weight, height = 1920, 1080
    def __init__(self):
        self._running = True
        self.display = None
 
    def on_init():
        pygame.init()
        StartingScreen.init()
        mainGameLoop.display = pygame.display.set_mode(mainGameLoop.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
 
    def on_loop():
        if Kribbeln.currentState == GameState.STARTING:
            StartingScreen.on_loop(mainGameLoop.display)
        elif Kribbeln.currentState == GameState.PLAYING:
            MainScreen.on_loop(mainGameLoop.display)
        elif Kribbeln.currentState == GameState.ENDING:
            EndScreen.on_loop(mainGameLoop.display)
        pygame.display.flip()

    def on_cleanup():
        pygame.quit()
    
    def on_execute():
        if mainGameLoop.on_init() == False:
            Kribbeln.currentState = GameState.FINISHED
        while(Kribbeln.currentState != GameState.FINISHED):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    Kribbeln.currentState = GameState.FINISHED
                if Kribbeln.currentState == GameState.STARTING:
                    StartingScreen.on_event(event)
                elif Kribbeln.currentState == GameState.PLAYING:
                    MainScreen.on_event(event)
                elif Kribbeln.currentState == GameState.ENDING:
                    EndScreen.on_event(event)
                mainGameLoop.on_loop()
            clock = pygame.time.Clock()
            clock.tick(60)
        mainGameLoop.on_cleanup()

mainGameLoop.on_execute()