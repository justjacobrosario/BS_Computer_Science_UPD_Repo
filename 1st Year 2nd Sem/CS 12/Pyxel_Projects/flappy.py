import pyxel
from random import randint, choice
from typing import Protocol
from time import sleep
		

class Pipe:
	def __init__(self, x:int, y:int, w:int, h:int, col:int):
		self._x = x
		self._y = y
		self._col = col
		self._w = w
		self._h = h

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def w(self):
		return self._w

	@property
	def h(self):
		return self._h

	@property
	def col(self):
		return self._col

	def upd_x(self, magnitude:int):
		self._x += magnitude

class Bird:
	def __init__(self, x:int, y:int, r:int, col:int):
		self._x = x
		self._y = y
		self._r = r
		self._col = col
		self._downward = True
		self._rightward = True

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
	def downward(self):
		return self._downward

	@property
	def rightward(self):
		return self._rightward

	def swap_y(self):
		if self._downward:
			self._downward = False
		else:
			self._downward = True

	def swap_x(self):
		if self._rightward:
			self._rightward = False
		else:
			self._rightward = True

	def upd_x(self, magnitude:int):
		self._x += magnitude

	def upd_y(self, magnitude:int):
		self._y += magnitude


class FlappyModel:
	def __init__(self, screen_w:int, screen_h:int):
		self._screen_w = screen_w
		self._screen_h = screen_h
		self._bird:Bird = Bird(self._screen_w//2, self._screen_h//2, 10, 10)
		self._grav:int = 10
		self._pipespeed:int = 10
		self._max_tightness:int = 5
		self._pipe_width:int = 50
		self._score:int = 0
		self._quit: bool = False
		self._collides:bool = False

	## instantiate obj here
		self._pipelist: list[list[Pipe]] = []

	@property
	def collides(self):
		return self._collides

	@property
	def quit(self):
		return self._quit
	@property
	def screen_w(self):
		return self._screen_w
	
	@property
	def screen_h(self):
		return self._screen_h

	@property
	def bird(self):
		return self._bird

	@property
	def pipelist(self):
		return self._pipelist

	@property
	def score(self):
		return self._score

	def game_over(self):
		return self._collides

	def classic_grav(self):
		self._bird.upd_y(self._grav)

	def restart_func(self):
		if self._collides and pyxel.btnp(pyxel.KEY_R):
			self._bird = Bird(self._screen_w//2, self._screen_h//2, 10, 10)
			self._pipelist = []
			self._score = 0
			self._collides = False

	def full_screen_func(self):
		if pyxel.frame_count == 0:
			pyxel.fullscreen(True)

	def flap(self):
		if pyxel.btn(pyxel.KEY_SPACE):
			if self._bird.y - self._bird.r > 0:
				self._bird.upd_y(-30)

		if self._bird.y + self._bird.r > self._screen_h:
			self._bird.upd_y(-10)


	def will_quit(self):
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()

	def move_pipes(self):
		for pipe_column in self.pipelist:
			for pipe in pipe_column:
				pipe.upd_x(-self._pipespeed)

	def make_single_pipe(self):
		is_lower_pipe = choice([True, False])

		if is_lower_pipe:
			x:int = self._screen_w
			y:int = randint(2*(self._bird.r) + self._max_tightness, self._screen_h)
			w:int = self._pipe_width
			h:int = self._screen_h - y
			pipe:Pipe = Pipe(x, y, w, h, 3)

		else:
			x:int = self._screen_w
			y:int = 0
			w:int = self._pipe_width
			h:int = randint(0, self._screen_h - (2*(self._bird.r) + self._max_tightness))
			pipe:Pipe = Pipe(x, y, w, h, 11)

		self._pipelist.append([pipe])

	def next_pipe(self, frame_count:int):
		if frame_count == 0:
			return True
		else:
			ans:bool = False
			for pipe_column in self._pipelist:
				pipe:Pipe = pipe_column[0]
				if pipe.x + self._pipe_width <= 0:
					self._pipelist.pop()
					self._score += 1
					ans = True
					return ans
			return ans

	def check_collision(self):
		if self._pipelist:
			bx1 = (self._bird.x - self._bird.r)
			by1 = (self._bird.y - self._bird.r)
			bx2 = (self._bird.x + self._bird.r)
			by2 = (self._bird.y + self._bird.r)

			p = self._pipelist[-1][0]
			px1 = p.x
			py1 = p.y
			px2 = p.x + p.w
			py2 = p.y + p.h

			self._collides = not(
				bx2 < px1 or
				bx1 > px2 or 
				by2 < py1 or
				by1 > py2)




class FlappyView:
	def clear_s(self, col:int):
		pyxel.cls(col)

	def draw_bird(self, b:Bird):
		pyxel.circ(b.x, b.y, b.r, b.col)

	def draw_pipes(self, pipelist:list[list[Pipe]]):
		if pipelist:
			for pipe_column in pipelist:
				for pipe in pipe_column:
					pyxel.rect(pipe.x, pipe.y, pipe.w, pipe.h, pipe.col)

	def draw_score(self, score:int, x:int, y:int):
		pyxel.text(x, y, str(score), 7)

	def draw_gameover(self, x:int, y:int):
		pyxel.text(x, y, "GAME OVER!", 7)



class FlappyController:
	def __init__(self, model:FlappyModel, view:FlappyView):
		self._model = model
		self._view = view

	def run(self):
		model = self._model
		view = self._view

		pyxel.init(model.screen_w, model.screen_h, "FlappyBurd", 100)
		pyxel.run(self.update, self.draw)

	def update(self):
		model = self._model

		model.will_quit()
		model.full_screen_func()
		model.restart_func()

		if not model.game_over():
			model.flap()
			model.classic_grav()

			model.move_pipes()

		    # FIX
		if not model.pipelist:
			model.make_single_pipe()

		elif model.next_pipe(pyxel.frame_count):
			model.make_single_pipe()

		model.check_collision()


	def draw(self):
		model = self._model
		view = self._view

		if not model.game_over():
			view.clear_s(1)
			view.draw_bird(model.bird)

			view.draw_pipes(model.pipelist)

			view.draw_score(model.score, model.screen_w//2, model.screen_h//2 - 20)

		else:
			view.clear_s(8)
			view.draw_score(model.score, model.screen_w//2, model.screen_h//2 - 20)
			view.draw_gameover(model.screen_w//2 - 17, model.screen_h//2)


# Instantiation phase
screen_w:int = 384
screen_h:int = 216

model = FlappyModel(screen_w, screen_h)
view = FlappyView()
controller = FlappyController(model, view)

controller.run()

