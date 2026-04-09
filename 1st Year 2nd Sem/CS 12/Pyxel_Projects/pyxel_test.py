import pyxel
from random import randint


class Ball:
	def __init__(self, x:int, y:int, r:int, col:int):
		self._x = x
		self._y = y
		self._r = r
		self._col = col
		self._going_down = True
		self._going_right = True

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def r(self):
		return self._r

	@property
	def col(self):
		return self._col

	@property
	def going_down(self):
		return self._going_down

	@property
	def going_right(self):
		return self._going_right

	def swap_grav(self):
		if self._going_down:
			self._going_down = False
		else:
			self._going_down = True

	def swap_x_prop(self):
		if self._going_right:
			self._going_right = False
		else:
			self._going_right = True

	def upd_x(self, magnitude:int):
		self._x += magnitude

	def upd_y(self, magnitude:int):
		self._y += magnitude


class PyxelModel:
	def __init__(self, screen_w:int, screen_h:int):
		self._screen_w = screen_w
		self._screen_h = screen_h
		self._grav_constant = 10
		self._rightward_constant = 10

		# add objects here

		self._ball_list: list[Ball] = []

	@property
	def screen_w(self):
		return self._screen_w

	@property
	def screen_h(self):
		return self._screen_h

	@property
	def ball_list(self):
		return self._ball_list
	

	def quit_func(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def add_ball_func(self):
		if pyxel.btnp(pyxel.KEY_B):
			self._ball_list.append(Ball(x = randint(0, self._screen_w - 200), y = randint(0, self._screen_h - 50), r = 40, col = randint(1, 15)))

	def classic_phys(self):
		if self._ball_list:
			for ball in self._ball_list:
				if ball.going_down:
					ball.upd_y(self._grav_constant)
				if not ball.going_down:
					ball.upd_y(-self._grav_constant)
				if ball.going_right:
					ball.upd_x(self._rightward_constant)
				if not ball.going_right:
					ball.upd_x(-self._rightward_constant)

	def border_collision(self):
		if self._ball_list:
			for ball in self._ball_list:
				if ball.x + ball.r + 200 >= self.screen_w or ball.x - ball.r - 200 <= 0:
					ball.swap_x_prop()
				if ball.y + ball.r + 50 >= self.screen_h or ball.y - ball.r - 50 <= 0:
					ball.swap_grav()


class PyxelView:
	def clear_screen(self):
		pyxel.cls()

	def draw_text(self, x:int, y:int, text:str, col:int):
		pyxel.text(x, y, text, col)

	def draw_balls(self, balls:list[Ball]):
		for ball in balls:
			pyxel.circb(ball.x, ball.y, ball.r, ball.col)


class PyxelController:
	def __init__(self, model:Model, view:View, screen_w:int, screen_h:int):
		self._model = model
		self._view = view
		self._screen_h = screen_h
		self._screen_w = screen_w

	def run(self):
		model = self._model
		view = self._view

		pyxel.init(self._screen_w, self._screen_h, title = "try pyxel", fps = 50)
		pyxel.run(self.update, self.draw)

	def update(self):
		model = self._model
		view = self._view

		model.quit_func()
		model.add_ball_func()

		model.border_collision()
		model.classic_phys()

	def draw(self):
		view = self._view
		model = self._model

		#view.draw_text(model.screen_w//2, model.screen_h//2, "eyy", 11)
		view.draw_balls(model.ball_list)


# instantiation

screen_h = 1080
screen_w = 1980
model = PyxelModel(screen_w, screen_h)
view = PyxelView()
controller = PyxelController(model, view, screen_w, screen_h)

controller.run()