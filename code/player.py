from task import Task
from imageHelper import *

class Player:
    name : str
    highestKribbelPoints : int
    currentIndex : int

    def __init__(self, defaultName : str): # hier sollte standartmäßig Spieler 1, Spieler 2 etc stehen, umbenennen dann über die funktion rename
        self.name = defaultName
        self.points = 0
        self.highestKribbelPoints = 0

    def rename(self, newName):
        self.name = newName

    def getHighestKribblePoints(self) -> int:
        return self.highestKribbelPoints

    def getName(self):
        return self.name