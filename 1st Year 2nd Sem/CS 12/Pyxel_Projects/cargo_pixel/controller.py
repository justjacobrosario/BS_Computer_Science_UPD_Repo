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

        model.upd_tick()
        model.upd_curr_keys(view.get_key_input())


        model.is_quit()
        model.move_player_dir()
        model.world.upd_ship_trail(model.tick)

    def draw(self):
        model = self._model
        view = self._view
        
        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_matrix, model.world.player.x, model.world.player.y)
        view.draw_ship_trail(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.movement_graphics.prev_locs,model.world.player.x, model.world.player.y)
        view.draw_player(model.screen_width, model.screen_height,  model.world.row_count, model.world.col_count, model.cell_px_size, model.curr_keys, model.world.player.ship)


    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)
