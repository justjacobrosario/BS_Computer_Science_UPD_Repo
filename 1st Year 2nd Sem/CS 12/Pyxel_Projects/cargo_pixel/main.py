import pyxel
from controller import Controller
from model import Model
from view import View

if __name__ == "__main__":
    controller = Controller(Model(1980, 1080, "map_data.py"), View())
    controller.run_game()