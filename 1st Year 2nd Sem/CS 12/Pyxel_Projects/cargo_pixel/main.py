import pyxel
from controller import Controller
from model import Model
from view import View

if __name__ == "__main__":
    controller = Controller(Model(128, 72, "southeast map.png"), View())
    controller.run_game()