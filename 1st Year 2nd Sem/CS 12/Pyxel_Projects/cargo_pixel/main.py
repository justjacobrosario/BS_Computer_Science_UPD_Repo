import pyxel
from controller import Controller
from model import Model
from view import View

if __name__ == "__main__":
    controller = Controller(Model(16, 9, scale = 7), View())
    controller.run_game()