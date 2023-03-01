from enum import Enum

class GameState(Enum):
    STARTING: int = 0
    PLAYING : int = 1
    ENDING: int = 2
    FINISHED: int = 3