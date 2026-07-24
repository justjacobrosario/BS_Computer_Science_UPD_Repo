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
    GO_UP = auto()
    GO_DOWN = auto()
    GO_LEFT = auto()
    GO_RIGHT = auto()
    GO_UP_2 = auto(),
    GO_DOWN_2 = auto()
    GO_LEFT_2 = auto()
    GO_RIGHT_2 = auto()
    NONE = auto()

class ShipType(Enum):
    Tugboat = {
        "name" : "Tugboat",
        "hp" : 100, 
        "speed" : 1, 
        "max_cargo" : 50, 
        "fuel" : 100, 
        "min_lvl_req" : 0}
    Mini_Bulk_Carriers = {
        "name" : "Mini-Bulk Carriers",
        "hp" : 100, 
        "speed" : 1, 
        "max_cargo" : 50, 
        "fuel" : 100, 
        "min_lvl_req" : 0}
    Roro = {
        "name" : "RORO Ship",
        "hp" : 100, 
        "speed" : 1, 
        "max_cargo" : 50, 
        "fuel" : 100, 
        "min_lvl_req" : 0}
    Super_Tanker = {
        "name" : "Super Tanker",
        "hp" : 100, 
        "speed" : 1, 
        "max_cargo" : 50, 
        "fuel" : 100, 
        "min_lvl_req" : 0}

Level_to_Ship = {
    0 : ShipType.Tugboat,
    1 : ShipType.Mini_Bulk_Carriers,
    2 : ShipType.Roro,
    3 : ShipType.Super_Tanker
}

class ShipToTile(Enum):
    Tugboat = (0,8),
    Mini_Bulk_Carriers = (8, 8),
    Roro = (16, 8),
    Super_Tanker = (24, 8)

