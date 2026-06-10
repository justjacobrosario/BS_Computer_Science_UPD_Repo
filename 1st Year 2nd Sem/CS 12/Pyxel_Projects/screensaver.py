import pyxel
from random import randint


#from model import model
#from view import view

#objects

class Bird:
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.going_right = True
		self.dropping = True



class Model:
	def __init__(self, screen_w, screen_h):
		self._screen_w = screen_w
		self._screen_h = screen_h
		self.bird = Bird(screen_w//2, screen_h//2, 100, 8)
		self.bird2 = Bird(screen_w//2 + randint(-500, 500), screen_h//2 + randint(-500, 500), 100, 9)
		self.bird3 = Bird(screen_w//2 - randint(-500, 500), screen_h//2 - randint(-500, 500), 100, 10)
		self.bird4 = Bird(screen_w//2 - randint(-500, 500), screen_h//2 - randint(-500, 500), 100, 3)
		self.bird5 = Bird(screen_w//2 - randint(-500, 500), screen_h//2 - randint(-500, 500), 100, 1)
		self.bird6 = Bird(screen_w//2 - randint(-500, 500), screen_h//2 - randint(-500, 500), 100, 2)

	@property
	def screen_w(self):
		return self._screen_w

	@property
	def screen_h(self):
		return self._screen_h

	def gravity(self, bird):
		bird.y += 15

	def anti_gravity(self, bird):
		bird.y -= 15

	def flap(self, bird, strength = 100):
		bird.y -= strength

	def fly_r(self, bird):
		bird.x += 15

	def fly_l(self, bird):
		bird.x -= 15

	def dvd(self, bird: Bird):
		if bird.going_right:
			self.fly_r(bird)
		if not bird.going_right:
			self.fly_l(bird)
		if bird.dropping:
			self.gravity(bird)
		if not bird.dropping:
			self.anti_gravity(bird)

		if bird.x + 200 >= self.screen_w:
			bird.going_right = False
		if bird.x - 200 <= 0:
			bird.going_right = True
		if bird.y + 110 >= self.screen_h:
			bird.dropping = False
		if bird.y - 110 <= 0:
			bird.dropping = True


	


class View:
	def draw_bird(self, x, y, r, c):
		pyxel.circ(x, y, r, c)


class Controller:
	def __init__(self, model: model, view: view):
		self._model = model
		self._view = view

	def start_game(self):
		model = self._model
		view = self._view

		pyxel.init(model.screen_w, model.screen_h, title = "flappy", fps = 200)
		pyxel.run(self.update, self.draw)

	def update(self):
		model = self._model
		view = self._view

		if pyxel.btnp(pyxel.KEY_Q):   # press Q to quit
			pyxel.quit()

		if pyxel.btn(pyxel.KEY_F):
			model.flap(model.bird, strength = randint(20, 200))
			model.flap(model.bird2, strength = randint(20, 200))
			model.flap(model.bird3, strength = randint(20, 200))
			model.flap(model.bird4, strength = randint(20, 200))
			model.flap(model.bird5, strength = randint(20, 200))
			model.flap(model.bird6, strength = randint(20, 200))

		model.dvd(model.bird)
		model.dvd(model.bird2)
		model.dvd(model.bird3)
		model.dvd(model.bird4)
		model.dvd(model.bird5)
		model.dvd(model.bird6)



	def draw(self):
		model = self._model
		view = self._view

		pyxel.cls(0)
		view.draw_bird(model.bird.x, model.bird.y, model.bird.radius, model.bird.color)
		view.draw_bird(model.bird2.x, model.bird2.y, model.bird2.radius, model.bird2.color)
		view.draw_bird(model.bird3.x, model.bird3.y, model.bird3.radius, model.bird3.color)
		view.draw_bird(model.bird4.x, model.bird4.y, model.bird4.radius, model.bird4.color)
		view.draw_bird(model.bird5.x, model.bird5.y, model.bird5.radius, model.bird5.color)
		view.draw_bird(model.bird6.x, model.bird6.y, model.bird6.radius, model.bird6.color)



# Instantiate

screen_w = 1920
screen_h = 1080

_model = Model(screen_w, screen_h)
_view = View()
_controller = Controller(_model, _view)
_controller.start_game()