from enum import Enum, auto
from typing import Protocol
from abc import ABC, abstractmethod

class Water(ABC):
	@abstractmethod
	def coords_to_water(self, i:int, j:int):
		pass
class WaterBasic(Water):
	def coords_to_water(self, i:int, j:int):
		return [[i, j]]

class WaterSteel(Water):
	def coords_to_water(self, i:int, j:int):
		neighbors:list[list[int,int]] = []
		v_shift = [1, -1, 0]
		h_shift = [1, -1, 0]

		for shift1 in v_shift:
			for shift2 in h_shift:
				neighbors.append([i + shift1, j + shift2])

		return neighbors

class Plant(Protocol):
	cost: int
	growth_days: int
	days_left_to_grow: int
	harvest_val: int
	name: str
	growing_sprite: str
	harvestable_sprite: str


	def dec_days():
		pass

class Turnip:
	def __init__(self):
		self.cost: int = 300
		self.growth_days: int = 2
		self.days_left_to_grow: int = 2
		self.harvest_val: int = 500
		self.name: str = "turnip"
		self.growing_sprite: str = 't'
		self.harvestable_sprite: str = 'T'


	def dec_days(self):
		self.days_left_to_grow -= 1


class Sunflower:
	def __init__(self):
		self.cost: int = 25
		self.growth_days: int = 1
		self.days_left_to_grow: int = 1
		self.harvest_val: int = 50
		self.name: str = "sunflower"
		self.growing_sprite: str = 's'
		self.harvestable_sprite: str = 'S'


	def dec_days(self):
		self.days_left_to_grow -= 1

class Marigold:
	def __init__(self):
		self.cost: int = 50
		self.growth_days: int = 2
		self.days_left_to_grow: int = 2
		self.harvest_val: int = 150
		self.name: str = "marigold"
		self.growing_sprite: str = 'm'
		self.harvestable_sprite: str = 'M'


	def dec_days(self):
		self.days_left_to_grow -= 1
