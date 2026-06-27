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

        model.upd_curr_key(view.get_key_input())


        model.is_quit()
        model.move_player_dir()

    def draw(self):
        model = self._model
        view = self._view
        
        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_matrix, model.world.player.x, model.world.player.y)
        


    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)