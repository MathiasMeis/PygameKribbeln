
class Player:
    name : str
    points : int

    def __init__(self, defaultName): # hier sollte standartmäßig Spieler 1, Spieler 2 etc stehen, umbenennen dann über die funktion rename
        self.name = defaultName
        self.points = 0


    def rename(self, newName):
        self.name = newName



    #def addPoints //siehe scoreboard