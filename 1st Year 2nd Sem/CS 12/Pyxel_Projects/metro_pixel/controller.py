import pyxel
from model import Model
from view import View



class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._prev_mouse_x, self._prev_mouse_y = None, None



    def update(self):
        model = self._model
        view = self._view

        model.upd_tick()
        model.upd_curr_keys(view.get_key_input())
        model.change_scale()
        model.is_quit()
        model.upd_day_cycle()

        is_dragging, mouse_x, mouse_y = view.get_mouse_state()
        if is_dragging:
            if self._prev_mouse_x is not None:
                dx = self._prev_mouse_x - mouse_x
                dy = self._prev_mouse_y - mouse_y
                model.pan_camera(dx, dy)
            self._prev_mouse_x, self._prev_mouse_y = mouse_x, mouse_y
        else:
            self._prev_mouse_x, self._prev_mouse_y = None, None
        
    def draw(self):
        model = self._model
        view = self._view
        
        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_matrix, model.camera_x, model.camera_y, model.zoom)
        
    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)
