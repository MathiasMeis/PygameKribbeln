import Die
import array
import Color

class Dice:
    dieBlack = Die(Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE,Color.YELLOW,Color.PINK)
    dieBlue = Die(Color.BLUE, Color.ORANGE, Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN)
    dieGreen = Die(Color.GREEN, Color.BLUE, Color.ORANGE, Color.YELLOW,Color.PINK,Color.BLACK)
    dieOrange = Die(Color.ORANGE,Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE) # Reihenfolge farben 1-6 1 ist im namen
    diePink = Die(Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE,Color.YELLOW)
    dieYellow = Die(Color.YELLOW,Color.PINK,Color.BLACK, Color.GREEN, Color.BLUE,Color.ORANGE)

    allDice : list [dieBlack, dieBlue, dieGreen, dieOrange, diePink, dieYellow]

    toReroll : array = array(False, False, False, False, False, False)
    total : int

    def getValues(self) -> int:
        return 1 # summe aller values der würfen
    

    def __init__(self):
        self.total = self.getValues()

    def reroll(self):
        for i in range(6):
            if (self.toReroll[i]):
                self.allDice.__getitem__(i).roll()


        print() # jenach 0,1 rerollen

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



        