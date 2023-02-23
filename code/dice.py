from die import Die
from array import array
from color import Color

class Dice: 

    def __init__(self):
        self.dieBlack : Die = Die(Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK)
        self.dieBlue : Die = Die(Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN)
        self.dieGreen : Die = Die(Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK)
        self.dieOrange : Die = Die(Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE)
        self.diePink : Die = Die(Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW)
        self.dieYellow : Die = Die(Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE)
        self.allDice : list[Die] = [self.dieBlack, self.dieBlue, self.dieGreen, self.dieOrange, self.diePink, self.dieYellow]
        self.toReroll : list[bool] = [False, False, False, False, False, False]
        self.total = 0

    def getValues(self) -> int:
        total : int = 0
        for i in range(6):
            total += self.allDice.__getitem__(i).getValue()
        return total
 
    def reroll(self):
        for i in range(6):
            if (self.toReroll[i]):
                self.allDice.__getitem__(i).roll()

    def resetReroll(self):
        self.toReroll = [False, False, False, False, False, False]
        self.reroll()

    def enableReroll(self, number):
        self.toReroll[number] = True

    def disableReroll(self, number):
        self.toReroll[number] = False

    def getNumberOfColorInstances(self, color) -> int:
        numberOfInstances : int = 0
        for i in range(6):
            if self.allDice[i].getColor() == color:
                numberOfInstances += 1
        return numberOfInstances

    def getNumberOfColors(self) -> int:
        presentColors : list = []
        for i in range(6):
            presentColors.append(self.allDice[i].getColor())
        return len(presentColors)


    def getNumberOfInstancesAsArray(self) -> array:
        instanceNumbers : array = array(0, 0, 0, 0, 0, 0)
        allColors : list = Color.getAllColors()
        for i in range(6):
            instanceNumbers[i] = self.getNumberOfColorInstances(allColors[i])
        
        return instanceNumbers
    
    def show(self): #only for testing purpose, delete later
        print(self.dieBlack.show(), self.dieBlue.show(), self.dieGreen.show(), self.dieOrange.show(), self.diePink.show(), self.dieYellow.show()) 
