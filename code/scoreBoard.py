from button import Button
from dice import Dice
from imageHelper import ImageHelper
from player import Player
from task import Task
from taskHelper import TaskHelper
import os.path
import pygame

class ScoreBoard:
    
    def __init__(self, players : list[Player]) -> None:
        self.players : list[Player]= players
        self.numberOfPlayers : int = len(self.players)
        self.tasks : list[Task] = TaskHelper.getDefaultTasks()
        self.points : list[list[int]] = self.getPointsTable()
        self.resultingPoints : list[list[int]] = self.getPointsTable()
        self.scores : list[list[int]] = self.getEmptyScores()
        if self.numberOfPlayers < 5:
            self.imageName : str = "scoreBoardBackgroundSmall"
            self.width : int = 850
        else:
            self.imageName : str = "scoreBoardBackground"
            self.width : int = 1300
        self.baseX : int = 960 - (self.width/2)
        self.baseY : int = 100
        self.closeButton : Button = Button(910+(self.width/2),100,50,50," ",imageName="close")

    def getEmptyScores(self) -> list[list[int]]:
        scoreTable : list[list[int]] = []
        for _ in range(self.numberOfPlayers):
            scoreTable.append([-1, -1, -1])
        return scoreTable

    def updateScore(self, roundIndex) -> None:
        if (roundIndex >= 2):
            for playerIndex in range(self.numberOfPlayers):
                self.scores[playerIndex][0] = 0
                self.scores[playerIndex][0] += self.resultingPoints[playerIndex][0]
                self.scores[playerIndex][0] += self.resultingPoints[playerIndex][1]
                self.scores[playerIndex][0] += self.resultingPoints[playerIndex][2]
        if (roundIndex >= 5):
            for playerIndex in range(self.numberOfPlayers):
                self.scores[playerIndex][1] = self.scores[playerIndex][0]
                self.scores[playerIndex][1] += self.resultingPoints[playerIndex][3]
                self.scores[playerIndex][1] += self.resultingPoints[playerIndex][4]
                self.scores[playerIndex][1] += self.resultingPoints[playerIndex][5]
        if (roundIndex >= 9):
            for playerIndex in range(self.numberOfPlayers):
                self.scores[playerIndex][2] = self.scores[playerIndex][1]
                self.scores[playerIndex][2] += self.resultingPoints[playerIndex][6]
                self.scores[playerIndex][2] += self.resultingPoints[playerIndex][7]
                self.scores[playerIndex][2] += self.resultingPoints[playerIndex][8]
                self.scores[playerIndex][2] += self.resultingPoints[playerIndex][9]

    def getPointList(self) -> list[int]:
        points : list[int] = []
        for _ in range(len(self.tasks)):
            points.append(-1)
        return points
    
    def getPointsTable(self) -> list[list[int]]:
        pointsTable : list[list[int]] = []
        for _ in range(self.numberOfPlayers):
            pointsTable.append(self.getPointList())
        return pointsTable
    
    def setPoints(self, dice : Dice, playerIndex : int, roundIndex : int) -> None:
        achievedPoints : int = 0
        if (self.tasks[roundIndex].isCompleted(dice, self.players[playerIndex])):
            achievedPoints = dice.getValues()
        self.points[playerIndex][roundIndex] = achievedPoints
        if (TaskHelper.isKribbelnTask(self.tasks[roundIndex])):
            self.players[playerIndex].setHighestKribblePoints(achievedPoints)

    def checkForMouseInput(self, xCoord, yCoord) -> bool:
        return self.closeButton.checkForMouseInput(xCoord, yCoord)

    def drawScores(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960-(width/2) + 225
        baseY : int = 360
        xDeviation : int = 150
        font  = pygame.font.SysFont("comicsans", 20)
        for playerIndex in range(self.numberOfPlayers):
            xCoord : int = baseX + (playerIndex*xDeviation)
            for scoreIndex in range(3):
                value : int = self.scores[playerIndex][scoreIndex]
                if value >= 0:
                    if scoreIndex == 0:
                        yAddition = 0
                    elif scoreIndex == 1:
                        yAddition = 200
                    else:
                        yAddition = 450
                    scoreLabel = font.render(f"{value}", 1, (0, 0, 0))
                    centering : int = (scoreLabel.get_width() /2)
                    display.blit(scoreLabel, [xCoord-centering, baseY+yAddition])

    def drawResultingPoints(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960-(width/2) +275
        baseY : int = 210
        xDeviation : int = 150
        yDeviation : int = 50
        font  = pygame.font.SysFont("comicsans", 20)
        for playerIndex in range(self.numberOfPlayers):
            xCoord : int = baseX + (playerIndex*xDeviation)
            for taskIndex in range(len(self.tasks)):
                yCoord : int = baseY + (taskIndex*yDeviation)
                value : int = self.resultingPoints[playerIndex][taskIndex]
                if value >= 0:
                    if taskIndex > 5:
                        yAddition = 100
                    elif taskIndex > 2:
                        yAddition = 50
                    else:
                        yAddition = 0
                    pointLabel = font.render(f"{value}", 1, (0, 0, 0))
                    centering : int = (pointLabel.get_width() /2)
                    display.blit(pointLabel, [xCoord-centering, yCoord+yAddition])

    def drawPoints(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960-(width/2)+200
        baseY : int = 210
        xDeviation : int = 150
        yDeviation : int = 50
        font  = pygame.font.SysFont("comicsans", 20)
        for playerIndex in range(self.numberOfPlayers):
            xCoord : int = baseX + (playerIndex*xDeviation)
            for taskIndex in range(len(self.tasks)):
                yCoord : int = baseY + (taskIndex*yDeviation)
                value : int = self.points[playerIndex][taskIndex]
                if value >= 0:
                    if taskIndex > 5:
                        yAddition = 100
                    elif taskIndex > 2:
                        yAddition = 50
                    else:
                        yAddition = 0
                    pointLabel = font.render(f"{value}", 1, (0, 0, 0))
                    centering : int = (pointLabel.get_width() /2)
                    display.blit(pointLabel, [xCoord-centering, yCoord+yAddition])

    def drawTasks(self, display) -> None:
        width2 : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960-(width2/2)+75
        baseY : int = 225
        yDeviation : int = 50
        for taskIndex in range(len(self.tasks)):
            paths : list[str] = self.tasks[taskIndex].getIconPaths()
            deviations : list[int] = self.tasks[taskIndex].getIconDeviations()
            width : int = self.tasks[taskIndex].getIconWidth()
            for iconIndex in range(len(paths)):
                if taskIndex > 5:
                    yAddition = 100
                elif taskIndex > 2:
                    yAddition = 50
                else:
                    yAddition = 0
                if width > 300:
                    scale = 0.4
                elif width > 250:
                    scale = 0.5
                elif width > 200:
                    scale = 0.6
                elif width > 150:
                    scale = 0.75
                else:
                    scale = 1
                pic =  pygame.image.load(os.path.join(paths[iconIndex]))
                scaledPic = pygame.transform.scale(pic,(scale*pic.get_width(),scale*pic.get_height()))
                display.blit(scaledPic,(baseX+(deviations[iconIndex]*scale)-(scale*width/2), baseY+(yDeviation*taskIndex)+yAddition-(scaledPic.get_height()/2)))

    def drawPlayerLabel(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960 - (width/2) + 75
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "userIcon"))),(baseX - 25, 145))
        font  = pygame.font.SysFont("comicsans", 20)
        for index in range(self.numberOfPlayers):
            playerLabel = font.render(self.players[index].getName(), 1, (0, 0, 0))
            centering : int = (150) - (playerLabel.get_width() /2)
            display.blit(playerLabel, [baseX+ (150*index)+centering,160])

    def drawGitter(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960 - (width/2)
        baseY : int = self.baseY + 50
        diff : int = 150
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "firstRow"))),(baseX, baseY))
        for index in range(self.numberOfPlayers- 1):
            display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "midRow"))),(diff+baseX+(diff*index), baseY))
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "lastRow"))),(baseX+((diff*self.numberOfPlayers)), baseY))

    def drawScoreLabels(self, display) -> None:
        width : int = 150 * (self.numberOfPlayers + 1)
        baseX : int = 960-(width/2)
        baseY : int = 350
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "score"))),(baseX, baseY))
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "score"))),(baseX, baseY+200))
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", "score"))),(baseX, baseY+450))

    def draw(self, display) -> None:
        self.drawGitter(display)
        self.drawTasks(display)
        self.drawPlayerLabel(display)
        self.drawPoints(display)
        self.drawResultingPoints(display)
        self.drawScores(display)
        self.drawScoreLabels(display)

    def drawAsOverlay(self, display) -> None:
        display.blit(pygame.image.load(os.path.join(ImageHelper.getImage("scoreBoard", self.imageName))),(self.baseX, self.baseY))
        self.draw(display)
        self.closeButton.draw(display)

    def getReducingPointsCausedByDuplicates(pairs, value, startIndex) -> int:
        valueCounter : int = -1
        for index in range(len(pairs)):
            if index >= startIndex:
                if pairs[index][0] == value:
                    valueCounter += 1
        return valueCounter

    def updateResultingPoints(self, roundIndex) -> None:
        pairs : list = []
        for playerIndex in range(self.numberOfPlayers):
            pairs.append((self.points[playerIndex][roundIndex], playerIndex))
        pairs.sort(key=lambda item: item[0], reverse=True)
        obtainablePoints : int = self.numberOfPlayers
        for index in range(self.numberOfPlayers):
            if (pairs[index][0] > 0):
                self.resultingPoints[pairs[index][1]][roundIndex] = obtainablePoints - ScoreBoard.getReducingPointsCausedByDuplicates(pairs, self.points[pairs[index][1]][roundIndex], index)
            else:
                self.resultingPoints[pairs[index][1]][roundIndex] = 0
            obtainablePoints -= 1