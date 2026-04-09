import argparse
from enum import Enum, auto
from typing import Protocol
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Protocol
from common_types import Plant, Water, WaterBasic, WaterSteel, Turnip
from model_part1 import Model, AnimalCrossing, PlantsVsZombies
from view import View
from controller import Controller



if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--mode', choices=['ac', 'pvz'], required = True)
	parser.add_argument('--water', choices=['basic', 'steel'], required = True)

	args = parser.parse_args()

	match args.mode, args.water:
		case 'ac', 'basic':
			_model = AnimalCrossing(WaterBasic())
		case 'ac', 'steel':
			_model = AnimalCrossing(WaterSteel())
		case 'pvz', 'basic':
			_model = PlantsVsZombies(WaterBasic())
		case 'pvz', 'steel':
			_model = PlantsVsZombies(WaterSteel())
		case _:
			raise ValueError("Unexpected parameters for modes and water")


	_view = View()
	_controller = Controller(_model, _view)
	_controller.run()

		
		


