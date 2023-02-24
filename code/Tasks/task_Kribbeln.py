from dice import Dice
from task import Task

#from player import Player

class Task_Kribbeln(Task): # 1 mal eine Farbe
    minimumPoints : int = 0

   # player : Player

    def __init__(self): #referenz auf player oder scoreboard
        super().__init__(0)

    def isCompleted(self, dice : Dice) -> bool:
        if (Task_Kribbeln.minimumPoints < dice.getValues()):
            return True
        else:
            return False
        
    #def setPlayer(self, playerRef : Player):
    #    self.player = playerRef


    def getInfo(self) -> str:
        if (Task_Kribbeln.minimumPoints == 0):
            return "Get as many points as you want. But you might need to top it later on."
        else:
            return f"Get at least {Task_Kribbeln.minimumPoints + 1} points."

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()