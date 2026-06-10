# common
import numpy as np
import pandas as pd
from sklearn import linear_model

# Libraries for retrieving data from the web and handling zip files
import requests, zipfile
from io import StringIO
import io


# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Load and clean the data
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])


def homework(anime_data_extracted, X_column, Y_column):
    X = anime_data_extracted[[X_column]]
    y = anime_data_extracted[Y_column]

    model = linear_model.LinearRegression()
    model.fit(X, y)
    result = model.score(X, y)
    return result

result = homework(anime_data_extracted, X_column='Members', Y_column='Completed')
print(result)








from __future__ import annotations
from enum import Enum, auto
from random import Random, choice, choices
import math
import pyxel
import json

from towers import Tower, BasicTower, SniperTower, SplitterTower, MedicTower
from enemies import Enemy, Color, EnemyType
from bullets import Bullet
from player import Dir

class Map:
    def __init__(self, width, height, data) -> None:
        # Locations and Dimensions
        self._width: int = width
        self._height: int = height
        self._dimensions = (15, 7)
        cols, rows  = self._dimensions
        self._cell_size = self._width // cols
        self._total_grid_height = rows * self._cell_size
        self.VERT_OFFSET = (self.height - self.total_grid_height) // 2
        paths_all_round, tunnel_all_round, guns_all_round = Map.parse_map_txt("path_maps.txt")
        self._all_paths = paths_all_round
        self._all_tunnel_paths = tunnel_all_round
        self._all_gun_coords = guns_all_round
        self._paths = paths_all_round.get(1, [])
        self._tunnel_paths = tunnel_all_round.get(1, [])
        self._gun_pixel_coords = (0, 0) # px coords of gun
        self._gun_coords = guns_all_round.get(1, (7, 4)) # grid coords of gun




        # Constants
        self._colors = [
            Color.Orange, Color.Red, Color.Blue, 
            Color.Green, Color.Pink, Color.DarkBlue
        ]
        self._choice_weights = [20 for _ in range(5)]

        # Map Status
        self._tick: int = 0
        self._rounds = 2
        self._tower_locs: list[Tower] = []
        self._displayed_enemies: list[Enemy] = []
        self._displayed_bullets = []
        self._current_round = 1
        self._waiting_for_start = True
        self._is_game_over = False
        self._enemies_per_round = data["enemies_per_round"]
        self._rounds = data["rounds"]
        self._regenerator_gain_hp: int = data["regenerator_gain_hp"]
        self._chameleon_freq_change: int = data["chameleon_freq_change"]
        self._enemies = [
            [choice(self.colors) for _ in range(self.enemies_per_round)] for _ in range(self._rounds)]
        self._enemy_types = [typ for typ in EnemyType]

        # Player Atrributes
        self._exp: int = 100 # ! Test value, should start with 0
        self._hp: int = 2
        self._max_hp: int = self.hp
        self._pending_bullets: Color = choice([Color.Orange, Color.Red, Color.Yellow])
        self._next_color = 7


    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    @property
    def dimensions(self) -> bool:
        return self._dimensions

    @property
    def cell_size(self):
        return self._cell_size

    @property
    def total_grid_height(self):
        return self._total_grid_height

    @property
    def paths(self) -> list[list[tuple[int, int]]]:
        return self._paths
    
    @property
    def path(self) -> list[tuple[int, int]]:
        return self._paths[0] # just return the first path
    

    @property
    def tick(self):
        return self._tick
    @tick.setter 
    def tick(self, val_input: int):
        self._tick = val_input
    
    @property
    def enemies(self):
        return self._enemies

    @property
    def regenerator_gain_hp(self):
        return self._regenerator_gain_hp
    
    @property
    def chameleon_freq_change(self):
        return self._chameleon_freq_change

    @property
    def enemies_per_round(self):
        return self._enemies_per_round
    
    @property
    def displayed_enemies(self):
        return self._displayed_enemies
    
    @property
    def enemy_types(self):
        return self._enemy_types
    
    @property
    def pending_bullets(self):
        return self._pending_bullets
    
    @property
    def displayed_bullets(self):
        return self._displayed_bullets

    @property 
    def towers_locs(self):
        return self._tower_locs

    @property
    def gun_coords(self):
        return self._gun_coords

    @property
    def transformed_gun_coords(self):
        return self._transformed_gun_coords

    @property
    def tunnel_paths(self):
        return self._tunnel_paths

    @property
    def tunnel_path(self):
        return self._tunnel_paths[0] # for now just return the first tunnel path

    @property
    def all_tunnel_cells(self): # for process_shot to check fi a cell is a tunnel
        all_tunnel_cells = set()
        for path in self._tunnel_paths:
            all_tunnel_cells.update(path)
        return all_tunnel_cells

    @property
    def current_round(self):
        return self._current_round
    
    @property
    def rounds(self):
        return self._rounds

    @property
    def colors(self):
        return self._colors
    
    @property
    def waiting_for_start(self):
        return self._waiting_for_start
    @waiting_for_start.setter
    def waiting_for_start(self, val_input: bool) -> None:
        self._waiting_for_start = val_input

    @property
    def is_game_over(self) -> bool:
        return self._is_game_over
    @is_game_over.setter 
    def is_game_over(self, val_input: bool) -> None:
        self._is_game_over = val_input

    @property
    def exp(self) -> int:
        return self._exp
    @exp.setter
    def exp(self, val_input: int) -> None:
        self._exp = val_input

    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, val_input: int) -> None:
        self._hp = val_input

    @property
    def next_color(self):
        return self._next_color

    @property
    def choice_weights(self):
        return self._choice_weights

    @staticmethod
    def parse_map_txt(filename):
        with open(filename, encoding='utf-8') as f:
            lines = f.read().splitlines()
        
        paths, tunnels, guns = {}, {}, {}
        current_round = None

        for line in lines:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            words = s.split()
            if words[0] == "round":
                current_round = int(words[1])
                if current_round not in paths:
                    paths[current_round] = []
                    tunnels[current_round] = []

            elif words[0] == "path":
                path_coords = [tuple(int(x) for x in t.split(",")) for t in words[1:]]
                paths[current_round].append(path_coords)
            elif words[0] == "tunnel":
                tunnel_coords = [tuple(int(x) for x in t.split(",")) for t in words[1:]]
                tunnels[current_round].append(tunnel_coords)
            elif words[0] == "gun" and current_round not in guns:
                guns[current_round] = (int(words[1]), int(words[2]))
        
        return paths, tunnels, guns

    def load_round_map(self, round_num):
        self._paths = self._all_paths.get(round_num, self._paths)
        self._tunnel_paths = self._all_tunnels.get(round_num, [])
        self._gun_coords = self._all_guns.get(round_num, self._gun_coords)



    def inc_tick(self):
        self._tick += 1

    def transform_gun_coords(self, gun_col: int, gun_row: int):
        x = gun_col * self.cell_size
        y = self.VERT_OFFSET + (gun_row * self.cell_size)

        tile_side = 16
        offset = (self.cell_size - tile_side) // 2

        x += offset
        y += offset

        self._transformed_gun_coords = (x, y)

    def check_if_next_round(self):
        if (len(self._enemies[self._current_round - 1]) == 0) and (len(self._displayed_enemies) == 0) and ((self._current_round) < self._rounds):
                self._current_round += 1
                self._waiting_for_start = True # pause between rounds
                self.load_round_map(self._current_round)

    def check_is_game_over(self):
        if self._hp <= 0:
            self._is_game_over = True

    def delete_enemy_out_of_bounds(self):
        self._displayed_enemies = [e for e in self._displayed_enemies if e.current_health > 0]
        self._displayed_bullets = [b for b in self._displayed_bullets if not b.is_used]
    
    # * Must check if a bug may occur in process_shot
    # Implement spatial hash
    def process_shot(self):
        """
        Checks the list of displayed bullets and displayed enemies if there exists
        a pair that intersects. If there is an intersection, it updates the attribute
        `is_used` of the bullet. And updates the `current_health` attribute of the enemy
        by decrementing it by 1. Finally, since it intersects it increases the `exp`
        attribute by 1.
        """
        if self._pending_bullets:
            self._next_color = self.pending_bullets.value
        else:
            self._next_color = Color.Black.value

        new_bullets = []

        for bullet in self._displayed_bullets:

            if bullet.is_used:
                continue

            # bullet radius in pixels
            r1 = bullet.radius

            for enemy in self._displayed_enemies:
                enemy_x = enemy.col * self.cell_size + (self.cell_size // 2)
                enemy_y = self.VERT_OFFSET + (enemy.row * self.cell_size) + (self.cell_size // 2)

                # enemy radius in pixels
                r2 = enemy.radius

                dist_sq = (bullet.x - enemy_x)**2 + (bullet.y - enemy_y)**2
                if dist_sq > ((r1 + r2)**2):
                    continue

                if bullet.color == enemy.color or bullet.color == Color.Black:
                    if bullet.color == enemy.color:
                        self._exp += 1
                    else:
                        self._exp -= 5

                    enemy.current_health -= 1
                    
                    if bullet.piercing_power > 1:
                        bullet._piercing_count += 1
                        if bullet.piercing_count >= bullet.piercing_power:
                            bullet.is_used = True
                    else:
                        bullet.is_used = True

                    if enemy.enemy_type is EnemyType.NINJA:
                        self._exp += 5
                    else:
                        self._exp += 1
                    bullet._piercing_count += 1

                    if bullet.piercing_count >= bullet.piercing_power:
                        bullet.is_used = True
                        break

                elif bullet.can_split and bullet.color != enemy.color:
                    bullet.can_split = False
                    bullet.is_used = True
                    speed = math.sqrt(bullet.vx**2 + bullet.vy**2)
                    base_angle = math.atan2(bullet.vy, bullet.vx)
                    angles = [-30, 0, 30] if bullet.is_upgraded else [-20, 20]
                    for deg in angles:
                        angle = base_angle + math.radians(deg)
                        new_bullet = Bullet(bullet.x, bullet.y)
                        new_bullet.color = choice(self.colors)
                        new_bullet.direction = Dir.CURSOR
                        new_bullet.vx = math.cos(angle) * speed
                        new_bullet.vy = math.sin(angle) * speed
                        new_bullet.radius = bullet.radius
                        new_bullets.append(new_bullet)

        self._displayed_bullets.extend(new_bullets)
        return False

    def display_next_enemy(self):
        if (self._tick%50 == 0) and (len(self._enemies[self._current_round - 1]) != 0):
            color = self._enemies[self._current_round - 1].pop()
            type = choices(
                self.enemy_types, 
                weights=self.choice_weights, 
                k=1
            )
            enemy = Enemy()
            enemy.color = color
            enemy.enemy_type = type[0]  # Since type returns list

            if enemy.enemy_type is EnemyType.BOMBER:
                enemy.color = Color.Black
            elif enemy.enemy_type is EnemyType.NINJA:
                enemy.walk_speed = 0.5

            enemy.path_idx = len(self._displayed_enemies) % len(self._paths) # assign path index
            self._displayed_enemies.append(enemy)

    def shoot(self, dir: Dir):
        direction_velocities = {
                                Dir.UP: (0, -14.4),
                                Dir.DOWN: (0, 14.4),
                                Dir.LEFT: (-14.4, 0),
                                Dir.RIGHT: (14.4, 0)
                                }
        if self._pending_bullets:
            color = self._pending_bullets
            self._pending_bullets = choice(self.colors)

            x_coord = self.transformed_gun_coords[0]
            y_coord = self.transformed_gun_coords[1]
            bullet_coords = (x_coord, y_coord)

            bullet = Bullet(x_coord, y_coord)
            bullet.color = color
            bullet.direction = dir
            bullet.radius = self.cell_size // bullet.radius

            if bullet.direction == Dir.CURSOR:
                mouse_coords = pyxel.mouse_x, pyxel.mouse_y
                vx, vy = self.calculate_velocity(bullet_coords, mouse_coords)
                bullet.vx = vx
                bullet.vy = vy
            else:
                bullet.vx, bullet.vy = direction_velocities[bullet.direction]                

            self._displayed_bullets.append(bullet)

    def calculate_velocity(self, pointA: tuple[float, float], 
                           pointB: tuple[float, float]) -> tuple[float, float]:
        x1, y1 = pointA
        x2, y2 = pointB
        dx: float = x2 - x1
        dy: float = y2 - y1
        norm = self.normalize(pointA, pointB)

        vx = dx/norm * 14.4
        vy = dy/norm * 14.4
        return vx, vy

    def normalize(self, pointA: tuple[float, float], 
                  pointB: tuple[float, float]) -> float:
        x1, y1 = pointA
        x2, y2 = pointB
        ans = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

        return ans

    def move_bullet(self):
        for bullet in self._displayed_bullets:
            if not bullet.is_used:
                match bullet.direction:
                    case Dir.UP:
                        bullet.y += bullet.vy
                        if bullet.y < 0:
                            bullet.is_used = True

                    case Dir.DOWN:
                        bullet.y += bullet.vy
                        if bullet.y > self.height:
                            bullet.is_used = True

                    case Dir.LEFT:
                        bullet.x += bullet.vx
                        if bullet.x < 0:
                            bullet.is_used = True
                            
                    case Dir.RIGHT:
                        bullet.x += bullet.vx
                        if bullet.x > self.width:
                            bullet.is_used = True

                    case Dir.CURSOR:
                        bullet.x += bullet.vx
                        bullet.y += bullet.vy
                        if bullet.x > self.width:
                            bullet.is_used = True
    def move_enemy(self, enemy: Enemy):
        path = self._paths[enemy.path_idx]

        enemy.progress += enemy.walk_speed 
        
        current_path_idx = int(enemy.progress)
        next_path_idx = current_path_idx + 1

        if next_path_idx >= len(path): # if nakalagpas na yung enemy, -1 hp
            if enemy.current_health > 0:
                if enemy.enemy_type is EnemyType.BOMBER:
                    enemy.current_health = 0
                enemy.current_health = 0
                #self._hp -= 1
            return

        # percent until next path (ex. from idx 0 to 1, 0.5 yung progress, so meaning halfway pa lang sya to the next)
        percent = enemy.progress - current_path_idx

        p1 = path[current_path_idx]
        p2 = path[next_path_idx]

        if enemy.enemy_type == EnemyType.REGENERATOR:
            if (int(enemy.progress) + 1) % self.regenerator_gain_hp == 0 and int(enemy.progress) != 0:
                if not enemy.gained_hp:
                    enemy.current_health += 1
                    enemy.gained_hp = True
            else:
                enemy.gained_hp = False

        elif enemy.enemy_type == EnemyType.CHAMELEON:
            if self.tick % self.chameleon_freq_change == 0:
                color = list({enemy.color} ^ set(self.colors))
                enemy.color = choice(color)

        # update row and col
        enemy.row = p1[0] + (p2[0] - p1[0]) * percent
        enemy.col = p1[1] + (p2[1] - p1[1]) * percent

    def place_tower(self, tower_class: type[Tower], col, row):
        # 
        if tower_class is None:
            return
        
        all_path_cells = {cell for path in self._paths for cell in path}

        if (row, col) in all_path_cells:
            # that location is the path
            return
        if any(tower.col == col and tower.row == row for tower in self._tower_locs):
            # tower already exists in that location
            return
        tower = tower_class(col, row)
        if self._exp >= tower.exp_cost:
            self._exp -= tower.exp_cost
            self._tower_locs.append(tower)

    def upgrade_tower(self, tower: Tower): # temp: until a phase 3 model is made since no tower upgrades in phase 2
        if self._exp >= tower._upgrade_cost and not tower.upgraded:
            self._exp -= tower._upgrade_cost
            tower.upgrade()

    def tick_towers(self):
        for tower in self._tower_locs:
            tower.fire_cooldown -= tower.fire_rate / 30 # 30 fps

            if tower.fire_cooldown <= 0:

                tower_x = (tower.col * self.cell_size) + (self.cell_size // 2)
                tower_y = self.VERT_OFFSET + (tower.row * self.cell_size) + (self.cell_size // 2)

                for color in tower.pick_bullet_color():
                    bullet = tower.create_bullet(tower_x, tower_y, color)
                    if bullet:
                        self._displayed_bullets.append(bullet)

                tower.fire_cooldown = 1.0  # reset to full interval