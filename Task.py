import Difficulty
import Color

# Oberklasse für alle Tasks, namensgebung für unterklassen noch fragwürdig
# unterklassen sollten alle 4 mothoden überschreiben, letztere kann erstmal warten
class Task:
    difficulty : Difficulty
    numberOfColors : int
    colors : list


    def __init__(self):
        self.difficulty = Difficulty.EASY
        self.numberOfColors = 0 # ggfs überflüssig colors sollt reichen
        self.colors = None # Color.getColors(self.numberOfColors) 


    def isCompleted(self, dice) -> bool: #override
        return True
    
    def getInfo(self) -> str: #falls wir nen infopanel zum drüberhovern machen sollten, oben im default screen, nicht unbedingt scoreboard
        return " "

    def getImage(self): # return zusammengebasteltes Bild mit fester größe
        print()




# Hier einige Vorschläge für Aufgabenarten. können natürlich auch mehr oder weniger sein.

#Easy
#0 mal FarbeX
#1 mal FarbeX
#1 mal FarbeX und 0 mal FarbeY
#2 mal FarbeX
#2 mal FarbeX und 0 mal FarbeY
#0 mal FarbeX und 0 mal FarbeY
#min 2 mal FarbeX
#
#Medium
#3 mal FarbeX
#min 3 mal FarbeX
#2 mal FarbeX und 0 mal FarbeY
#nur 2 Farben
#nur 3 Farben
#3 mal bel Farbe
#nicht 3 mal bel Farbe
#nicht 2 mal bel Farbe
#3 mal bel Farbe und 2 mal bel andere Farbe
#2 mal bel Farbe und 2 mal bel andere Farbe
#
#Hard
#4 mal bel Farbe
#5 mal bel farbe
#FarbeX = FarbeY
#FarbeX != FarbeY
#FarbeX = FarbeY = FarbeZ
#FarbeX != FarbeY != FarbeZ
#FarbeX > FarbeY
#FarbeX > alle Farben
