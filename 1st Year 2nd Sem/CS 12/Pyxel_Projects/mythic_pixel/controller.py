import pyxel
from model import Model
from view import View



class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view


    def update(self):
        model = self._model
        view = self._view
        key_inputs = view.get_key_input()
        
        model.upd_cursor_coord(key_inputs, view.get_cursor_coords()) 
        model.upd_ingame_runtimes(key_inputs)
        

    def draw(self):
        model = self._model
        view = self._view

        
        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_matrix, model.world.player.x, model.world.player.y, model.zoom)
        view.draw_player(model.screen_width, model.screen_height,  model.world.row_count, model.world.col_count, model.cell_px_size, model.curr_keys, model.zoom)

        view.draw_menu(model.screen_width, model.screen_height, model.stage_access, model.curs_x, model.curs_y, model.is_left_clicked)
                


    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)
