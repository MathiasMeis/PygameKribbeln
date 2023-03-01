import pygame
import os
from scoreBoard import ScoreBoard
from game import Game
from gamestate import GameState
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper
from button import Button

from startingScreen import StartingScreen
from messageBoard import MessageBoard

class MainScreen:

    quitMessageBoard : MessageBoard = MessageBoard("Do you want to quit?", "QUIT", "CANCEL", True)
    #Hier wird der ui stuff für das Würfel
    throwButtonPos = [300, 800, 200, 100]
    throwLabelPos = [340,800]
    turnButtonPos = [600, 800, 350, 100]
    turnLabelPos = [620,800]
    closeButtonPos = [1800, 50, 100, 100]
    closeLabelPos = [1825,50]
    scoreButtonPos = [1700, 550, 200, 100]
    scoreLabelPos = [1700,550]
    isShowScoreBoard : bool = False
    isShowQuitMessageBoard : bool = False

    pygame.font.init()
    font  = pygame.font.SysFont("comicsans", 70)
    smallFont  = pygame.font.SysFont("comicsans", 30)
    throwLabel = font.render("Roll", 1, (255, 255, 255))
    turnLabel = font.render("New Turn", 1, (255, 255, 255))
    closeLabel = font.render("X", 1, (255, 255, 255))
    scoreLabel = font.render("Score", 1, (255, 255, 255))
    testButton : Button = Button(100,100,200,50,"TESTmbi")

    size = weight, height = 1920, 980 # 1920, 1080
    background = pygame.transform.scale(pygame.image.load(ImageHelper.getBackground("concept")), size)

    def inThrowButton(x,y):
        if MainScreen.throwButtonPos[0] <= x <= MainScreen.throwButtonPos[0]+MainScreen.throwButtonPos[2] and MainScreen.throwButtonPos[1] <= y <= MainScreen.throwButtonPos[1]+MainScreen.throwButtonPos[3]: return True
        else: return False

    def inTurnButton(x,y):
        if MainScreen.turnButtonPos[0] <= x <= MainScreen.turnButtonPos[0]+MainScreen.turnButtonPos[2] and MainScreen.turnButtonPos[1] <= y <= MainScreen.turnButtonPos[1]+MainScreen.turnButtonPos[3]: return True
        else: return False

    def mightBeDieStateChange(x,y) -> bool:
        if():
            return True
        else:
            return False

    def inScoreButton(x,y):
        if MainScreen.scoreButtonPos[0] <= x <= MainScreen.scoreButtonPos[0]+MainScreen.scoreButtonPos[2] and MainScreen.scoreButtonPos[1] <= y <= MainScreen.scoreButtonPos[1]+MainScreen.scoreButtonPos[3]: return True
        else: return False

    def inCloseButton(x,y):
        if MainScreen.closeButtonPos[0] <= x <= MainScreen.closeButtonPos[0]+MainScreen.closeButtonPos[2] and MainScreen.closeButtonPos[1] <= y <= MainScreen.closeButtonPos[1]+MainScreen.closeButtonPos[3]: return True
        else: return False


    def drawThrowButton(display,mouse):
        if MainScreen.inThrowButton(mouse[0],mouse[1]):
            pygame.draw.rect(display, (120,30,70), MainScreen.throwButtonPos)
        else: 
            pygame.draw.rect(display, (120,120,120), MainScreen.throwButtonPos)
        display.blit(MainScreen.throwLabel, MainScreen.throwLabelPos)
        #Hier später einfach Bild von Button Neuer Wurf rein

    def drawNewTurnButton(display,mouse):
        if MainScreen.inTurnButton(mouse[0],mouse[1]):
            pygame.draw.rect(display, (120,30,70), MainScreen.turnButtonPos)
        else: 
            pygame.draw.rect(display, (120,120,120), MainScreen.turnButtonPos)
        display.blit(MainScreen.turnLabel, MainScreen.turnLabelPos)
        #Hier später einfach Bild von Button Neuer Zug rein


    def drawScoreButton(display,mouse):
        if MainScreen.inScoreButton(mouse[0],mouse[1]):
            pygame.draw.rect(display, (120,30,70), MainScreen.scoreButtonPos)
        else: 
            pygame.draw.rect(display, (120,120,120), MainScreen.scoreButtonPos)
        display.blit(MainScreen.scoreLabel, MainScreen.scoreLabelPos)
        #Hier später einfach Bild von Button Neuer Zug rein


    def drawCloseButton(display,mouse):
        if MainScreen.inCloseButton(mouse[0],mouse[1]):
            pygame.draw.rect(display, (120,30,70), MainScreen.closeButtonPos)
        else: 
            pygame.draw.rect(display, (120,120,120), MainScreen.closeButtonPos)
        display.blit(MainScreen.closeLabel, MainScreen.closeLabelPos)
        #Hier später einfach Bild von Button Neuer Zug rein


    def drawDice(display,mouse):
        MainScreen.testButton.draw(display)
        MainScreen.drawDices(display)
        MainScreen.drawDiceHover(display,mouse)

    def drawDices(display):
        for i in range(6):
            xCoordinate = DiceRerollHandler.baseDicePos[0] + i*DiceRerollHandler.diceDistance
            yCoordinate = DiceRerollHandler.baseDicePos[1]
            if(Game.playingDice.toReroll[i] == False):
                yCoordinate += 300
            display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getColorPath())),(xCoordinate, yCoordinate))
            display.blit(pygame.image.load(os.path.join(Game.playingDice.allDice[i].getValuePath())),(xCoordinate, yCoordinate))

    def drawDiceHover(display, mouse):
        DiceRerollHandler.setIndexWithMouse(mouse)
        display.blit(pygame.image.load(os.path.join(DiceRerollHandler.getImagePath())),DiceRerollHandler.getHoverPosition())

    def drawTask(display):
        taskLabel = MainScreen.smallFont.render(ScoreBoard.tasks[Game.currentRound].getInfo(), 1, (255, 255, 255))
        display.blit(taskLabel, [800,150])
    
    def drawTaskIcon(display): #TODO default x,y anpassen, breite des icons berücksichtigen(in Task funktion anbieten) 
        paths : list[str] = ScoreBoard.tasks[Game.currentRound].getIconPaths()
        dev : list[int] = ScoreBoard.tasks[Game.currentRound].getIconDeviations()
        iconWidth : int = ScoreBoard.tasks[Game.currentRound].getIconWidth()
        for i in range(len(paths)):
            OGpic = pygame.image.load(os.path.join(paths[i]))
            width : int = 2*OGpic.get_width()
            hight : int = 2*OGpic.get_height()
            pic = pygame.transform.scale(OGpic,(width,hight))
            display.blit(pic,((960-iconWidth)+2*dev[i], 20))
            #display.blit(pygame.image.load(os.path.join(paths[i])),(870+dev[i], 50))
        
    def drawCurrentPlayerLabel(display):
        cFont  = pygame.font.SysFont("comicsans", 30)
        playerLabel = cFont.render(StartingScreen.players[0].getName(), 1, (255, 255, 255))
        display.blit(playerLabel, [10,10])
        #display.blit(pygame.image.load(os.path.join(ImageHelper.getTaskTable())),(560, -50))

    def drawMessageBoard(display):
        message : str = MainScreen.smallFont.render(MainScreen.quitMessageBoard.message, 1, (0, 0, 0))
        baseX : int = 660
        baseY : int = 390
        buttonLabels : list[str] = MainScreen.quitMessageBoard.getButtonLabels()
        buttonDeviation : list[int] = MainScreen.quitMessageBoard.getIconDeviation()
        buttonIconPath : list[str] = MainScreen.quitMessageBoard.getIconPaths()

        display.blit(pygame.image.load(os.path.join(ImageHelper.getMessageBoardIcon())),(baseX, baseY))
        display.blit(message, [baseX+20,baseY+50])
        for i in range(MainScreen.quitMessageBoard.getNumberOfButtons()):
            display.blit(pygame.image.load(os.path.join(buttonIconPath[i])),(baseX+200+buttonDeviation[i], baseY+275))
            if(i == 0 and MainScreen.quitMessageBoard.firstButtonIsRed):
                buttonLabel = MainScreen.smallFont.render(buttonLabels[i], 1, (255, 255, 255))
            else:
                buttonLabel = MainScreen.smallFont.render(buttonLabels[i], 1, (0, 0, 0))

            centering : int = 100 - (buttonLabel.get_width() /2)
            display.blit(buttonLabel, [baseX+200+buttonDeviation[i]+centering,baseY+275])
    


    def drawTaskTable(display): # Final
            isCompleted : bool = ScoreBoard.tasks[Game.currentRound].isCompleted(Game.playingDice)
            display.blit(pygame.image.load(os.path.join(ImageHelper.getCompletionIndicator(isCompleted))),(560, -50))
            display.blit(pygame.image.load(os.path.join(ImageHelper.getTaskTable())),(560, -50))

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

    def on_event(event):
        if(MainScreen.isShowQuitMessageBoard):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if MainScreen.isQuitInQuitMessageBoard(mouse[0],mouse[1]):
                    pygame.quit()          
                if MainScreen.isCancelInQuitMessageBoard(mouse[0],mouse[1]):
                    MainScreen.isShowQuitMessageBoard = False
        elif(MainScreen.isShowScoreBoard):
            pass
        elif(False):
            pass #playerswitchmessageboard
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if MainScreen.inThrowButton(mouse[0],mouse[1]):
                    Game.playingDice.reroll()   
                if MainScreen.testButton.mouseIsIn(mouse[0],mouse[1]):
                    print("HI")

                if MainScreen.inTurnButton(mouse[0],mouse[1]):
                    Game.currentRound += 1
                if MainScreen.inCloseButton(mouse[0],mouse[1]):
                    MainScreen.isShowQuitMessageBoard = True
                if DiceRerollHandler.setIndexWithMouse(mouse):
                    DiceRerollHandler.switchReroll()
            if event.type ==  pygame.KEYDOWN:
                if (DiceRerollHandler.isArrowKey(event.key)):
                    DiceRerollHandler.handleKeyInput(event.key)


    def on_loop(display):
        display.blit(MainScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        MainScreen.drawThrowButton(display,mouse)
        MainScreen.drawNewTurnButton(display,mouse)
        MainScreen.drawDice(display,mouse)
        MainScreen.drawTaskTable(display)
        MainScreen.drawTaskIcon(display)
        MainScreen.drawTask(display)
        MainScreen.drawCloseButton(display,mouse)
        MainScreen.drawScoreButton(display,mouse)
        MainScreen.testButton.mouseIsIn(mouse[0], mouse[1])
        if(MainScreen.isShowScoreBoard):
            print("Score")
        elif(MainScreen.isShowQuitMessageBoard):
            MainScreen.drawMessageBoard(display)
