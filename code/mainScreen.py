import pygame
import os
from kribbeln import Kribbeln
from gamestate import GameState
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper
from button import Button
from messageBoard import MessageBoard

class MainScreen:
    taskInfoMessageBoard : MessageBoard
    quitMessageBoard : MessageBoard = MessageBoard(["Do you want to quit?"], hasButton=True, buttonText="QUIT", buttonFontColor=(255,255,255), buttenImageName="buttonRed")
    nextTurnMessageBoard : MessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")

    isShowQuitMessageBoard : bool = False
    isShowNextTurnMessageBoard : bool = False
    isShowTaskInfo : bool = False
    isShowScoreBoard : bool = False

    pygame.font.init()
    font  = pygame.font.SysFont("comicsans", 70)
    smallFont  = pygame.font.SysFont("comicsans", 30)

    endScreenButton : Button = Button(100,150,300,100,"END GAME",imageName="300x100White") # for testing
    taskInfoButton : Button = Button(1300,0,50,50," ", imageName="taskInfo")
    rerollButton : Button = Button(100,400,300,100,"REROLL",imageName="300x100White")
    finishButton : Button = Button(100,800,300,100,"FINISH",imageName="300x100White")
    quitButton : Button = Button(1760,50,300,100," ",imageName="300x100Quit")
    scoreBoardButton : Button = Button(1760,200,300,100,"SCORE              ",imageName="300x100White")

    size = weight, height = 1920, 1080
    background = pygame.transform.scale(pygame.image.load(ImageHelper.getBackground("table")), size)

    def mightBeDieStateChange(x,y) -> bool:
        if():
            return True
        else:
            return False
        

    def drawPointsLabel(display):
        display.blit(pygame.image.load(os.path.join(ImageHelper.getButton("300x200White"))),(100, 550))
        pointsHeaderLabel = MainScreen.smallFont.render("POINTS:", 1, (0, 0, 0))
        headerCentering : int = (150) - (pointsHeaderLabel.get_width() /2)
        display.blit(pointsHeaderLabel, [100+headerCentering,560])
        pointFont  = pygame.font.SysFont("comicsans", 70)
        if(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice)):
            pointsLabel = pointFont.render(f"{Kribbeln.playingDice.getValues()}", 1, (0, 216, 36))
        else:
            pointsLabel = pointFont.render(f"{Kribbeln.playingDice.getValues()}", 1, (255, 0, 25))
        centering : int = (150) - (pointsLabel.get_width() /2)
        display.blit(pointsLabel, [100+centering,600])

        font  = pygame.font.SysFont("comicsans", 15)
        remainingRerollsLabel = font.render(f"Remaining rerolls: {Kribbeln.getRemainigRerolls()}", 1, (0, 0, 0))
        xCentering : int = remainingRerollsLabel.get_width() / 2
        display.blit(remainingRerollsLabel, [250-xCentering,720])

    def drawDice(display,mouse):
        MainScreen.drawDices(display)
        MainScreen.drawDiceHover(display,mouse)

    def drawDices(display):
        for i in range(6):
            xCoordinate = DiceRerollHandler.baseDicePos[0] + i*DiceRerollHandler.diceDistance
            yCoordinate = DiceRerollHandler.baseDicePos[1]
            if(Kribbeln.playingDice.toReroll[i] == False):
                yCoordinate += 300
            display.blit(pygame.image.load(os.path.join(Kribbeln.playingDice.allDice[i].getColorPath())),(xCoordinate, yCoordinate))
            display.blit(pygame.image.load(os.path.join(Kribbeln.playingDice.allDice[i].getValuePath())),(xCoordinate, yCoordinate))

    def drawDiceHover(display, mouse):
        DiceRerollHandler.setIndexWithMouse(mouse)
        display.blit(pygame.image.load(os.path.join(DiceRerollHandler.getImagePath())),DiceRerollHandler.getHoverPosition())

    def drawTaskIcon(display):
        paths : list[str] = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconPaths()
        dev : list[int] = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconDeviations()
        iconWidth : int = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconWidth()
        for i in range(len(paths)):
            OGpic = pygame.image.load(os.path.join(paths[i]))
            width : int = 2*OGpic.get_width()
            hight : int = 2*OGpic.get_height()
            pic = pygame.transform.scale(OGpic,(width,hight))
            display.blit(pic,((960-iconWidth)+2*dev[i], 20))
        
    def drawCurrentPlayerLabel(display):
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("labels", "playerLabel"))),(0, 0))
        cFont  = pygame.font.SysFont("comicsans", 40)
        playerLabel = cFont.render(Kribbeln.players[Kribbeln.currentPlayerIndex].getName(), 1, (0, 0, 0))
        xCentering : int = 150 - (playerLabel.get_width() /2)
        yCentering : int = 75 - (playerLabel.get_height() /2)
        display.blit(playerLabel, [xCentering,yCentering])


    def drawTaskTable(display): # Final
            isCompleted : bool = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice)
            display.blit(pygame.image.load(os.path.join(ImageHelper.getCompletionIndicator(isCompleted))),(560, -50))
            display.blit(pygame.image.load(os.path.join(ImageHelper.getTaskTable())),(560, -50))



    def on_event(event):
        mouse = pygame.mouse.get_pos()
        if(MainScreen.isShowQuitMessageBoard):
            if MainScreen.quitMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()          
            if MainScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowQuitMessageBoard = False
        elif(MainScreen.isShowNextTurnMessageBoard):
            if MainScreen.nextTurnMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowNextTurnMessageBoard = False
                Kribbeln.nextPlayer()
        elif(MainScreen.isShowTaskInfo):
            if MainScreen.taskInfoMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowTaskInfo = False
        elif(MainScreen.isShowScoreBoard):
            if Kribbeln.scoreBoard.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowScoreBoard = False
        else:
            if MainScreen.endScreenButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN: # for testing
                Kribbeln.currentState = GameState.ENDING # for testing
            if MainScreen.taskInfoButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowTaskInfo = False
            if MainScreen.quitButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowQuitMessageBoard = True
            if MainScreen.scoreBoardButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowScoreBoard = True
            if MainScreen.finishButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.nextTurnMessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
                MainScreen.isShowNextTurnMessageBoard = True
            if MainScreen.rerollButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                if Kribbeln.hasRemainingRerolls():
                    Kribbeln.playingDice.reroll()
                    Kribbeln.lowerRerollCounter()
            if MainScreen.taskInfoButton.mouseIsIn(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.taskInfoMessageBoard = MessageBoard(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getInfo())
                MainScreen.isShowTaskInfo = True

            if DiceRerollHandler.setIndexWithMouse(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                DiceRerollHandler.switchReroll()
            if event.type ==  pygame.KEYDOWN:
                if (DiceRerollHandler.isArrowKey(event.key)):
                    DiceRerollHandler.handleKeyInput(event.key)

    def drawElements(display):
        MainScreen.drawCurrentPlayerLabel(display)
        MainScreen.drawTaskTable(display)
        MainScreen.drawTaskIcon(display)
        MainScreen.drawPointsLabel(display)
        MainScreen.endScreenButton.draw(display) # for testing
        MainScreen.taskInfoButton.draw(display)
        MainScreen.quitButton.draw(display)
        MainScreen.finishButton.draw(display)
        MainScreen.scoreBoardButton.draw(display)
        MainScreen.rerollButton.draw(display)
        if(MainScreen.isShowQuitMessageBoard):
            MainScreen.quitMessageBoard.draw(display)
        elif(MainScreen.isShowNextTurnMessageBoard):
            MainScreen.nextTurnMessageBoard.draw(display)
        elif(MainScreen.isShowTaskInfo):
            MainScreen.taskInfoMessageBoard.draw(display)
        elif(MainScreen.isShowScoreBoard):
            Kribbeln.scoreBoard.drawAsOverlay(display)

    def on_loop(display):
        display.blit(MainScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        MainScreen.drawDice(display, mouse) # split
        MainScreen.drawElements(display)