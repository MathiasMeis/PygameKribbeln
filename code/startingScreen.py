# UI stuff, startbildschirm mit spieleranzahlauswahl, spielerbenennung, später ggfs modusauswahl
import pygame
from gameSetup import GameSetup
from game import Game
from gamestate import GameState
import os
from messageBoard import MessageBoard
from imageHelper import ImageHelper
from button import Button

class StartingScreen:
    playerText = ''
    editPlayerLabel = -1
    yDeviation = 150
    quitMessageBoard : MessageBoard = MessageBoard("Do you want to quit?", "QUIT", "CANCEL", True)
    isShowQuitMessageBoard : bool = False

    size = weight, height = 1920, 1080 # 1920, 1080
    background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), size)

    pygame.font.init()
    smallFont  = pygame.font.SysFont("comicsans", 30)

    startGameButton = Button(600, 850, 400, 100,"Start Game")
    addPlayerButton = Button(200,200+GameSetup.numberOfPlayers*150,200,100,'Add Player')
    removePlayerButton = Button(300,500,250,100,"Remove Player")
    editPlayerButton = Button(200, 200, 270, 100,"Player 1",color=(130,70,20))

    def inWhichEditBox(mouseX,mouseY) -> int:
        for i in range(GameSetup.numberOfPlayers):   
            [x,y,xL,yL] = [200, 200+i*StartingScreen.yDeviation, 270, 100]
            if x <= mouseX <= x+xL and y <= mouseY <= y+yL: 
                return i
        else: 
            return -1

    def drawMessageBoard(display):
        message : str = StartingScreen.smallFont.render(StartingScreen.quitMessageBoard.messages, 1, (0, 0, 0))
        baseX : int = 660
        baseY : int = 390
        buttonLabels : list[str] = StartingScreen.quitMessageBoard.getButtonLabels()
        buttonDeviation : list[int] = StartingScreen.quitMessageBoard.getIconDeviation()
        buttonIconPath : list[str] = StartingScreen.quitMessageBoard.getIconPaths()

        display.blit(pygame.image.load(os.path.join(ImageHelper.getMessageBoardIcon())),(baseX, baseY))
        display.blit(message, [baseX+20,baseY+50])
        for i in range(StartingScreen.quitMessageBoard.getNumberOfButtons()):
            display.blit(pygame.image.load(os.path.join(buttonIconPath[i])),(baseX+200+buttonDeviation[i], baseY+275))
            if(i == 0 and StartingScreen.quitMessageBoard.firstButtonIsRed):
                buttonLabel = StartingScreen.smallFont.render(buttonLabels[i], 1, (255, 255, 255))
            else:
                buttonLabel = StartingScreen.smallFont.render(buttonLabels[i], 1, (0, 0, 0))

            centering : int = 100 - (buttonLabel.get_width() /2)
            display.blit(buttonLabel, [baseX+200+buttonDeviation[i]+centering,baseY+275])


    def isQuitInQuitMessageBoard(mouseX,mouseY):
        if (710 <= mouseX <= 910):
            if(665 <= mouseY <= 715):
                return True
        else: return False

    def isCancelInQuitMessageBoard(mouseX,mouseY):
        if (1010 <= mouseX <= 1210):
            if(665 <= mouseY <= 715):
                return True
        else: return False


    def on_event(event): #TODO aufräumen, das geht auch anders
        if event.type == pygame.QUIT:
           Game.currentState = GameState.FINISHED

        if(StartingScreen.isShowQuitMessageBoard):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if StartingScreen.isQuitInQuitMessageBoard(mouse[0],mouse[1]):
                    pygame.quit()          
                if StartingScreen.isCancelInQuitMessageBoard(mouse[0],mouse[1]):
                    StartingScreen.isShowQuitMessageBoard = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                editBox = StartingScreen.inWhichEditBox(mouse[0],mouse[1])
                if editBox > -1:
                    if StartingScreen.editPlayerLabel != editBox:
                        if StartingScreen.editPlayerLabel != -1:
                            GameSetup.renamePlayer(StartingScreen.playerText)
                        StartingScreen.editPlayerLabel = editBox
                        GameSetup.currentIndex = editBox
                        StartingScreen.playerText = GameSetup.players[editBox].getName()
                    else: 
                        GameSetup.renamePlayer(StartingScreen.playerText)
                        StartingScreen.editPlayerLabel = -1
                if StartingScreen.addPlayerButton.mouseIsIn(mouse[0],mouse[1]):
                    GameSetup.addPlayer()
                if StartingScreen.removePlayerButton.mouseIsIn(mouse[0],mouse[1]) and GameSetup.numberOfPlayers > 1:
                    GameSetup.removePlayer()
                    if GameSetup.numberOfPlayers == StartingScreen.editPlayerLabel:
                        StartingScreen.editPlayerLabel = -1
                if StartingScreen.startGameButton.mouseIsIn(mouse[0], mouse[1]):
                    if StartingScreen.editPlayerLabel != -1:
                        GameSetup.renamePlayer(StartingScreen.playerText)
                    Game.currentState = GameState.PLAYING
            if event.type == pygame.KEYDOWN and StartingScreen.editPlayerLabel != -1:
                if event.key == pygame.K_BACKSPACE:
                    StartingScreen.playerText =  StartingScreen.playerText[:-1]
                else:
                    StartingScreen.playerText += event.unicode

    def on_loop(display):
        display.blit(StartingScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        StartingScreen.startGameButton.drawWithMouse(display,mouse)
        for i in range(GameSetup.numberOfPlayers):
            if StartingScreen.editPlayerLabel == i:
                StartingScreen.editPlayerButton = Button(200, 200+i*StartingScreen.yDeviation, 270, 100,StartingScreen.playerText,color=(130,70,20))
                StartingScreen.editPlayerButton.draw(display)
            else: 
                PlayerButton = Button(200, 200+i*StartingScreen.yDeviation, 270, 100,GameSetup.players[i].getName())
                PlayerButton.draw(display)
        StartingScreen.addPlayerButton = Button(200,200+GameSetup.numberOfPlayers*150,200,100,'Add Player')
        StartingScreen.addPlayerButton.drawWithMouse(display,mouse)
        if GameSetup.numberOfPlayers > 1:
            StartingScreen.removePlayerButton = Button(500,200+GameSetup.numberOfPlayers*150,250,100,"Remove Player")
            StartingScreen.removePlayerButton.drawWithMouse(display,mouse)
        
