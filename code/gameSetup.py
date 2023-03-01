# UI stuff, startbildschirm mit spieleranzahlauswahl, spielerbenennung, später ggfs modusauswahl

from player import Player 

class GameSetup:
    numberOfPlayers : int = 1
    players : list[Player] = [Player('Player 1')]
    currentIndex : int

    def addPlayer():
        GameSetup.numberOfPlayers += 1
        GameSetup.players.append(Player(f"Player {GameSetup.numberOfPlayers}"))

    def removePlayer():
        GameSetup.players.remove(GameSetup.players[GameSetup.numberOfPlayers-1])#GameSetup.currentIndex
        GameSetup.numberOfPlayers -= 1

    def renamePlayer(newName):
        GameSetup.players[GameSetup.currentIndex].rename(newName)