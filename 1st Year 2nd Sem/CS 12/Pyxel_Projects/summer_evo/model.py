import pyxel
from world import World
from constants import Color, Key_Input
# 9 by 16 grid
# 16 by 16 px tiles

class Model():
    def __init__(self, map_txt_path, screen_scale = 1):
        self._screen_scale = screen_scale
        self._screen_col_count = 16
        self._screen_row_count = 9
        self._cell_px_size = 16 # cell px sidelength from 16 by 16 px tiles
        self._screen_width = self.screen_scale * (self._screen_col_count * self.cell_px_size)
        self._screen_height = self.screen_scale * (self._screen_row_count * self.cell_px_size)
        self._world = World(self._screen_width, self._screen_height, map_txt_path)
        self._is_game_over = False
        self._map_txt_path = map_txt_path
        self._curr_key = Key_Input.NONE


    @property
    def screen_scale(self):
        return self._screen_scale
    
    @property
    def screen_col_count(self):
        return self._screen_col_count
    
    @property
    def screen_row_count(self):
        return self._screen_row_count
    
    @property
    def cell_px_size(self):
        return self._cell_px_size

    @property
    def screen_width(self):
        return self._screen_width

    @property
    def screen_height(self):
        return self._screen_height

    @property
    def is_game_over(self):
        return self._is_game_over

    @property
    def map_txt_path(self):
        return self._map_txt_path

    @property
    def world(self):
        return self._world
    
    @property
    def curr_key(self):
        return self._curr_key
    
    def set_key(self, key_input):
        self._curr_key = key_input

    def is_quit(self):
        if self._curr_key == Key_Input.QUIT:
            pyxel.quit()


    def move_player_dir(self):
        max_map_w = self._world.col_count * self._cell_px_size
        max_map_h = self._world.row_count * self._cell_px_size
        step = 5 * self._world.player.speed

        if self._curr_key in (Key_Input.GO_UP, Key_Input.GO_DOWN, Key_Input.GO_LEFT, Key_Input.GO_RIGHT):
            match self._curr_key:
                case Key_Input.GO_UP:
                    if (0 <= (self._world.player.y - step) <= max_map_h):
                        self._world.player.y -= step
                case Key_Input.GO_DOWN:
                    if (0 <= (self._world.player.y + step) <= max_map_h):
                        self._world.player.y += step
                case Key_Input.GO_LEFT:
                    if (0 <= (self._world.player.x - step) <= max_map_w):
                        self._world.player.x -= step
                case Key_Input.GO_RIGHT:
                    if (0 <= (self._world.player.x + step) <= max_map_w):
                        self._world.player.x += step
