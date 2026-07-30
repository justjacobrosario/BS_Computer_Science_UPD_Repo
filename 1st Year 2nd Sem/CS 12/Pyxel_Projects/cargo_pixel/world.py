

from player import Player
from ports import RedPort, OrangePort, YellowPort, GreenPort, BluePort
from constants import Tile, Cargo, PORT_GEN_INTERVAL_SEC, FPS
from random import sample, choice, randint
import map_data

PORT_CLASSES = [RedPort, OrangePort, YellowPort, GreenPort, BluePort]
MIN_PORT_SPACING = 5

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
        self._port_gen_ticks_left = PORT_GEN_INTERVAL_SEC * FPS
    
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
    
    @property
    def ports(self):
        return self._ports

    def upd_ship_trail(self, tick, max_trail=30):
        self._movement_graphics.add_prev_locs((self._player.x, self._player.y))
            
        while len(self._movement_graphics._prev_locs) > max_trail:
            self._movement_graphics.del_oldest_locs(1)
        
    def _find_port_location(self, attempts=200):
        for _ in range(attempts):
            row = randint(0, self._row_count - 1)
            col = randint(0, self._col_count - 1)

            # tile must be grass and has adjacent ocean or sea tile for the ship to dock
            if self._map_matrix[row][col] == Tile.GRASS.value: 
                if any(0 <= row + dr < self._row_count and 0 <= col + dc < self._col_count and self._map_matrix[row + dr][col + dc] in (Tile.OCEAN.value, Tile.SEA.value) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    if all(abs(p.x - col) > MIN_PORT_SPACING or abs(p.y - row) > MIN_PORT_SPACING for p in self._ports):
                        return col, row
        return None
    
    def _gen_new_port(self):
        location = self._find_port_location()
        if location is None:
            return
        col, row = location
        port_cls = choice(PORT_CLASSES)
        self._ports.append(port_cls(col, row))
    
    def upd_port_generation(self):
        self._port_gen_ticks_left -= 1
        if self._port_gen_ticks_left <= 0:
            self._gen_new_port()
            self._port_gen_ticks_left = PORT_GEN_INTERVAL_SEC * FPS


    def upd_cargo_generation(self):
        for port in self._ports:
            port.upd_cargo_timer()
        


    def upd_timers(self):
        self.upd_port_generation()
        self.upd_cargo_generation()

    def process_player_port_collision(self):
        player_tile_x = self._player.x // self._cell_px_size
        player_tile_y = self._player.y // self._cell_px_size

        for port in self._ports:
            dx = abs(port.x - player_tile_x)
            dy = abs(port.y - player_tile_y)
            if (dx == 0 and dy == 0) or (dx + dy == 1):  # Player is on the same tile or adjacent tile):
                while self._player.total_cargo < self._player.max_cargo and port.cargos_to_ship:
                    if self._player._cargo_priority is not None and self._player._cargo_priority in port.cargos_to_ship:
                        self._player.curr_cargo[self._player._cargo_priority] += 1
                        port.remove_cargo(self._player._cargo_priority)
                    else:
                        cargo = port.cargos_to_ship[0]
                        self._player.curr_cargo[cargo] += 1
                        port.remove_cargo(cargo)
        return None
    
