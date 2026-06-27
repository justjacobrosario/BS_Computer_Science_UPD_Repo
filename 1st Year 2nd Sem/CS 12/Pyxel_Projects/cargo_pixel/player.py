from enum import Enum
from constants import ShipType, Level_to_Ship, Ship_to_Tile

class Player:
	def __init__(self, x, y, lvl):
		self._x = x
		self._y = y
		self._lvl = lvl
		self._ship = Level_to_Ship[lvl]
		self._ship_name = self._ship.value["name"]
		self._hp = self._ship.value["hp"]
		self._speed = self._ship.value["speed"]
		self._max_cargo = self._ship.value["max_cargo"]
		self._cargo = 0
		self._fuel = self._ship.value["fuel"]
		self._curr_fuel = self._fuel
		self._min_lvl_req = self._ship.value["min_lvl_req"]



