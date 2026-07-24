from enum import Enum
from constants import ShipType, Level_to_Ship, ShipToTile, Cargo

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
        self._fuel = self._ship.value["fuel"]
        self._min_lvl_req = self._ship.value["min_lvl_req"]

        self._curr_fuel = self._fuel
        self._curr_cargo = {Cargo.RED: 0, Cargo.ORANGE: 0, Cargo.YELLOW: 0, Cargo.GREEN: 0, Cargo.BLUE: 0}
        self._total_cargo = 0
        self._exp = 0
        self._is_dead = False
        self._cargo_priority = None # Prioritizes a specific cargo type, None means no priorities

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

    @property
    def exp(self):
        return self._exp

    @property
    def total_cargo(self):
        return self._total_cargo
    
    @exp.setter
    def exp(self, val):
        self._exp = val

    def upd_total_cargo(self):
        self._total_cargo = sum(self._curr_cargo.values())

    def lvl_up(self):
        self._lvl += 1
        self._ship = Level_to_Ship[self._lvl]
        self._ship_name = self._ship.value["name"]
        self._hp = self._ship.value["hp"]
        self._speed = self._ship.value["speed"]
        self._max_cargo = self._ship.value["max_cargo"]
        self._fuel = self._ship.value["fuel"]
        self._curr_fuel = self._fuel
        self._min_lvl_req = self._ship.value["min_lvl_req"]
    
    def add_cargo(self, cargo_type: Cargo):
        if cargo_type in self._curr_cargo:
            self._curr_cargo[cargo_type] += 1
        else:
            raise ValueError(f"Invalid cargo type: {cargo_type}")
    
    def remove_cargo(self, cargo_type: Cargo):
        if cargo_type in self._curr_cargo:
            if self._curr_cargo[cargo_type] >= 1:
                self._curr_cargo[cargo_type] -= 1
            else:
                raise ValueError(f"Not enough cargo of type {cargo_type} to remove. Current amount: {self._curr_cargo[cargo_type]}")
        else:
            raise ValueError(f"Invalid cargo type: {cargo_type}")
    
    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Refuel amount cannot be negative.")
        self._curr_fuel = min(self._curr_fuel + amount, self._fuel)
    
    def consume_fuel(self, amount):
        if amount >= 0:
            self._curr_fuel = max(self._curr_fuel - amount, 0)
    
    def check_if_dead(self):
        if self._hp <= 0 or self._curr_fuel <= 0:
            self._is_dead = True
        return self._is_dead
    
    
    
    
    
    
    

