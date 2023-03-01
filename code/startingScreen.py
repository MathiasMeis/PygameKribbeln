# UI stuff, startbildschirm mit spieleranzahlauswahl, spielerbenennung, später ggfs modusauswahl
import pygame
from gameSetup import GameSetup
from game import Game
from gamestate import GameState
import os
from messageBoard import MessageBoard
from imageHelper import ImageHelper

class StartingScreen:
    startGameButtonPos = [600, 850, 400, 100]
    playerLabelPos = [200, 200, 270, 100]
    addPlayerButtonPos = [200,350,50,100]
    removePlayerButtonPos = [300,350,50,100]
    editPlayerButtonPos = [500, 200, 150, 100]
    textBoxActive : bool = False
    playerText = ''
    editPlayerLabel = -1
    yDeviation = 150
    quitMessageBoard : MessageBoard = MessageBoard("Do you want to quit?", "QUIT", "CANCEL", True)
    isShowQuitMessageBoard : bool = False
    pygame.font.init()
    smallFont  = pygame.font.SysFont("comicsans", 30)
    
    font  = pygame.font.SysFont("comicsans", 70)

    size = weight, height = 1920, 980 # 1920, 1080
    background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), size)

    def inStartGameButton(mouseX,mouseY) -> bool:
        [x,y,xL,yL] = StartingScreen.startGameButtonPos
        if x <= mouseX <= x+xL and y <= mouseY <= y+yL: return True
        else: return False
    
    def inAddPlayerButton(mouseX,mouseY) -> bool:
        [x,y,xL,yL] = StartingScreen.addPlayerButtonPos
        if x <= mouseX <= x+xL and y <= mouseY <= y+yL: return True
        else: return False
    
    def inRemovePlayerButton(mouseX,mouseY) -> bool:
        [x,y,xL,yL] = StartingScreen.removePlayerButtonPos
        if x <= mouseX <= x+xL and y <= mouseY <= y+yL and GameSetup.numberOfPlayers > 1: return True
        else: return False

    def inWhichEditBox(mouseX,mouseY) -> int:
        for i in range(GameSetup.numberOfPlayers):   
            [x,y,xL,yL] = StartingScreen.editPlayerButtonPos
            y += i*StartingScreen.yDeviation
            if x <= mouseX <= x+xL and y <= mouseY <= y+yL: 
                return i
        else: 
            return -1

    def drawGameStartButton(display,mouse):
        if StartingScreen.inStartGameButton(mouse[0],mouse[1]):
            pygame.draw.rect(display, (120,30,70), StartingScreen.startGameButtonPos)
        else: 
            pygame.draw.rect(display, (120,120,120), StartingScreen.startGameButtonPos)
        label = StartingScreen.font.render("Start Game",1, (255, 255, 255))
        display.blit(label, StartingScreen.startGameButtonPos)
        #Hier später einfach Bild von Button Start Game rein

    def drawAddRemovePlayerButton(display):
        pygame.draw.rect(display, (120,70,70), StartingScreen.addPlayerButtonPos)
        label = StartingScreen.font.render("+",1, (255, 255, 255))
        display.blit(label, StartingScreen.addPlayerButtonPos)
        if GameSetup.numberOfPlayers > 1:                
            pygame.draw.rect(display, (120,70,70), StartingScreen.removePlayerButtonPos)
            label = StartingScreen.font.render("-",1, (255, 255, 255))
            display.blit(label, StartingScreen.removePlayerButtonPos)

    def drawEditButtons(display):
        for i in range(GameSetup.numberOfPlayers):
            x,y,xL,yL = StartingScreen.editPlayerButtonPos[0],StartingScreen.editPlayerButtonPos[1],StartingScreen.editPlayerButtonPos[2],StartingScreen.editPlayerButtonPos[3]
            y += i*StartingScreen.yDeviation
            pygame.draw.rect(display, (120,70,70), [x,y,xL,yL])
            if StartingScreen.editPlayerLabel != i:
                label = StartingScreen.font.render("Edit",1, (255, 255, 255))
            else:
                label = StartingScreen.font.render("Save",1, (255, 255, 255))
            display.blit(label, [x,y,xL,yL]) 

    def drawPlayerLabels(display):
        for i in range(GameSetup.numberOfPlayers):
            x,y,xL,yL = StartingScreen.playerLabelPos
            y += i*StartingScreen.yDeviation
            if StartingScreen.editPlayerLabel != i:
                pygame.draw.rect(display, (120,70,70), [x,y,xL,yL])
                playerLabel = StartingScreen.font.render(GameSetup.players[i].getName(), 1, (255, 255, 255))
            else: 
                pygame.draw.rect(display, (180,100,70), [x,y,xL,yL])
                playerLabel = StartingScreen.font.render(StartingScreen.playerText,1, (255, 255, 255))
            display.blit(playerLabel,[x,y,xL,yL]) 

    def drawMessageBoard(display):
        message : str = StartingScreen.smallFont.render(StartingScreen.quitMessageBoard.message, 1, (0, 0, 0))
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
                        StartingScreen.textBoxActive = True
                        GameSetup.currentIndex = editBox
                        StartingScreen.playerText = GameSetup.players[editBox].getName()
                    else: 
                        GameSetup.renamePlayer(StartingScreen.playerText)
                        StartingScreen.editPlayerLabel = -1
                        StartingScreen.textBoxActive = False
                if StartingScreen.inAddPlayerButton(mouse[0],mouse[1]):
                    StartingScreen.addPlayerButtonPos[1] += StartingScreen.yDeviation
                    StartingScreen.removePlayerButtonPos[1] += StartingScreen.yDeviation
                    GameSetup.addPlayer()
                if StartingScreen.inRemovePlayerButton(mouse[0],mouse[1]):
                    StartingScreen.addPlayerButtonPos[1] -= StartingScreen.yDeviation
                    StartingScreen.removePlayerButtonPos[1] -= StartingScreen.yDeviation
                    GameSetup.removePlayer()
                    if GameSetup.numberOfPlayers == StartingScreen.editPlayerLabel:
                        StartingScreen.editPlayerLabel = -1
                        StartingScreen.textBoxActive = False
                if StartingScreen.inStartGameButton(mouse[0], mouse[1]):
                    if StartingScreen.editPlayerLabel != -1:
                        GameSetup.renamePlayer(StartingScreen.playerText)
                    Game.currentState = GameState.PLAYING
            if event.type == pygame.KEYDOWN and StartingScreen.textBoxActive:
                if event.key == pygame.K_BACKSPACE:
                    StartingScreen.playerText =  StartingScreen.playerText[:-1]
                else:
                    StartingScreen.playerText += event.unicode

    def on_loop(display):
        display.blit(StartingScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        StartingScreen.drawGameStartButton(display,mouse)
        StartingScreen.drawPlayerLabels(display)
        StartingScreen.drawEditButtons(display)
        StartingScreen.drawAddRemovePlayerButton(display)
        
