
import pyxel
from constants import Key_Input, Tile, ToolType, TOOL_COSTS, FPS
from world import World

MIN_ZOOM = 0.4
MAX_ZOOM = 3.0
ZOOM_STEP = 0.25


class Model:
    def __init__(self, screen_col_count, screen_row_count, map_info, mode_config, scale = 1):
        self._cell_px_size = 8
        self._scale = scale
        self._screen_width = self._cell_px_size * screen_col_count * self._scale
        self._screen_height = self._cell_px_size * screen_row_count * self._scale
        self._screen_col_count, self._screen_row_count = (screen_col_count, screen_row_count)
        self._curr_keys = set({Key_Input.NONE})

        map_module = map_info.load_data()
        self._world = World(self._screen_width, self._screen_height, self._cell_px_size, map_module)
        self._camera_x, self._camera_y = self._world.spawn_x, self._world.spawn_y

        self._mode_config = mode_config
        self._money = mode_config.starting_money
        self._day = 1
        self._day_tick = 0
        self._game_over = False

        self._tick = 0
        self._zoom = 1.0

    @property
    def zoom(self):
        return self._zoom

    @property
    def camera_x(self):
        return self._camera_x

    @property
    def camera_y(self):
        return self._camera_y

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





    @property
    def money(self):
        return self._money

    @property
    def day(self):
        return self._day

    @property
    def is_night(self):
        return self._day_tick >= self._mode_config.day_phase_sec * FPS

    @property
    def is_game_over(self):
        return self._game_over
    

        
    def upd_tick(self):
        self._tick += 1


    def upd_curr_keys(self, key_inputs):
        self._curr_keys = key_inputs

    def is_quit(self):
        if Key_Input.QUIT in self._curr_keys:
            pyxel.quit()


    def pan_camera(self, dx, dy):
        max_map_w = self._world.col_count * self._cell_px_size
        max_map_h = self._world.row_count * self._cell_px_size

        new_x = self._camera_x + (dx / self._zoom)
        new_y = self._camera_y + (dy / self._zoom)

        self._camera_x = max(0, min(new_x, max_map_w))
        self._camera_y = max(0, min(new_y, max_map_h))

    def change_scale(self):
        if Key_Input.ZOOM_IN in self._curr_keys:
            self._zoom = min(self._zoom + ZOOM_STEP, MAX_ZOOM)
        
        elif Key_Input.ZOOM_OUT in self._curr_keys:
            self._zoom = max(self._zoom - ZOOM_STEP, MIN_ZOOM)


    def upd_day_cycle(self):
        if self._game_over:
            return
        self._day_tick += 1
        if self._day_tick >= self._mode_config.day_length_sec * FPS:
            self._day_tick = 0
            self._day += 1
            self._money += self._mode_config.money_per_day
            max_days = self._mode_config.max_days
            if max_days is not None and self._day > max_days:
                self._game_over = True

    def buy_tool(self, tool_type: ToolType) -> bool:
        cost = TOOL_COSTS[tool_type]
        if self._money < cost:
            return False
        self._money -= cost
        return True
    