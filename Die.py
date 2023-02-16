import Color

class Die:
    firstSide = None #: (int, Color)
    secondSide = None
    thirdSide = None
    fourthSide = None
    fifthSide = None
    sixthSide = None

    sides : list = [firstSide, secondSide, thirdSide, fourthSide, fifthSide, sixthSide]
    currentSide = None

    def __init__(self, col1, col2, col3, col4, col5, col6):
        self.firstSide = (1,col1)
        self.secondSide = (2,col2)
        self.thirdSide = (3,col3)
        self.fourthSide = (4, col4)
        self.fifthSide = (5, col5)
        self.sixthSide = (6, col6)
        self.currentSide = self.firstSide


    def getValue(self):
        return self.currentSide[0] # value of current

    def getColor(self):
        return self.currentSide[1] # return current color

    def roll(self):
        self.currentSide = self.currentSide # randomSide



    def getPic(self, value):
        return f"Die_{value[0]}_{value[1]}"
        if value[1] == Color.GREEN:
            if value[0] == 1:
                return "green1"
            if value[0] == 2:
                return "green2"
            if value[0] == 3:
                return "green3"
            if value[0] == 4:
                return "green4"
            

    def getRandomPic(self):
        print() # return random pic for animation, ggfs anders lösen


    #def returnCurrent() 



