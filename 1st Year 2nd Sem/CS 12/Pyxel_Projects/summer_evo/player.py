from enum import Enum
from constants import Color, Key_Input, Animal


class Player:
    def __init__(self, x, y, animal_type = Animal.FLY):
        self._color = animal_type.value["color"]
        self._x = x
        self._y = y
        self._speed = 1

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def animal_type(self):
        return self._animal_type
    
    @property
    def speed(self):
        return self._speed

    @property
    def color(self):
        return self._color
    

    @x.setter 
    def x(self, val_input: int):
        self._x = val_input

    @y.setter 
    def y(self, val_input: int):
        self._y = val_input
    
    @animal_type.setter 
    def animal_type(self, val_input: int):
        self._animal_type = val_input