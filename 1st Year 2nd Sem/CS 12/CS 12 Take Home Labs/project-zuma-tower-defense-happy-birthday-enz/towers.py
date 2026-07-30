from abc import ABC, abstractmethod
from enum import Enum, auto
from bullets import Bullet
from enemies import Color
from player import Dir
import random

class TowerType(Enum):
    BASIC = auto()
    SNIPER = auto()
    SPLITTER = auto()
    MEDIC = auto()

class Tower(ABC):
    _tower_type: TowerType
    _exp_cost: int = 0
    _upgrade_cost: int = 0
    _bullet_colors: list[Color] = []

    def __init__(self, pos_col, pos_row):
        self._fire_rate: float = 0.5 # bullets / second
        self._fire_cooldown: float = 0.0 # time since last shot

        self._col: float = float(pos_col) # defined per instance
        self._row: float = float(pos_row) # defined per instance

        self._upgraded: bool = False
        self._direction: Dir = Dir.UP
	
    @property
    def tower_type(self) -> TowerType:
        return self._tower_type

    @property
    def col(self) -> float: # req for pos drawing
        return self._col
    
    @property
    def row(self) -> float: # req for pos drawing
        return self._row
    
    @property
    def fire_rate(self) -> float: # req for shooting cooldown
        return self._fire_rate

    @property
    def fire_cooldown(self) -> float: # req for shooting cooldown
        return self._fire_cooldown
    
    @fire_cooldown.setter
    def fire_cooldown(self, value: float):
        self._fire_cooldown = value
    
    @property
    def exp_cost(self) -> int: # req for placing
        return self._exp_cost
    
    @property
    def upgraded(self) -> bool: # req for upgrading and drawing
        return self._upgraded
    
    @property
    def direction(self) -> Dir:
        return self._direction
    
    @direction.setter
    def direction(self, value: Dir):
        self._direction = value
    
    # --

    def pick_bullet_color(self) -> list[Color]:
        return [random.choice(self._bullet_colors)]
    
    def on_upgrade(self):
        pass

    def create_bullet(self, x, y, color) -> Bullet | None:
        bullet = Bullet(x, y)
        bullet.color = color
        bullet.radius = 18
        bullet.direction = self.direction
        self._apply_velocity(bullet)
        return bullet
    
    def _apply_velocity(self, bullet: Bullet, speed: float = 14.4):
        match self.direction:
            case Dir.UP:
                bullet.vx = 0
                bullet.vy = -speed
            case Dir.DOWN:
                bullet.vx = 0
                bullet.vy = speed
            case Dir.LEFT:
                bullet.vx = -speed  
                bullet.vy = 0
            case Dir.RIGHT:
                bullet.vx = speed
                bullet.vy = 0
    
    def upgrade(self):
        if not self._upgraded:
            self._upgraded = True
            self.on_upgrade()
            return True
        return False

# phase 2 tower: piercd 1, cost 5 (+1 bullet on upgrade)
class BasicTower(Tower): 
    _exp_cost = 5
    _upgrade_cost = 5
    _bullet_colors = [Color.Orange, Color.Red, Color.Blue]
    _tower_type = TowerType.BASIC

    def __init__(self, pos_col, pos_row):
        super().__init__(pos_col, pos_row)

    def pick_bullet_color(self) -> list[Color]:
        if self._upgraded:
            return random.sample(self._bullet_colors, 2)  # 2 bullets only when upgraded
        return [random.choice(self._bullet_colors)]

class SniperTower(Tower):
    _exp_cost = 7
    _upgrade_cost = 7
    _bullet_colors = [Color.Orange, Color.Red, Color.Blue]
    _tower_type = TowerType.SNIPER

    def __init__(self, pos_col, pos_row):
        super().__init__(pos_col, pos_row)
        self._fire_rate = 0.2

    def create_bullet(self, x: float, y: float, color: Color) -> Bullet:
        bullet = super().create_bullet(x, y, color)
        bullet.piercing_power = 5 if self._upgraded else 3
        return bullet

class SplitterTower(Tower):
    _exp_cost = 10
    _upgrade_cost = 10
    _bullet_colors = [Color.Orange, Color.Red, Color.Blue]
    _tower_type = TowerType.SPLITTER

    def __init__(self, pos_col, pos_row):
        super().__init__(pos_col, pos_row)
        self._fire_rate = 0.2

    def create_bullet(self, x: float, y: float, color: Color) -> Bullet:
        bullet = super().create_bullet(x, y, color)
        bullet.can_split = True
        bullet.is_upgraded = self._upgraded
        return bullet

class MedicTower(Tower):
    _exp_cost = 12
    _upgrade_cost = 12
    _bullet_colors = [] # doesn't shoot
    _tower_type = TowerType.MEDIC

    def __init__(self, pos_col, pos_row):
        super().__init__(pos_col, pos_row)
        self._fire_rate = 0.0 # doesn't shoot
        self._heal_amount = 1

    @property
    def heal_amount(self):
        return self._heal_amount

    def on_upgrade(self):
        self._heal_amount = 2

    def pick_bullet_color(self) -> list[Color]:
        return [] # doesn't shoot
    
    def create_bullet(self, x, y, color) -> Bullet:
        return None # doesn't shoot