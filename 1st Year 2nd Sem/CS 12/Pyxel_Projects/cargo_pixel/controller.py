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
        model.change_scale()


        model.is_quit()
        model.move_player_dir()
        model.world.upd_ship_trail(model.tick)
        model.world.upd_timers()
        model.world.player.upd_total_cargo()
        model.world.process_player_port_collision()

    def draw(self):
        model = self._model
        view = self._view
        
        view.draw_grid_map(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.map_matrix, model.world.player.x, model.world.player.y, model.zoom)
        view.draw_ports(model.screen_width, model.screen_height, model.world.ports, model.cell_px_size, model.world.player.x, model.world.player.y,model.zoom)
        view.draw_ship_trail(model.screen_width, model.screen_height, model.world.row_count, model.world.col_count, model.cell_px_size, model.world.movement_graphics.prev_locs,model.world.player.x, model.world.player.y, model.zoom)
        view.draw_player(model.screen_width, model.screen_height,  model.world.row_count, model.world.col_count, model.cell_px_size, model.curr_keys, model.world.player.ship, model.zoom)
        view.draw_ship_hud(model.screen_width, model.screen_height, model.world.player.curr_cargo, model.world.player.total_cargo, model.world.player.max_cargo)

    def run_game(self):
        model = self._model
        view = self._view

        view.start(model.screen_width, model.screen_height)
        pyxel.run(self.update, self.draw)
