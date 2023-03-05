class Player:
    def __init__(self, defaultName : str):
        self.name = defaultName
        self.highestKribbelPoints = 0

    def getName(self) -> str:
        return self.name
    
    def rename(self, newName : str) -> None:
        self.name = newName

    def getHighestKribblePoints(self) -> int:
        return self.highestKribbelPoints

    def setHighestKribblePoints(self, points : int) -> None:
        self.highestKribbelPoints = points
    