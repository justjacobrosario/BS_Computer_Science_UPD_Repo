import pyxel

from model import Model
from view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view

    def start_game(self):
        self.__view.start_game(self, self)

    def update(self):
        self.__model.update(pyxel.btnp(pyxel.KEY_SPACE))

    def draw(self):
        # bird
        # pipes
        # score

        self.__view.reset_screen()

        self.__view.draw_bird(self.__model.bird)
        self.__view.draw_pipes(self.__model.pipes)
        self.__view.draw_score(self.__model.score)
