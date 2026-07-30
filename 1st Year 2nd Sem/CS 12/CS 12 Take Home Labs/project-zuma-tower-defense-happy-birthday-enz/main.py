from model import (Model)
from player import Dir
from view import View
from controller import Controller
import pyxel

if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model, view) 
    
    controller.start_game()