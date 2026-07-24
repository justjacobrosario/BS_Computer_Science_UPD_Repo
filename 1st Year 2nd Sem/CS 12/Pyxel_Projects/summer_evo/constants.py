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


class Animal(Enum):
    FLY = {"color" : Color.LIGHT_GRAY}
    BUTTERFLY = {"color" : Color.BLUE}
    CHICKEN = {"color" : Color.BROWN}
    ALL = {"color" : Color.BLACK}

    