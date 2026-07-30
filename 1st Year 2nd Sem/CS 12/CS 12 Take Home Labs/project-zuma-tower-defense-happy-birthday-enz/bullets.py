from enemies import Color
from player import Dir

class Bullet:
	def __init__(self, x: float, y: float):
		self._x: float = x
		self._y: float = y
		self._radius = 5
		self._color = Color.Orange
		self._is_used: bool = False
		self._direction: Dir = Dir.UP
		self._vx: float = 0
		self._vy: float = 0

		self._piercing_power: int = 1
		self._piercing_count: int = 0
		self._can_split: bool = False
		self._is_upgraded: bool = False

	@property
	def x(self) -> float:
		return self._x

	@property
	def y(self) -> float:
		return self._y
	
	@property
	def vx(self) -> float:
		return self._vx
	
	@property
	def vy(self) -> float:
		return self._vy

	@property
	def radius(self):
		return self._radius

	@property
	def is_used(self):
		return self._is_used

	@property
	def color(self):
		return self._color

	@property
	def direction(self):
		return self._direction
	
	@property
	def piercing_power(self):
		return self._piercing_power
	
	@property
	def piercing_count(self):
		return self._piercing_count
	
	@property
	def can_split(self):
		return self._can_split
	
	@property
	def is_upgraded(self):
		return self._is_upgraded

	@x.setter
	def x(self, value):
		self._x = value

	@y.setter
	def y(self, value):
		self._y = value

	@vx.setter
	def vx(self, value):
		self._vx = value

	@vy.setter
	def vy(self, value):
		self._vy = value

	@color.setter
	def color(self, value):
		self._color = value

	@radius.setter
	def radius(self, value):
		self._radius = value

	@is_used.setter
	def is_used(self, value):
		self._is_used = value

	@direction.setter
	def direction(self, value):
		self._direction = value

	@piercing_power.setter
	def piercing_power(self, value):
		self._piercing_power = value

	@piercing_count.setter
	def piercing_count(self, value):	
		self._piercing_count = value

	@can_split.setter
	def can_split(self, value):
		self._can_split = value

	@is_upgraded.setter
	def is_upgraded(self, value):
		self._is_upgraded = value

'''

class PiercingBullet(Bullet): # sniper tower bullet that pierces 3 (5 if upgraded)
	def __init__(self, x: float, y: float):
		super().__init__(x, y)
		self._piercing_power = 3
		self._is_upgraded = False # determined if tower who fired is upgraded or not

	@property
	def piercing_power(self):
		return self._piercing_power

	@piercing_power.setter
	def piercing_power(self, value):
		self._piercing_power = value
		
	@property
	def is_upgraded(self):
		return self._is_upgraded

	@is_upgraded.setter
	def is_upgraded(self, value):
		self._is_upgraded = value

class SplitterBullet(Bullet): # splitter tower bullet that splits into 2 (3) when hitting wrong enemy
    def __init__(self, x, y):
        super().__init__(x, y)
        self._has_split = False # only allows split once
        self._is_upgraded = False # determined if tower who fired is upgraded or not

    @property
    def has_split(self):
        return self._has_split

    @has_split.setter
    def has_split(self, value):
        self._has_split = value

    @property
    def is_upgraded(self):
        return self._is_upgraded
	
    @is_upgraded.setter
    def is_upgraded(self, value):
        self._is_upgraded = value

'''