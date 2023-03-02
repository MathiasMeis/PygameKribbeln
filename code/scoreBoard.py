from task import Task
from taskHelper import TaskHelper
from player import Player
from gameSetup import GameSetup
from dice import Dice


#hier werden die aufgaben gesetzt. 2xeasy + kribbeln1 + 2xmedium + kribbeln2 + 2xhard + kribbeln3+4
# ui stuff dafür könnte auch in ne andere klasse ausgelagert werden, wenns zu viel wird
# ui sollte beim würfeln als overlay realisiert werden, könnte über hide() und show() getooglet werden
# punkte können hier oder beim spieler selbst hinterlegt werden. letzteres könnte sinniger sein, wenn man die spielerreihenfolge variabel nach punkten macht
# bzw ab 2tem kribbeln nach punkten schauen
class ScoreBoard:
    tasks : list[Task] = TaskHelper.getEveryTask()
    playerindex : int = -1
    points : list[list[int]]
    resultingPoints : list[list[int]]




    def getNextTask(self) -> Task:
        self.round = self.round +1
        return self.tasks[self.round]



    def getLatestKribblePoints(self, player) -> int: #liefer die punktzahl vom letzten kribbeln des übergebenen sppilers
        print()



    def getPointList() -> list[int]:
        points : list[int] = []
        for _ in range(len(ScoreBoard.tasks)):
            points.append(-1)

        #print(points)
        return points
    
    def setUpPointTable() -> None:
        ScoreBoard.points : list[list[int]] = []
        for _ in range(GameSetup.numberOfPlayers):
            ScoreBoard.points.append(ScoreBoard.getPointList())

        ScoreBoard.points

    
    def setPoints(dice : Dice, playerIndex : int, roundIndex : int):
        achievedPoints : int = 0
        currentTask : Task = ScoreBoard.tasks[roundIndex]
        if (TaskHelper.isKribbelnTask(currentTask)):
            TaskHelper.setKribbelnMinumum(GameSetup.players[playerIndex].getHighestKribblePoints())

        isComleted : bool = currentTask.isCompleted(dice)
        if (isComleted):
            achievedPoints = dice.getValues()
        ScoreBoard.points[ScoreBoard.playerindex][ScoreBoard.round] = achievedPoints


