# UI stuff, startbildschirm mit spieleranzahlauswahl, spielerbenennung, später ggfs modusauswahl
import pygame
from gameSetup import GameSetup
from kribbeln import Kribbeln
from gamestate import GameState
import os
from messageBoard import MessageBoard
from imageHelper import ImageHelper
from button import Button

class StartingScreen:
    quitButton : Button = Button(1760,50,300,100," ",imageName="300x100Quit")
    quitMessageBoard : MessageBoard = MessageBoard(["Do you want to quit?"], hasButton=True, buttonText="QUIT", buttonFontColor=(255,255,255), buttenImageName="buttonRed")
    isShowQuitMessageBoard : bool = False
    editingEnabled : bool = False

    newPlayerName : str = ""

    removeBaseX : int = 710
    editBaseX : int = 1160
    playerBaseX : int = 810
    BaseY : int = 100
    editingPlayerIndex : int = -1
    size = weight, height = 1920, 1080
    background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), size)

    pygame.font.init()
    smallFont  = pygame.font.SysFont("comicsans", 30)
    startGameButton = Button(810, 850, 300, 100,"Start Game", imageName="300x100White")

    editButton : Button = Button(playerBaseX+50,BaseY+(100*(Kribbeln.numberOfPlayers-100)),500,500, "xxx")#, imageName="playerEditing")
    denyEditButton : Button = Button(playerBaseX+50,BaseY+(100*(Kribbeln.numberOfPlayers-100)),500,500, "xxx")#, imageName="playerEditing")
    confirmsEditButton : Button = Button(playerBaseX+50,BaseY+(100*(Kribbeln.numberOfPlayers-100)),500,500, "xxx")#, imageName="playerEditing")
    removePlayerButtons : list[Button] = []
    addPlayerButton : Button = Button(playerBaseX+125,BaseY + 12+(100*Kribbeln.numberOfPlayers),50,50," ", imageName="addPlayer")
    editPlayerButtons : list[Button] = []
    playerButtons : list[Button] = []

    def init():
        StartingScreen.addPlayerButton : Button = Button(StartingScreen.playerBaseX+125,StartingScreen.BaseY + 12+(100*Kribbeln.numberOfPlayers),50,50," ", imageName="addPlayer")
        StartingScreen.removePlayerButtons = []
        StartingScreen.playerButtons = []
        StartingScreen.editPlayerButtons = []
        for index in range(len(Kribbeln.players)):
            StartingScreen.playerButtons.append(Button(StartingScreen.playerBaseX,StartingScreen.BaseY+(100*index),300,75, f"{Kribbeln.players[index].getName()}", imageName="player"))
            StartingScreen.editPlayerButtons.append(Button(StartingScreen.editBaseX, StartingScreen.BaseY+12+(100*index), 50, 50," ", imageName="playerEditStart"))
            StartingScreen.removePlayerButtons.append(Button(StartingScreen.removeBaseX,StartingScreen.BaseY+12+(100*index),50,50," ", imageName="removePlayer"))




    def on_event(event): #TODO aufräumen, das geht auch anders
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
           Kribbeln.currentState = GameState.FINISHED

        if(StartingScreen.isShowQuitMessageBoard):
            if StartingScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0],mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                StartingScreen.isShowQuitMessageBoard = False
            if StartingScreen.quitMessageBoard.checkForMouseLocationOnButton(mouse[0],mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()  
        elif(StartingScreen.editingEnabled):
            if StartingScreen.denyEditButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                StartingScreen.newPlayerName = ""
                StartingScreen.editingEnabled = False
            if StartingScreen.confirmsEditButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                Kribbeln.players[StartingScreen.editingPlayerIndex].rename(StartingScreen.newPlayerName)
                StartingScreen.playerButtons[StartingScreen.editingPlayerIndex].label = StartingScreen.newPlayerName
                StartingScreen.newPlayerName = ""
                StartingScreen.editingPlayerIndex = -1
                StartingScreen.editingEnabled = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    StartingScreen.newPlayerName =  StartingScreen.newPlayerName[:-1]
                else:
                    StartingScreen.newPlayerName += event.unicode
        else:
            if StartingScreen.editButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if StartingScreen.quitButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                StartingScreen.isShowQuitMessageBoard = True
            if StartingScreen.startGameButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                Kribbeln.reinit()
                Kribbeln.currentState = GameState.PLAYING
            if Kribbeln.numberOfPlayers < 7 and StartingScreen.addPlayerButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                Kribbeln.addPlayer()
                StartingScreen.init()
            for index in range(len(StartingScreen.playerButtons)):
                StartingScreen.playerButtons[index].mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN
                if len(Kribbeln.players) != 1 and StartingScreen.removePlayerButtons[index].mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                    Kribbeln.removePlayer(index)
                    StartingScreen.init()
                    break
                if StartingScreen.editPlayerButtons[index].mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                    StartingScreen.editButton = Button(StartingScreen.playerBaseX,StartingScreen.BaseY+(100*(index)),300,75, f"{StartingScreen.newPlayerName}", imageName="playerEditing")
                    StartingScreen.denyEditButton = Button(StartingScreen.editBaseX+30, StartingScreen.BaseY+12+(100*index),50,50, " ", imageName="playerEditDeny")
                    StartingScreen.confirmsEditButton = Button(StartingScreen.editBaseX-30, StartingScreen.BaseY+12+(100*index),50,50, " ", imageName="playerEditConfirm")
                    StartingScreen.editingPlayerIndex = index
                    StartingScreen.editingEnabled = True


    def drawElements(display):
        StartingScreen.quitButton.draw(display)
        StartingScreen.startGameButton.draw(display)
        for i in range(len(StartingScreen.playerButtons)):
            StartingScreen.playerButtons[i].draw(display)
            if not StartingScreen.editingEnabled:
                StartingScreen.editPlayerButtons[i].draw(display)
                if len(Kribbeln.players) != 1:
                    StartingScreen.removePlayerButtons[i].draw(display)
        if StartingScreen.isShowQuitMessageBoard:
            StartingScreen.quitMessageBoard.draw(display)
        elif StartingScreen.editingEnabled:
            StartingScreen.editButton.label = f"{StartingScreen.newPlayerName}"
            StartingScreen.editButton.draw(display)
            StartingScreen.denyEditButton.draw(display)
            StartingScreen.confirmsEditButton.draw(display)
        else:
            if Kribbeln.numberOfPlayers < 7:
                StartingScreen.addPlayerButton.draw(display)



    def on_loop(display):
        display.blit(StartingScreen.background, (0,0))
        StartingScreen.drawElements(display)
