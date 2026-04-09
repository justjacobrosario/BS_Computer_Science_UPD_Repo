# pyright: strict
import argparse
import pyxel
from enum import Enum, auto

class Direction(Enum):
	L = auto()
	R = auto()
	U = auto()
	D = auto()

class Pacman:
	def __init__(self, x:int, y:int, r:int, col:int):
		self.x = x
		self.y = y
		self.r = r
		self.col = col
		self.dir: Direction = Direction.R

	def change_dir(self, d:Direction):
		self.dir = d

class Model:
	def __init__(self, screen_w:int, screen_h:int, pacman: Pacman):
		self.screen_w = screen_w
		self.screen_h = screen_h
		self.rows = 10
		self.cols = 10
		self.pacman = pacman
		self.move_mag = 10
		self.manhattan_const = 0

	def quit_func(self):
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()

	def move_func(self):
		if pyxel.btn(pyxel.KEY_A):
			self.pacman.change_dir(Direction.L)
		elif pyxel.btn(pyxel.KEY_D):
			self.pacman.change_dir(Direction.R)
		elif pyxel.btn(pyxel.KEY_W):
			self.pacman.change_dir(Direction.U)
		elif pyxel.btn(pyxel.KEY_S):
			self.pacman.change_dir(Direction.D)

	def move_pacman(self):

		'''match self.pacman.dir:
									case Direction.L:
										x -= m
									case Direction.R:
										x += m
									case Direction.U:
										y -= m
									case Direction.D:
										y += m'''
		if self.pacman.dir == Direction.L:
			self.pacman.x -= self.move_mag
		elif self.pacman.dir == Direction.R:
			self.pacman.x += self.move_mag
		elif self.pacman.dir == Direction.U:
			self.pacman.y -= self.move_mag
		elif self.pacman.dir == Direction.D:
			self.pacman.y += self.move_mag

	def upd_manhattan_const(self):
		self.manhattan_const += 0.1

		if self.manhattan_const > self.rows//2:
			self.manhattan_const = 0




class View():
	def make_board(self, w:int, h:int, rows:int, cols:int):
		for r in range(rows):
			for c in range(cols):
				if (r + c)%2 == 0:
					pyxel.rect(r*(w//rows), c*(h//cols), w//rows, h//cols, 9)
				else:
					pyxel.rect(r*(w//rows), c*(h//cols), w//rows, h//cols, 10)

	def manhattan_pulse(self, w:int, h:int, rows:int, cols:int, const:int):
		i = rows // 2
		j = cols // 2

		for r in range(rows):
			for c in range(cols):
				"""if abs(i - r) + abs(j - c) <= const:
																	pyxel.rect(r*(w//rows), c*(h//cols), w//rows, h//cols, 8)"""
				if ((i-r)**2 + (j-c)**2)**(1/2) <= const:
					pyxel.rect(r*(w//rows), c*(h//cols), w//rows, h//cols, 8)

	def draw_pacman(self, pacman:Pacman):
		pyxel.circ(pacman.x, pacman.y, pacman.r, pacman.col)


class Controller:
	def __init__(self, model: Model, view:View):
		self._model = model
		self._view = view


	def start(self):
		model = self._model
		view = self._view

		pyxel.init(model.screen_w, model.screen_h, "Checkers", 25)
		pyxel.fullscreen(True)
		pyxel.run(self.update, self.draw)

	def update(self):
		model = self._model
		view = self._view

		model.quit_func()
		model.move_func()
		model.move_pacman()

		model.upd_manhattan_const()

	def draw(self):
		model = self._model
		view = self._view

		view.make_board(model.screen_w, model.screen_h, model.rows, model.cols)
		view.manhattan_pulse(model.screen_w, model.screen_h, model.rows, model.cols, model.manhattan_const)
		view.draw_pacman(model.pacman)



if __name__ == "__main__":
	parse = argparse.ArgumentParser()

	parse.add_argument("--screen_width", "-W", required = True)
	parse.add_argument("--screen_height", "-H", required = True)
	
	args = parse.parse_args()

	_model = Model(int(args.screen_width), int(args.screen_height), Pacman(0, 0, 30, 10))
	_view  = View()
	_controller = Controller(_model, _view)

	_controller.start()
