from button import Button
from diceRerollHandler import DiceRerollHandler
from gamestate import GameState
from imageHelper import ImageHelper
from kribbeln import Kribbeln
from messageBoard import MessageBoard
from taskHelper import TaskHelper
import os
import pygame

class MainScreen:
    taskInfoMessageBoard : MessageBoard
    quitMessageBoard : MessageBoard = MessageBoard(["Do you want to quit?"], hasButton=True, buttonText="QUIT", buttonFontColor=(255,255,255), buttenImageName="buttonRed")
    nextTurnMessageBoard : MessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")

    isShowQuitMessageBoard : bool = False
    isShowNextTurnMessageBoard : bool = False
    isShowTaskInfo : bool = False
    isShowScoreBoard : bool = False

    taskInfoButton : Button = Button(1300,0,50,50," ", imageName="taskInfo")
    rerollButton : Button = Button(100,400,300,100,"REROLL",imageName="300x100White")
    disableRerollButton : Button = Button(100,400,300,100,"REROLL",imageName="buttonDisabled")
    finishButton : Button = Button(100,800,300,100,"FINISH",imageName="300x100White")
    quitButton : Button = Button(1760,50,300,100," ",imageName="300x100Quit")
    scoreBoardButton : Button = Button(1760,200,300,100,"SCORE              ",imageName="300x100White")
    enableAllButton : Button = Button(1700,400,200,100,"KEEP NONE",imageName="200x100White", fontSize=25)
    disableAllButton : Button = Button(1700,800,200,100,"KEEP ALL",imageName="200x100White", fontSize=25)

    pygame.font.init()
    font  = pygame.font.SysFont("comicsans", 30)
    size = weight, height = 1920, 1080
    background = pygame.transform.scale(pygame.image.load(ImageHelper.getBackground("table")), size)

    def drawPointsLabel(display) -> None:
        smallFont  = pygame.font.SysFont("comicsans", 15)
        pointFont  = pygame.font.SysFont("comicsans", 70)
        display.blit(pygame.image.load(os.path.join(ImageHelper.getButton("300x200White"))),(100, 550))
        pointsHeaderLabel = MainScreen.font.render("POINTS:", 1, (0, 0, 0))
        headerCentering : int = (150) - (pointsHeaderLabel.get_width() /2)
        display.blit(pointsHeaderLabel, [100+headerCentering,560])
        if(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice,  Kribbeln.players[Kribbeln.currentPlayerIndex])):
            pointsLabel = pointFont.render(f"{Kribbeln.playingDice.getValues()}", 1, (0, 216, 36))
        else:
            pointsLabel = pointFont.render(f"{Kribbeln.playingDice.getValues()}", 1, (255, 0, 25))
        centering : int = (150) - (pointsLabel.get_width() /2)
        display.blit(pointsLabel, [100+centering,600])
        if (TaskHelper.isKribbelnTask(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound])):
            minimumPointsLabel = smallFont.render(f"You need at least {Kribbeln.players[Kribbeln.currentPlayerIndex].getHighestKribblePoints() + 1} points.", 1, (0, 0, 0))
            minimumPointsCentering : int = minimumPointsLabel.get_width() / 2
            display.blit(minimumPointsLabel, [250-minimumPointsCentering,700])
        remainingRerollsLabel = smallFont.render(f"Remaining rerolls: {Kribbeln.getRemainigRerolls()}", 1, (0, 0, 0))
        xCentering : int = remainingRerollsLabel.get_width() / 2
        display.blit(remainingRerollsLabel, [250-xCentering,720])

    def drawDice(display) -> None:
        for i in range(6):
            xCoordinate = DiceRerollHandler.baseDicePos[0] + i*DiceRerollHandler.diceDistance
            yCoordinate = DiceRerollHandler.baseDicePos[1]
            if(Kribbeln.playingDice.toReroll[i] == False):
                yCoordinate += 400
            display.blit(pygame.image.load(os.path.join(Kribbeln.playingDice.allDice[i].getColorPath())),(xCoordinate, yCoordinate))
            display.blit(pygame.image.load(os.path.join(Kribbeln.playingDice.allDice[i].getValuePath())),(xCoordinate, yCoordinate))
        display.blit(pygame.image.load(os.path.join(DiceRerollHandler.getImagePath())),DiceRerollHandler.getHoverPosition())
        
    def drawTaskIcon(display) -> None:
        paths : list[str] = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconPaths()
        dev : list[int] = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconDeviations()
        iconWidth : int = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getIconWidth()
        for i in range(len(paths)):
            OGpic = pygame.image.load(os.path.join(paths[i]))
            width : int = 2*OGpic.get_width()
            hight : int = 2*OGpic.get_height()
            pic = pygame.transform.scale(OGpic,(width,hight))
            display.blit(pic,((960-iconWidth)+2*dev[i], 20))
        
    def drawCurrentPlayerLabel(display) -> None:
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("labels", "playerLabel"))),(0, 0))
        cFont  = pygame.font.SysFont("comicsans", 40)
        playerLabel = cFont.render(Kribbeln.players[Kribbeln.currentPlayerIndex].getName(), 1, (0, 0, 0))
        xCentering : int = 150 - (playerLabel.get_width() /2)
        yCentering : int = 75 - (playerLabel.get_height() /2)
        display.blit(playerLabel, [xCentering,yCentering])

    def drawKeepingDiceArea(display) -> None:
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("dice", "keepDiceArea"))),(450, 650))
        font  = pygame.font.SysFont("comicsans", 40)
        label = font.render("dice to keep:", 1, (255, 255, 255))
        xCentering : int = 1050 - (label.get_width() /2)
        display.blit(label, [xCentering,980])

    def drawTaskTable(display) -> None:
            isCompleted : bool = Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].isCompleted(Kribbeln.playingDice, Kribbeln.players[Kribbeln.currentPlayerIndex])
            display.blit(pygame.image.load(os.path.join(ImageHelper.getCompletionIndicator(isCompleted))),(560, -50))
            display.blit(pygame.image.load(os.path.join(ImageHelper.getTaskTable())),(560, -50))

    def on_event(event) -> None:
        mouse = pygame.mouse.get_pos()
        if(MainScreen.isShowQuitMessageBoard):
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()          
                if event.key == pygame.K_ESCAPE:
                    MainScreen.isShowQuitMessageBoard = False
            if MainScreen.quitMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()          
            if MainScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowQuitMessageBoard = False
        elif(MainScreen.isShowNextTurnMessageBoard):
            if event.type ==  pygame.KEYDOWN and event.key == pygame.K_RETURN:
                MainScreen.isShowNextTurnMessageBoard = False
                Kribbeln.nextPlayer()
            if MainScreen.nextTurnMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowNextTurnMessageBoard = False
                Kribbeln.nextPlayer()
        elif(MainScreen.isShowTaskInfo):
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    MainScreen.isShowTaskInfo = False
            if MainScreen.taskInfoMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowTaskInfo = False
        elif(MainScreen.isShowScoreBoard):
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    MainScreen.isShowScoreBoard = False
            if Kribbeln.scoreBoard.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowScoreBoard = False
        else:
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if Kribbeln.hasRemainingRerolls():
                        Kribbeln.playingDice.reroll()
                        Kribbeln.lowerRerollCounter()
                    else:
                        MainScreen.nextTurnMessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
                        MainScreen.isShowNextTurnMessageBoard = True
                if event.key == pygame.K_SPACE:
                        MainScreen.nextTurnMessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
                        MainScreen.isShowNextTurnMessageBoard = True
                if event.key == pygame.K_ESCAPE:
                    MainScreen.isShowQuitMessageBoard = True
                if event.key == pygame.K_TAB:
                    MainScreen.isShowScoreBoard = True
                if event.key == pygame.K_i:
                    MainScreen.taskInfoMessageBoard = MessageBoard(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getInfo())
                    MainScreen.isShowTaskInfo = True
            if MainScreen.taskInfoButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowTaskInfo = False
            if MainScreen.quitButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowQuitMessageBoard = True
            if MainScreen.scoreBoardButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.isShowScoreBoard = True
            if MainScreen.enableAllButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                Kribbeln.playingDice.enableAll()
            if MainScreen.disableAllButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                Kribbeln.playingDice.disableAll()
            if MainScreen.finishButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.nextTurnMessageBoard = MessageBoard([f"You got {Kribbeln.getResultingPoints()} points.",f"Next player will be {Kribbeln.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
                MainScreen.isShowNextTurnMessageBoard = True
            if MainScreen.disableRerollButton.checkForMouseInput(mouse[0], mouse[1]):
                pass #only for visual effect
            if MainScreen.rerollButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                if Kribbeln.hasRemainingRerolls():
                    Kribbeln.playingDice.reroll()
                    Kribbeln.lowerRerollCounter()
            if MainScreen.taskInfoButton.checkForMouseInput(mouse[0], mouse[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                MainScreen.taskInfoMessageBoard = MessageBoard(Kribbeln.scoreBoard.tasks[Kribbeln.currentRound].getInfo())
                MainScreen.isShowTaskInfo = True
            if DiceRerollHandler.setIndexWithMouse(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                DiceRerollHandler.switchReroll()
            if event.type ==  pygame.KEYDOWN:
                if (DiceRerollHandler.isArrowKey(event.key)):
                    DiceRerollHandler.handleKeyInput(event.key)
            DiceRerollHandler.setIndexWithMouse(mouse)

    def drawElements(display) -> None:
        MainScreen.drawKeepingDiceArea(display)
        MainScreen.drawCurrentPlayerLabel(display)
        MainScreen.drawTaskTable(display)
        MainScreen.drawTaskIcon(display)
        MainScreen.drawPointsLabel(display)
        MainScreen.drawDice(display)
        MainScreen.taskInfoButton.draw(display)
        MainScreen.quitButton.draw(display)
        MainScreen.finishButton.draw(display)
        MainScreen.scoreBoardButton.draw(display)
        MainScreen.rerollButton.draw(display)
        MainScreen.enableAllButton.draw(display)
        MainScreen.disableAllButton.draw(display)
        if(MainScreen.isShowQuitMessageBoard):
            MainScreen.quitMessageBoard.draw(display)
        elif(MainScreen.isShowNextTurnMessageBoard):
            MainScreen.nextTurnMessageBoard.draw(display)
        elif(MainScreen.isShowTaskInfo):
            MainScreen.taskInfoMessageBoard.draw(display)
        elif(MainScreen.isShowScoreBoard):
            Kribbeln.scoreBoard.drawAsOverlay(display)
        if not Kribbeln.hasRemainingRerolls():
            MainScreen.disableRerollButton.draw(display)

    def on_loop(display) -> None:
        display.blit(MainScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        MainScreen.drawElements(display)