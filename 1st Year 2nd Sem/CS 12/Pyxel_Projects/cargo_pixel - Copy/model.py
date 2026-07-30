
import pyxel
from constants import Key_Input, Tile
from world import World




class Model:
    def __init__(self, screen_col_count, screen_row_count, scale = 1):
        self._cell_px_size = 8
        self._screen_width = self._cell_px_size * screen_col_count * scale
        self._screen_height = self._cell_px_size * screen_row_count * scale
        self._screen_col_count, self._screen_row_count = (screen_col_count, screen_col_count)
        self._curr_keys = set({Key_Input.NONE})
        self._world = World(self._screen_width, self._screen_height, self._cell_px_size)
        self._tick = 0

    @property
    def screen_width(self):
        return self._screen_width

    @property
    def screen_height(self):
        return self._screen_height

    @property
    def cell_px_size(self):
        return self._cell_px_size

    @property
    def screen_col_count(self):
        return self._screen_col_count

    @property
    def screen_row_count(self):
        return self._screen_row_count
    
    @property
    def curr_keys(self):
        return self._curr_keys


    @property
    def world(self):
        return self._world


    @property
    def tick(self):
        return self._tick
        
    def upd_tick(self):
        self._tick += 1


    def upd_curr_keys(self, key_inputs):
        self._curr_keys = key_inputs

    def is_quit(self):
        if Key_Input.QUIT in self._curr_keys:
            pyxel.quit()


    
    def move_player_dir(self):
        max_map_w = self._world.col_count * self._cell_px_size
        max_map_h = self._world.row_count * self._cell_px_size
        step = 1 * self._world.player.speed

        if Key_Input.GO_UP in self._curr_keys:
            if (0 <= (self._world.player.y - step) <= max_map_h):

                next_block = self._world.map_matrix[(self._world.player.y - step)//self._cell_px_size][self._world.player.x//self._cell_px_size]
                if next_block == Tile.OCEAN.value:
                    self._world.player.y -= step
                elif next_block == Tile.SEA.value:
                    self._world.player.y -= (step * 2)

        if Key_Input.GO_DOWN in self._curr_keys:
            if (0 <= (self._world.player.y + step) <= max_map_h):

                next_block = self._world.map_matrix[(self._world.player.y + step)//self._cell_px_size][self._world.player.x//self._cell_px_size]
                if next_block == Tile.OCEAN.value:
                    self._world.player.y += step
                elif next_block == Tile.SEA.value:
                    self._world.player.y += (step * 2)

        if Key_Input.GO_LEFT in self._curr_keys:
            if (0 <= (self._world.player.x - step) <= max_map_w):

                next_block = self._world.map_matrix[(self._world.player.y)//self._cell_px_size][(self._world.player.x - step)//self._cell_px_size]
                if next_block == Tile.OCEAN.value:
                    self._world.player.x -= step
                elif next_block == Tile.SEA.value:
                    self._world.player.x -= (step * 2)

        if Key_Input.GO_RIGHT in self._curr_keys:
            if (0 <= (self._world.player.x + step) <= max_map_w):

                next_block = self._world.map_matrix[(self._world.player.y)//self._cell_px_size][(self._world.player.x + step)//self._cell_px_size]
                if next_block == Tile.OCEAN.value:
                    self._world.player.x += step
                elif next_block == Tile.SEA.value:
                    self._world.player.x += (step * 2)



    