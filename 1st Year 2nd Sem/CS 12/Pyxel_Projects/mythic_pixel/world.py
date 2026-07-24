

from player import Player
from constants import FPS
from random import sample, choice, randint

from stages import Stage, Grasslands
import map_data

class MovementGraphics:
    def __init__(self):
        self._prev_locs = []

    @property
    def prev_locs(self):
        return self._prev_locs
    

    def add_prev_locs(self, coord):
        x, y = coord
        self._prev_locs.append((x, y))

    def del_oldest_locs(self, count):
        for _ in range(count):
            self._prev_locs.pop(0)

        

class World:
    def __init__(self, screen_width, screen_height, cell_px_size):

        # MAP PROPERTIES
        self._cell_px_size = cell_px_size
        
        try:
            self._player_spawn_x, self._player_spawn_y = map_data.PLAYER_PX_SPAWNPOINT
            self._map_matrix = map_data.MAP_DATA
        except AttributeError: # if map not loaded yet
            self._player_spawn_x, self._player_spawn_y = (cell_px_size, cell_px_size)
            self._map_matrix = [[0, 0], [0, 0]]
        self._row_count = len(self._map_matrix)
        self._col_count = len(self._map_matrix[0]) if self._row_count else 0
    
        # PLAYER PROPERTIES
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._player = Player(self._player_spawn_x, self._player_spawn_y, 0)
        
        # MOVEMENT GRAPHICS PROPERTIES
        self._movement_graphics = MovementGraphics()
        self._movement_graphics.add_prev_locs((self._player.x, self._player.y))


    @property
    def col_count(self):
        return self._col_count

    @property
    def row_count(self):
        return self._row_count

    @property
    def map_matrix(self):
        return self._map_matrix
    

    @property
    def screen_width(self):
        return self._screen_width
    
    @property
    def screen_height(self):
        return self._screen_height

    @property
    def movement_graphics(self):
        return self._movement_graphics
    
    @property
    def player(self):
        return self._player

    def upd_stage(self, stage_type : Stage):
        stage_type.generate_map()
        self._player_spawn_x, self._player_spawn_y = map_data.PLAYER_PX_SPAWNPOINT
        self._map_matrix = map_data.MAP_DATA