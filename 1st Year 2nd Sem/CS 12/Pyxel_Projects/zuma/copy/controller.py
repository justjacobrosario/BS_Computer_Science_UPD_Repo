from model import Phase1Model
from view import View
import pyxel


class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def update(self):
        model = self._model
        view = self._view

        model.will_quit()

        if not self._model.is_game_over:

            model.inc_tick()
            model.move_bullet()
            model.process_shot()


            for enemy in list(model.displayed_enemies):
                
                model.move_enemy(enemy)
            model.display_next_enemy()

            

            if view.is_gun_clicked():
                model.shoot()

    def draw(self):
        model = self._model
        view = self._view

        view.reset_screen()
        view.display_map(model.height, model.total_grid_height, model.dimensions[1], model.dimensions[0], model.grid_size)
        view.display_path(model.height, model.total_grid_height, model.dimensions[1], model.dimensions[0], model.grid_size, model.path)
        view.display_enemies(model.height, model.total_grid_height, model.dimensions[1], model.dimensions[0], model.grid_size, model.displayed_enemies)
        view.display_bullets(model.height, model.total_grid_height, model.dimensions[1], model.dimensions[0], model.grid_size, model.displayed_bullets)

    def start_game(self):
        model = self._model
        view = self._view

        view.start_game(model.width, model.height)
        pyxel.run(self.update, self.draw)
