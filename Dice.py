import Die
import array
import Color

class Dice:
    dieBlack = Die(Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE,Color.YELLOW,Color.PINK)
    dieBlue = Die(Color.BLUE, Color.ORANGE, Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN)
    dieGreen = Die(Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW,Color.PINK,Color.BLACK)
    dieOrange = Die(Color.ORANGE,Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE)
    diePink = Die(Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE,Color.YELLOW)
    dieYellow = Die(Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE)

    allDice : list [dieBlack, dieBlue, dieGreen, dieOrange, diePink, dieYellow]
    toReroll : array = array(False, False, False, False, False, False)
    total : int

    def getValues(self) -> int:
        total : int = 0
        for i in range(6):
            total += self.allDice[i].getValue()
        return total
    

    def __init__(self):
        self.total = self.getValues()

    def reroll(self):
        for i in range(6):
            if (self.toReroll[i]):
                self.allDice.__getitem__(i).roll()

    def resetReroll(self):
        self.toReroll = array(False, False, False, False, False, False)
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
    