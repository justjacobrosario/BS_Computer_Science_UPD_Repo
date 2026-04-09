from enum import Enum, auto
from typing import Protocol
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Protocol
from common_types import Plant, Water, WaterBasic, WaterSteel, Turnip

class View:
	def ask_action(self, valid_moves: tuple[str]):
		move:str = input("Action:\n- ")

		if move not in valid_moves:
			return False

		else:
			return move


	def ask_crop(self, valid_crops:tuple[Plant]):
		valid: str = ''
		for i, crop in enumerate(valid_crops):
			if i == len(valid_crops) - 1:
				valid += crop().name
			else:
				valid += crop().name + ", "

		crop:str = input(f"Crops: {valid}\n- ")

		return crop

	def ask_coords(self):
		coord:str = input(f"Location (i j):\n- ")
		try:
			i, j = coord.split()
			return (int(i), int(j))
		except Exception:
			return (-1, -1)

	def display_pesos(self, pesos:int):
		print(f"Pesos: {pesos}")

	def display_day(self, day:int):
		print(f"=====\n\nDay: {day}")

	def display_grid(self, grid:list[list[str|Plant]]):
		r = len(grid)
		c = len(grid[0])

		for i in range(r):
			line:str = ""
			for j in range(c):
				if grid[i][j] == ".":
					line += "."
				else:
					if grid[i][j].days_left_to_grow <= 0:
						line += grid[i][j].harvestable_sprite
					else:
						line += grid[i][j].growing_sprite
			print(line)

		print()

	def display_is_success(self, verdict:bool):
		if verdict:
			print("Success!\n")
		else:
			print("Failed.\n")

	def display_day_ended(self):
		print("Day ended.\n")

