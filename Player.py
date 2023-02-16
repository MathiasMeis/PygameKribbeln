
class Player:
    name : str
    points : list
    highestKribbelPoints : int

    def __init__(self, defaultName): # hier sollte standartmäßig Spieler 1, Spieler 2 etc stehen, umbenennen dann über die funktion rename
        self.name = defaultName
        self.points = 0
        self.highestKribbelPoints = 0


    def rename(self, newName):
        self.name = newName

    def setTasks(self, tasks):
        for i in range(len(tasks)):
            self.points.append((tasks[i], -1)) #-1 für noch offenen task

    def getHighestKribblePoints(self) -> int:
        return self.highestKribbelPoints





    #def addPoints //siehe scoreboard