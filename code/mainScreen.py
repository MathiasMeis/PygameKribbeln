import pygame
import os
from scoreBoard import ScoreBoard
from game import Game
from gamestate import GameState
from diceRerollHandler import DiceRerollHandler
from imageHelper import ImageHelper
from button import Button
from messageBoard import MessageBoard

class MainScreen:
    taskInfoMessageBoard : MessageBoard
    quitMessageBoard : MessageBoard = MessageBoard(["Do you want to quit?"], hasButton=True, buttonText="QUIT", buttonFontColor=(255,255,255), buttenImageName="buttonRed")
    nextTurnMessageBoard : MessageBoard = MessageBoard([f"You got {Game.getResultingPoints()} points.",f"Next player will be {Game.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
    #Hier wird der ui stuff für das Würfel
  
    isShowScoreBoard : bool = False
    isShowQuitMessageBoard : bool = False
    isShowTaskInfo : bool = False
    isShowNextTurnMessageBoard : bool = False

    pygame.font.init()
    font  = pygame.font.SysFont("comicsans", 70)
    smallFont  = pygame.font.SysFont("comicsans", 30)

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

        if(ScoreBoard.tasks[Game.currentRound].isCompleted(Game.playingDice)):
            pointsLabel = pointFont.render(f"{Game.playingDice.getValues()}", 1, (0, 216, 36))
        else:
            pointsLabel = pointFont.render(f"{Game.playingDice.getValues()}", 1, (255, 0, 25))
        centering : int = (150) - (pointsLabel.get_width() /2)
        display.blit(pointsLabel, [100+centering,600])

    def drawDice(display,mouse):
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
    
    def drawTaskIcon(display):
        paths : list[str] = ScoreBoard.tasks[Game.currentRound].getIconPaths()
        dev : list[int] = ScoreBoard.tasks[Game.currentRound].getIconDeviations()
        iconWidth : int = ScoreBoard.tasks[Game.currentRound].getIconWidth()
        for i in range(len(paths)):
            OGpic = pygame.image.load(os.path.join(paths[i]))
            width : int = 2*OGpic.get_width()
            hight : int = 2*OGpic.get_height()
            pic = pygame.transform.scale(OGpic,(width,hight))
            display.blit(pic,((960-iconWidth)+2*dev[i], 20))
        
    def drawCurrentPlayerLabel(display):
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("labels", "playerLabel"))),(0, 0))
        cFont  = pygame.font.SysFont("comicsans", 40)
        playerLabel = cFont.render(Game.players[Game.currentPlayerIndex].getName(), 1, (0, 0, 0))
        xCentering : int = 150 - (playerLabel.get_width() /2)
        yCentering : int = 75 - (playerLabel.get_height() /2)
        display.blit(playerLabel, [xCentering,yCentering])


    def drawTaskTable(display): # Final
            isCompleted : bool = ScoreBoard.tasks[Game.currentRound].isCompleted(Game.playingDice)
            display.blit(pygame.image.load(os.path.join(ImageHelper.getCompletionIndicator(isCompleted))),(560, -50))
            display.blit(pygame.image.load(os.path.join(ImageHelper.getTaskTable())),(560, -50))



    def on_event(event):
        if(MainScreen.isShowQuitMessageBoard):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if MainScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]):
                    MainScreen.isShowQuitMessageBoard = False
                if MainScreen.quitMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]):
                    pygame.quit()          
        elif(MainScreen.isShowScoreBoard):
            pass
        elif(MainScreen.isShowTaskInfo):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if MainScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]):
                    MainScreen.isShowTaskInfo = False
        elif(MainScreen.isShowNextTurnMessageBoard):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if MainScreen.nextTurnMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1]):
                    MainScreen.isShowNextTurnMessageBoard = False
                if MainScreen.nextTurnMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1]):
                    Game.nextPlayer()
                    MainScreen.isShowNextTurnMessageBoard = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if(MainScreen.rerollButton.mouseIsIn(mouse[0],mouse[1])):
                    Game.playingDice.reroll()   
                if MainScreen.taskInfoButton.mouseIsIn(mouse[0],mouse[1]):
                    # TODO getInfo umschreiben
                    MainScreen.taskInfoMessageBoard = MessageBoard([ScoreBoard.tasks[Game.currentRound].getInfo()])
                    MainScreen.isShowTaskInfo = True
                    print("HI")
                if(MainScreen.finishButton.mouseIsIn(mouse[0],mouse[1])):
                    MainScreen.nextTurnMessageBoard = MessageBoard([f"You got {Game.getResultingPoints()} points.",f"Next player will be {Game.getNextPlayerName()}"], hasCloseButton=False, hasButton=True, buttonText="CONTINUE")
                    MainScreen.isShowNextTurnMessageBoard = True
                if (MainScreen.quitButton.mouseIsIn(mouse[0], mouse [1])):
                    MainScreen.isShowQuitMessageBoard = True
                if DiceRerollHandler.setIndexWithMouse(mouse):
                    DiceRerollHandler.switchReroll()
            if event.type ==  pygame.KEYDOWN:
                if (DiceRerollHandler.isArrowKey(event.key)):
                    DiceRerollHandler.handleKeyInput(event.key)


    def on_loop(display):
        display.blit(MainScreen.background, (0,0))
        mouse = pygame.mouse.get_pos()
        MainScreen.drawCurrentPlayerLabel(display)
        MainScreen.drawDice(display,mouse)
        MainScreen.drawTaskTable(display)
        MainScreen.drawTaskIcon(display)
        MainScreen.drawTask(display)
        MainScreen.drawPointsLabel(display)
        MainScreen.taskInfoButton.draw(display)
        MainScreen.taskInfoButton.mouseIsIn(mouse[0], mouse[1])
        MainScreen.quitButton.draw(display)
        MainScreen.quitButton.mouseIsIn(mouse[0], mouse[1])
        MainScreen.scoreBoardButton.draw(display)
        MainScreen.scoreBoardButton.mouseIsIn(mouse[0], mouse[1])
        MainScreen.finishButton.draw(display)
        MainScreen.finishButton.mouseIsIn(mouse[0], mouse[1])
        MainScreen.rerollButton.draw(display)
        MainScreen.rerollButton.mouseIsIn(mouse[0], mouse[1])
        MainScreen.taskInfoButton.mouseIsIn(mouse[0], mouse[1])
        if(MainScreen.isShowScoreBoard):
            print("Score")
        elif(MainScreen.isShowQuitMessageBoard):
            MainScreen.quitMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1])
            MainScreen.quitMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1])
            MainScreen.quitMessageBoard.draw(display)
        elif(MainScreen.isShowNextTurnMessageBoard):
            MainScreen.nextTurnMessageBoard.checkForMouseLocationOnButton(mouse[0], mouse[1])
            MainScreen.nextTurnMessageBoard.draw(display)
        elif(MainScreen.isShowTaskInfo):
            MainScreen.taskInfoMessageBoard.checkForMouseLocationOnCloseButton(mouse[0], mouse[1])
            MainScreen.taskInfoMessageBoard.draw(display)
