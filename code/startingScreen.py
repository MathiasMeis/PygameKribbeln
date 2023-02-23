# UI stuff, startbildschirm mit spieleranzahlauswahl, spielerbenennung, später ggfs modusauswahl

from player import Player 



class StartingScreen:
    numberOfPlayers : int = 0
    players : list[Player] = []
    currentIndex : int

    def addPlayer():
        StartingScreen.numberOfPlayers += 1
        StartingScreen.players.append(Player(f"Player {StartingScreen.numberOfPlayers}"))

    def removePlayer():
        StartingScreen.players.remove(StartingScreen.players[StartingScreen.currentIndex])
        StartingScreen.numberOfPlayers += 1

    def renamePlayer():
        newName : str = "" #inputfeld
        StartingScreen.players[StartingScreen.currentIndex].rename(newName)