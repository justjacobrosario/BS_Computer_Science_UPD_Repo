import pyxel
from controller import Controller
from model import Model
from view import View
from world import World

if __name__ == "__main__":
	controller = Controller(Model("map_setup.txt", 1), View())
	controller.run_game()