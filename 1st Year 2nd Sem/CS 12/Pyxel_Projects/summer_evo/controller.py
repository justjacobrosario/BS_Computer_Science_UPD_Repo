from model import Model
from world import World
from view import View
import pyxel

class Controller():
    def __init__(self, model, view):
        self._model = model
        self._view = view
    
    def update(self):
        model = self._model
        view = self._view

        model.is_quit()

        model.set_key(view.get_key_input())
        model.move_player_dir()

    def draw(self):
        model = self._model
        view = self._view


        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_coords_dict, model.world.player.x, model.world.player.y)
        view.draw_player(model.screen_width, model.screen_height, model.cell_px_size)
        
        view.draw_plants(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.plants_generator.plants_list, model.world.player.x, model.world.player.y)

    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)