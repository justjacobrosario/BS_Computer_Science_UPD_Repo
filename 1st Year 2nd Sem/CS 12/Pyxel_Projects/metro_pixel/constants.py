from enum import Enum, IntEnum, auto

class Color(IntEnum):
    BLACK = 0
    DARK_BLUE = 1
    DARK_PURPLE = 2
    DARK_GREEN = 3
    BROWN = 4
    DARK_GRAY = 5
    LIGHT_GRAY = 6
    WHITE = 7
    RED = 8
    ORANGE = 9
    YELLOW = 10
    GREEN = 11
    BLUE = 12
    LAVENDER = 13
    PINK = 14
    PEACH = 15

class Tile(Enum):
    GRASS = 0
    OCEAN = 1
    SEA = 2
    SAND = 3
    SNOW = 4
    PORT = 5


class Key_Input(Enum):
    QUIT = auto()
    ZOOM_IN = auto()
    ZOOM_OUT = auto()
    NONE = auto()

class GameError(Enum):
    WRONG_PW = auto()
    ACC_NOT_EXISTING = auto()
    ACC_EXISTS = auto()
    ACC_ALREADY_LOGGED_IN = auto()
    ACC_NOT_LOGGED_IN = auto()

class GameMode(Enum):
    CLASSIC = auto()
    ENDLESS = auto()

class BuildingType(Enum):
    APARTMENT = auto()

class PassengerType(Enum):
    CIVILIAN = auto()

class ToolType(Enum):
    ROAD = auto()
    JEEP = auto()

class AppState(Enum):
    MAIN_MENU = auto()
    LOGIN = auto()
    SIGNUP = auto()
    MODE_SELECT = auto()
    MAP_SELECT = auto()
    IN_GAME = auto()

TOOL_COSTS = {
    ToolType.ROAD : 50,
    ToolType.JEEP : 500,
}



# Timing constants
FPS = 30

