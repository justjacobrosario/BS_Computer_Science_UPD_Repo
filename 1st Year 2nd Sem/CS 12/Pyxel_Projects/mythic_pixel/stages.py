from map_generator import upd_map
import map_data
from typing import Protocol
from enum import Enum, auto

class Difficulty(Enum):
    Normal = auto()
    Hard = auto()
    Nightmare = auto()


class Stage(Protocol):
    difficulty : Difficulty
    map_pic_path : str

    def generate_map():
        ...


class Grasslands:
    def __init__(self):
        self.difficulty = Difficulty.Normal
        self.map_pic_path = "15_15_Grasslands.png"
        self.py_path = "map_data.py"

    def generate_map(self):
        upd_map(self.map_pic_path, self.py_path)

class Drylands:
    def __init__(self):
        self.difficulty = Difficulty.Normal
        self.map_pic_path = "15_15_Grasslands.png"
        self.py_path = "map_data.py"

    def generate_map(self):
        upd_map(self.map_pic_path, self.py_path)

class Winterlands:
    def __init__(self):
        self.difficulty = Difficulty.Normal
        self.map_pic_path = "15_15_Grasslands.png"
        self.py_path = "map_data.py"

    def generate_map(self):
        upd_map(self.map_pic_path, self.py_path)
    