from color import Color
from dieSide import DieSide
import random

class Die:


    def __init__(self, col1 : Color, col2 : Color, col3 : Color, col4 : Color, col5 : Color, col6 : Color):
        self.firstSide : DieSide = DieSide(1,col1)
        self.secondSide : DieSide = DieSide(2,col2)
        self.thirdSide : DieSide = DieSide(3,col3)
        self.fourthSide : DieSide = DieSide(4, col4)
        self.fifthSide : DieSide = DieSide(5, col5)
        self.sixthSide : DieSide = DieSide(6, col6)
        self.allSides : list[DieSide] = [self.firstSide, self.secondSide, self.thirdSide, self.fourthSide, self.fifthSide, self.sixthSide]
        self.currentSide : DieSide = self.firstSide


    def getValue(self) -> int:
        return self.currentSide.getValue() # value of current

    def getColor(self) -> Color:
        return self.currentSide.getColor() # return current color

    def roll(self) -> None:
        self.currentSide = random.sample(self.allSides,1)[0]



    def getPic(self, value):
        print() #get image of die at value

    def getRandomPic(self):
        print() # return random pic for animation, ggfs anders lösen

    def show(self) -> str: #only for testing purpose, delete later
        return f" < {self.getValue()},{self.getColor().name}> "

    #def returnCurrent() 



