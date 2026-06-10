from enum import Enum, auto
from typing import Protocol
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Protocol
from common_types import Plant, Water, WaterBasic, WaterSteel, Turnip, Sunflower, Marigold

class Model(Protocol):
	_grid: list[list[str|Plant]]
	_water: Water
	_day:int
	_pesos:int
	_valid_crops: tuple[Plant]
	_game_over: bool
	_watered_list: list[list[int, int]]
	_valid_moves: tuple(str)

class AnimalCrossing:
	def __init__(self, water:Water):
		self._grid: list[list[str|Plant]] = list(list("." for _ in range(5)) for _ in range(5))
		self._water: Water = water
		self._day:int = 1
		self._pesos:int = 1000
		self._valid_crops: tuple[Plant] = (Turnip,)
		self._game_over: bool = False
		self._watered_list: list[tuple[int, int]] = []
		self._valid_moves: tuple(str) = ('p', 'w', 'h', 'g', 'n')

	@property
	def grid(self):
		return self._grid.copy()

	@property
	def water(self):
		return self._water
	
	@property
	def day(self):
		return self._day

	@property
	def pesos(self):
		return self._pesos

	@property
	def valid_crops(self):
		return self._valid_crops

	@property
	def game_over(self):
		return self._game_over

	@property
	def valid_moves(self):
		return self._valid_moves

	def next_day(self):
		self._day += 1
		lis = set(self._watered_list)
		lis = list(lis)
		for i, j in lis:
			self._grid[i][j].dec_days()
		self._watered_list = []


	def quit(self):
		self._game_over = True

	def plant(self, plant_name:str, i:int, j:int):
		if plant_name not in list(crop().name for crop in self._valid_crops):
			return False
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False
		if self._grid[i][j] != '.':
			return False
		else:
			for plant in self._valid_crops:
				if plant().name == plant_name:
					self._grid[i][j] = plant()
					self._pesos -= self._grid[i][j].cost
					return True

	def water(self, i:int, j:int):
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False
		else:
			for r, c in self._water.coords_to_water(i, j):
				if 0 <= r <= len(self._grid) and 0 <= c <= len(self._grid[0]):
					if self._grid[r][c] != ".":
						self._watered_list.append((r, c))
			return True

	def harvest(self, i:int, j:int):
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False

		all_empty:bool = True

		for r in range(len(self._grid)):
			for c in range(len(self._grid[0])):
				if self._grid[r][c] != '.':
					all_empty = False
		if all_empty:
			return False

		elif self._grid[i][j] == ".":
			return False
		elif not self._grid[i][j].days_left_to_grow <= 0:
			return False
		else:
			self._pesos += self._grid[i][j].harvest_val
			self._grid[i][j] = "."
			return True



class PlantsVsZombies:
	def __init__(self, water:Water):
		self._grid: list[list[str|Plant]] = list(list("." for _ in range(9)) for _ in range(5))
		self._water: Water = water
		self._day:int = 1
		self._pesos:int = 100
		self._valid_crops: tuple[Plant] = (Sunflower, Marigold)
		self._game_over: bool = False
		self._watered_list: list[tuple[int, int]] = []
		self._valid_moves: tuple(str) = ('p', 'w', 'h', 'g', 'n')

	@property
	def grid(self):
		return self._grid.copy()

	@property
	def water(self):
		return self._water
	
	@property
	def day(self):
		return self._day

	@property
	def pesos(self):
		return self._pesos

	@property
	def valid_crops(self):
		return self._valid_crops

	@property
	def game_over(self):
		return self._game_over

	@property
	def valid_moves(self):
		return self._valid_moves

	def next_day(self):
		self._day += 1
		lis = set(self._watered_list)
		lis = list(lis)
		for i, j in lis:
			self._grid[i][j].dec_days()
		self._watered_list = []


	def quit(self):
		self._game_over = True

	def plant(self, plant_name:str, i:int, j:int):
		if plant_name not in list(crop().name for crop in self._valid_crops):
			return False
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False
		if self._grid[i][j] != '.':
			return False
		else:
			for plant in self._valid_crops:
				if plant().name == plant_name:
					self._grid[i][j] = plant()
					self._pesos -= self._grid[i][j].cost
					return True

	def water(self, i:int, j:int):
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False
		else:
			for r, c in self._water.coords_to_water(i, j):
				if 0 <= r <= len(self._grid) and 0 <= c <= len(self._grid[0]):
					if self._grid[r][c] != ".":
						self._watered_list.append((r, c))
			return True

	def harvest(self, i:int, j:int):
		if not 0 <= i <= len(self._grid) or not 0 <= j <= len(self._grid[0]):
			return False

		all_empty:bool = True

		for r in range(len(self._grid)):
			for c in range(len(self._grid[0])):
				if self._grid[r][c] != '.':
					all_empty = False
		if all_empty:
			return False

		elif self._grid[i][j] == ".":
			return False
		elif not self._grid[i][j].days_left_to_grow <= 0:
			return False
		else:
			self._pesos += self._grid[i][j].harvest_val
			self._grid[i][j] = "."
			return True





