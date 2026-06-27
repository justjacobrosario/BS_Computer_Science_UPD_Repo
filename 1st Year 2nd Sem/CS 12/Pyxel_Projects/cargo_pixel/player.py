from enum import Enum
from constants import ShipType, Level_to_Ship, ShipToTile

class Player:
    def __init__(self, x, y, lvl):
        self.x = x
        self.y = y
        self._lvl = lvl
        self._ship = Level_to_Ship[lvl]
        self._ship_name = self._ship.value["name"]
        self._hp = self._ship.value["hp"]
        self._speed = self._ship.value["speed"]
        self._max_cargo = self._ship.value["max_cargo"]
        self._curr_cargo = 0
        self._fuel = self._ship.value["fuel"]
        self._curr_fuel = self._fuel
        self._min_lvl_req = self._ship.value["min_lvl_req"]

    @property
    def lvl(self):
        return self._lvl

    @property
    def ship(self):
        return self._ship

    @property
    def ship_name(self):
        return self._ship_name

    @property
    def hp(self):
        return self._hp

    @property
    def speed(self):
        return self._speed

    @property
    def max_cargo(self):
        return self._max_cargo
    
    @property
    def curr_cargo(self):
        return self._curr_cargo

    @property
    def fuel(self):
        return self._fuel
    
    @property
    def curr_fuel(self):
        return self._curr_fuel

    @property
    def min_lvl_req(self):
        return self._min_lvl_req

    def lvl_up(self):
        self._lvl += 1
        self._ship = Level_to_Ship[lvl]
        self._ship_name = self._ship.value["name"]
        self._hp = self._ship.value["hp"]
        self._speed = self._ship.value["speed"]
        self._max_cargo = self._ship.value["max_cargo"]
        self._curr_cargo = 0
        self._fuel = self._ship.value["fuel"]
        self._curr_fuel = self._fuel
        self._min_lvl_req = self._ship.value["min_lvl_req"]
    
    
    
    
    
    
    
    

