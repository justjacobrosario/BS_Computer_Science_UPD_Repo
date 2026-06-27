from constants import Key_Input
from world import World



class Model:
    def __init__(self, screen_width, screen_height, map_path):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._cell_px_size = 8
        self._screen_col_count, self._screen_row_count = (16, 9)
        self._map_path = map_path
        self._curr_key = Key_Input.NONE
        self._world = World(self._screen_width, self._screen_height, map_path)

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
    def curr_key(self):
        return self._curr_key
    

    @property
    def map_path(self):
        return self._map_path

    def upd_curr_key(self, key_input):
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
    