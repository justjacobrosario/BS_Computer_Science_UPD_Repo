from PIL import Image
import map_data
from player import Player
import importlib
from constants import Tile
from random import sample


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
        
        self._player_spawn_x, self._player_spawn_y = map_data.PLAYER_PX_SPAWNPOINT
        self._map_matrix = map_data.MAP_DATA
        self._row_count = len(self._map_matrix)
        self._col_count = len(self._map_matrix[0]) if self._row_count else 0
        
        # PORT PROPERTIES
        self._ports = []
        self._chosen_cargo = []
        self._next_cargos = []
        self._port_to_go = ()




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
    def player(self):
        return self._player
    

    @property
    def screen_width(self):
        return self._screen_width
    
    @property
    def screen_height(self):
        return self._screen_height

    @property
    def movement_graphics(self):
        return self._movement_graphics
    
    

    def upd_ship_trail(self, tick, max_trail=30):
        self._movement_graphics.add_prev_locs((self._player.x, self._player.y))
            
        while len(self._movement_graphics._prev_locs) > max_trail:
            self._movement_graphics.del_oldest_locs(1)
        
    
    def gen_random_cargo_routes(self, count = 5):
        for _ in range(count):
            chosen = sample(self._ports, k=2)
            if chosen not in self._next_cargos:
                self._next_cargos.append(chosen)

    def choose_cargo(self, chosen):
        if chosen in self._next_cargos:
            self._chosen_cargo = chosen
            self._next_cargos.remove(chosen)

    def upd_port_to_go(self):
        if self._chosen_cargo:
            if len(self._chosen_cargo) == 2: # go to the initial 
                self._port_to_go = self._chosen_cargo.pop(0)
            else:
                port_x, port_y = self._port_to_go
                if (port_x <= self._player.x <= port_x + self._cell_px_size) and (port_y <= self._player.y <= port_y + self._cell_px_size): # port collision mechanics
                    self._port_to_go = self._chosen_cargo.pop()

    def route_done(self):
        if len(self._chosen_cargo) == 0: # implies the coord in self._port_to_go is the terminal port to complete a route
            port_x, port_y = self._port_to_go
            if (port_x <= self._player.x <= port_x + self._cell_px_size) and (port_y <= self._player.y <= port_y + self._cell_px_size): # port collision mechanics
                self._player.exp += 1


