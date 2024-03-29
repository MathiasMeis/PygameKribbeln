from array import array
from color import Color
from die import Die

class Dice: 

    def __init__(self):
        self.dieBlack : Die = Die(Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK)
        self.dieBlue : Die = Die(Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN)
        self.dieGreen : Die = Die(Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK)
        self.dieOrange : Die = Die(Color.ORANGE, Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE)
        self.diePink : Die = Die(Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW)
        self.dieYellow : Die = Die(Color.YELLOW, Color.PINK, Color.BLACK, Color.GREEN, Color.BLUE, Color.ORANGE)
        self.allDice : list[Die] = [self.dieBlack, self.dieBlue, self.dieGreen, self.dieOrange, self.diePink, self.dieYellow]
        self.toReroll : list[bool] = [True, True, True, True, True, True]
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

    def enableAll(self):
        self.toReroll = [True, True, True, True, True, True]

    def disableAll(self):
        self.toReroll = [False, False, False, False, False, False]

    def enableReroll(self, number):
        self.toReroll[number] = True

    def disableReroll(self, number):
        self.toReroll[number] = False

    def switchReroll(self,number):
        if self.toReroll[number] == True:
            self.toReroll[number] = False
        else: self.toReroll[number] = True

    def getNumberOfColorInstances(self, color) -> int:
        numberOfInstances : int = 0
        for i in range(6):
            if self.allDice[i].getColor() == color:
                numberOfInstances += 1
        return numberOfInstances

    def getNumberOfColors(self) -> int:
        presentColors : list = []
        for i in range(6):
            if (presentColors.count(self.allDice[i].getColor()) == 0):
                presentColors.append(self.allDice[i].getColor())
        return len(presentColors)