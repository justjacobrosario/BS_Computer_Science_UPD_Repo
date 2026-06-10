from enum import Enum, auto
from typing import Protocol
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Protocol
from common_types import Plant, Water, WaterBasic, WaterSteel, Turnip
from model_part1 import Model, AnimalCrossing, PlantsVsZombies
from view import View

class Controller:
	def __init__(self, model:Model, view:View):
		self._model = model
		self._view = view

	def run(self):
		model = self._model
		view = self._view

		view.display_day(model.day)
		view.display_pesos(model.pesos)
		view.display_grid(model.grid)

		while not model.game_over:
			action: bool | str = False
			while action == False: 
				action = view.ask_action(model.valid_moves)

			if action != False:
				if action == "p":
					crop = view.ask_crop(model.valid_crops)
					if crop != False:
						coords: tuple[int, int] = view.ask_coords()
						is_success = model.plant(crop, coords[0], coords[1])
						view.display_is_success(is_success)

				elif action == "w":
					coords: tuple[int, int] = view.ask_coords()
					is_success = model.water(coords[0], coords[1])
					view.display_is_success(is_success)

				elif action == "h":
					coords: tuple[int, int] = view.ask_coords()
					is_success = model.harvest(coords[0], coords[1])
					view.display_is_success(is_success)

				elif action == "g":
					view.display_pesos(model.pesos)
					view.display_grid(model.grid)

				elif action == "n":
					model.next_day()
					view.display_day_ended()
					view.display_day(model.day)
			else:
				view.display_is_success(False)


ey = set([1, 2, 3, 4, 4])
ey = list(ey)
print(ey)