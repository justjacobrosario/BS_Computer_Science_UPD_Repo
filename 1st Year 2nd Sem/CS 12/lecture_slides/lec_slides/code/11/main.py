from __future__ import annotations
import pyxel


FPS = 30
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
RADIUS = 20

class Model:
    def __init__(self, x: float, y: float, score: int):
        self._x = x
        self._y = y
        self._score = score
        self._tick = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def score(self):
        return self._score

    def press_up(self):
        self._y -= 2

    def press_down(self):
        self._y += 2

    def press_left(self):
        self._x -= 2

    def press_right(self):
        self._x += 2

    def tick(self):
        self._tick += 1

        if self._tick % FPS == 0:
            if self.x + RADIUS < 0 or self.x - RADIUS >= SCREEN_WIDTH or \
                self.y + RADIUS < 0 or self.y - RADIUS >= SCREEN_HEIGHT:
                self._score += 1

    @classmethod
    def default(cls, width: float, height: float):
        return Model(width / 2, height / 2, 0)


class View:
    def start(self, controller: Controller):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS)
        pyxel.run(controller.update, controller.draw)

    def draw(self, x: float, y: float, score: int):
        pyxel.cls(4)
        pyxel.circ(x, y, RADIUS, 1)
        pyxel.text(SCREEN_WIDTH / 2, 20, str(score), 1)

    def is_up_pressed(self):
        return pyxel.btn(pyxel.KEY_UP)

    def is_down_pressed(self):
        return pyxel.btn(pyxel.KEY_DOWN)

    def is_left_pressed(self):
        return pyxel.btn(pyxel.KEY_LEFT)

    def is_right_pressed(self):
        return pyxel.btn(pyxel.KEY_RIGHT)


class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def update(self):
        model = self._model

        if self._view.is_up_pressed():
            model.press_up()

        if self._view.is_down_pressed():
            model.press_down()

        if self._view.is_left_pressed():
            model.press_left()

        if self._view.is_right_pressed():
            model.press_right()

        model.tick()

    def draw(self):
        model = self._model

        self._view.draw(model.x, model.y, model.score)

    def start(self):
        self._view.start(self)


model = Model.default(SCREEN_WIDTH, SCREEN_HEIGHT)
view = View()
controller = Controller(model, view)

controller.start()
