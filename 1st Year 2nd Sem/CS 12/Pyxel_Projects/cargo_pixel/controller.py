from model import Model
from view import View



class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view


    def update(self):
        model = self._model
        view = self._view
        ...

    def draw(self):
        model = self._model
        view = self._view
        ...

    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)