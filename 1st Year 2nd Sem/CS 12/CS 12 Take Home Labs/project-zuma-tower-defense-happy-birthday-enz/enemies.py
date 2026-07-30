from typing import Protocol
from enum import Enum, auto

class Color(Enum):
	Black = 0
	DarkBlue = 1
	DarkPurple = 2
	DarkGreen = 3
	Brown = 4
	DarkGray = 5
	LightGray = 6
	White = 7
	Red = 8
	Orange = 9
	Yellow = 10
	Green = 11
	Blue = 12
	Indigo = 13
	Pink = 14
	Peach = 15


class EnemyType(Enum):
	NORMAL = auto()
	REGENERATOR = auto()
	CHAMELEON = auto()
	BOMBER = auto()
	NINJA = auto()


class Enemy():
	"""
	Base enemy
	Position is tracked in grid space (col, row)
	Coordinates are floats so movement will be smooth
	Radius in pixels, usually used for collision detected
	`progress` check move_enemy() in model.py for explanation
	`next_idx` tracks which path indx to go next
	`path_idx` tracks which path to follow
	"""
	def __init__(self):
		self._path_idx = 0
		self._walk_speed = 0.1
		self._color = Color.Orange
		self._base_health = 1
		self._current_health = 1
		self._enemy_type = EnemyType.NORMAL
		self._col = 0
		self._row = 0
		self._radius = 15 # pixel radius, for collision detection
		self._next_idx = 1 # what ith path coord to go next
		self._progress = 0 # basically like ith current/previous passed path coord, then yung decimals indicates the progress towards the next path coord
		self._gained_hp = False

	@property
	def path_idx(self):
		return self._path_idx

	@property
	def walk_speed(self):
		return self._walk_speed
	
	@property
	def color(self):
		return self._color
	
	@property
	def base_health(self):
		return self._base_health
	
	@property
	def current_health(self):
		return self._current_health

	@property
	def col(self):
		return self._col

	@property
	def row(self):
		return self._row

	@property
	def next_idx(self):
		return self._next_idx
	
	@property
	def progress(self):
		return self._progress

	@property
	def radius(self):
		return self._radius
	
	@property
	def enemy_type(self):
		return self._enemy_type
	
	@property
	def gained_hp(self):
		return self._gained_hp
	
	@property
	def walk_speed(self):
		return self._walk_speed
	
	@walk_speed.setter
	def walk_speed(self, value):
		self._walk_speed = value

	@path_idx.setter
	def path_idx(self, value):
		self._path_idx = value

	@col.setter
	def col(self, value):
		self._col = value

	@row.setter
	def row(self, value):
		self._row = value

	@radius.setter
	def radius(self, value):
		self._radius = value

	@color.setter
	def color(self, value):
		self._color = value

	@progress.setter
	def progress(self, value):
		self._progress = value

	@current_health.setter
	def current_health(self, value):
		self._current_health = value

	@enemy_type.setter 
	def enemy_type(self, value):
		self._enemy_type = value

	@gained_hp.setter
	def gained_hp(self, value):
		self._gained_hp = value

	def update(self, tick: int) -> None:
		pass
