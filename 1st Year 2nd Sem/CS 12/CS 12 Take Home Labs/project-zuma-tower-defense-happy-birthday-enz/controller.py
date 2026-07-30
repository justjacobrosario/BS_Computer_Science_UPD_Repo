from model import Model
from player import Dir
from dataclasses import dataclass
from towers import Tower, BasicTower, SniperTower, SplitterTower, MedicTower
from view import View
from leaderboard import save_score
from enum import Enum, auto
import pyxel
import sounds

from towers import Tower, BasicTower, SniperTower, SplitterTower, MedicTower
from view import View
from PyxelMenu.pyxel_menu import PyxelMenu


AVAILABLE_TOWERS = [BasicTower, SniperTower, SplitterTower, MedicTower]
class GameState(Enum):
    PLAYING = auto()
    NAME_INPUT = auto()
    LEADERBOARD = auto()
    END_SCREEN = auto()


@dataclass
class PlacementState:
    selected_tower: type[Tower] | None = None
    def select(self, tower_class):
        if self.selected_tower == tower_class:
            self.selected_tower = None
        else:
            self.selected_tower = tower_class

    def reset(self):
        self.selected_tower = None

class Window(Enum):
    MAIN_MENU = auto()
    CAMPAIGN = auto()
    ENDLESS = auto()
    LEADERBOARD = auto()

class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view
        self._tower_placement = PlacementState()

        self._menu = PyxelMenu(100, 100, ["Campaign", "Endless", "Leaderboard"])
        self._current = Window.MAIN_MENU
        self._option = ''
        self._tab: Window = Window.MAIN_MENU

        self._game_state: GameState = GameState.PLAYING
        self._name_buffer: str = ""
        self._last_name: str = "" # leaderboard highlight
        self._last_round: int = 0 # leaderboard highlight


    def update(self):
        model = self._model
        game_map = model.map
        view = self._view

        # Quits if 'q' is pressed
        model.will_quit()

        if self._game_state == GameState.END_SCREEN:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self._game_state = GameState.NAME_INPUT
                self._name_buffer = ""
            elif pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        if self._game_state == GameState.NAME_INPUT:
            self._name_buffer, confirmed = view.handle_name_input(self._name_buffer)
            if confirmed:
                self._last_name = self._name_buffer or "Anonymous"
                self._last_round = game_map.current_round - 1
                save_score(self._last_name, self._last_round)
                self._game_state = GameState.LEADERBOARD
            return

        if self._game_state == GameState.LEADERBOARD:
            if view.is_leaderboard_replay_pressed():
                self._model.map.__init__() # reset map
                self._tower_placement.reset()
                self._name_buffer = ""
                self._game_state = GameState.PLAYING
            return

        # Turns music on or off if "m" is pressed
        view.switch_music()

        match self._tab:
            case Window.MAIN_MENU:
                menu = self._menu
                if pyxel.btnp(pyxel.KEY_UP):
                    menu.move_up()
                elif pyxel.btnp(pyxel.KEY_DOWN):
                    menu.move_down()
                else:
                    pass

                if pyxel.btnp(pyxel.KEY_RETURN):
                    string_to_window = {"Campaign": Window.CAMPAIGN, "Endless": Window.ENDLESS, "Leaderboard": Window.LEADERBOARD}
                    self._option = menu.get_current_pos()
                    self._tab = string_to_window[menu.get_current_text()]
                    model.reset_map("settings.json")
                    pyxel.run(self.update, self.draw_campaign)
            case Window.CAMPAIGN:
                if game_map.waiting_for_start:
                    game_map.transform_gun_coords(*game_map.gun_coords)
                    if view.is_start_pressed(game_map.width, game_map.height):
                        model.start_round()
                        self._tower_placement.reset()
                        return
                    clicked_tower = view.get_tower_selection(game_map.width, game_map.height, AVAILABLE_TOWERS, game_map.cell_size)
                    if clicked_tower:
                        self._tower_placement.select(clicked_tower)
                    else:
                        cell = view.get_clicked_cell(game_map.height, game_map.total_grid_height, game_map.cell_size)
                        if cell:
                            col, row = cell

                            if pyxel.btn(pyxel.KEY_SHIFT):
                                tower = next((t for t in game_map.towers_locs if t.col == col and t.row == row), None)
                                if tower:
                                    game_map.upgrade_tower(tower)
                            elif self._tower_placement.selected_tower:
                                game_map.place_tower(self._tower_placement.selected_tower, col, row)
                                self._tower_placement.reset()
                    return # freezes rendering of enemies/bullets
                else:
                    if not game_map.is_game_over:
                        game_map.inc_tick()
                        game_map.move_bullet()
                        game_map.tick_towers()
                        is_shot = game_map.process_shot()
                        if is_shot:
                            sounds.shot_enemy_sound()

                        for enemy in list(game_map.displayed_enemies):
                            game_map.move_enemy(enemy)

                        game_map.display_next_enemy()
                        wasd_val = view.is_gun_wasd_clicked()

                        if wasd_val is not None:
                            vert_offset = (game_map.height - game_map.total_grid_height) // 2
                            hovered_col = pyxel.mouse_x // game_map.cell_size
                            hovered_row = (pyxel.mouse_y - vert_offset) // game_map.cell_size
                            hovered_tower = next((t for t in game_map.towers_locs if t.col == hovered_col and t.row == hovered_row), None)

                            if hovered_tower and pyxel.btn(pyxel.KEY_SHIFT):
                                if wasd_val != Dir.CURSOR: # guard check to prevent setting tower dir to cursor
                                    hovered_tower.direction = wasd_val
                            else:
                                sounds.shoot_sound()
                                game_map.shoot(wasd_val)
                    else:
                        self._tab = Window.MAIN_MENU
                        self._game_state = GameState.NAME_INPUT
                        self._name_buffer = ""
                        pyxel.run(self.update, self.draw_menu)


                    game_map.delete_enemy_out_of_bounds()
                    game_map.check_if_next_round()
                    game_map.check_is_game_over()
            case Window.ENDLESS:
                if game_map.waiting_for_start:
                    game_map.transform_gun_coords(*game_map.gun_coords)
                    if view.is_start_pressed(game_map.width, game_map.height):
                        model.start_round()
                        self._tower_placement.reset()
                        return
                    clicked_tower = view.get_tower_selection(game_map.width, game_map.height, AVAILABLE_TOWERS, game_map.cell_size)
                    if clicked_tower:
                        self._tower_placement.select(clicked_tower)
                    else:
                        cell = view.get_clicked_cell(game_map.height, game_map.total_grid_height, game_map.cell_size)
                        if cell:
                            col, row = cell

                            if pyxel.btn(pyxel.KEY_SHIFT):
                                tower = next((t for t in game_map.towers_locs if t.col == col and t.row == row), None)
                                if tower:
                                    game_map.upgrade_tower(tower)
                            elif self._tower_placement.selected_tower:
                                game_map.place_tower(self._tower_placement.selected_tower, col, row)
                                self._tower_placement.reset()
                    return # freezes rendering of enemies/bullets
                else:
                    if not game_map.is_game_over:
                        game_map.inc_tick()
                        game_map.move_bullet()
                        game_map.tick_towers()

                        is_shot = game_map.process_shot()
                        if is_shot:
                            sounds.shot_enemy_sound()

                        for enemy in list(game_map.displayed_enemies):
                            game_map.move_enemy(enemy)

                        game_map.display_next_enemy()
                        wasd_val = view.is_gun_wasd_clicked()

                        if wasd_val is not None:
                            vert_offset = (game_map.height - game_map.total_grid_height) // 2
                            hovered_col = pyxel.mouse_x // game_map.cell_size
                            hovered_row = (pyxel.mouse_y - vert_offset) // game_map.cell_size
                            hovered_tower = next((t for t in game_map.towers_locs if t.col == hovered_col and t.row == hovered_row), None)

                            if hovered_tower and pyxel.btn(pyxel.KEY_SHIFT):
                                if wasd_val != Dir.CURSOR: # guard check to prevent setting tower dir to cursor
                                    hovered_tower.direction = wasd_val
                            else:
                                sounds.shoot_sound()
                                game_map.shoot(wasd_val)
                    else:
                        self._tab = Window.MAIN_MENU
                        self._game_state = GameState.NAME_INPUT
                        self._name_buffer = ""
                        pyxel.run(self.update, self.draw_menu)

                    game_map.delete_enemy_out_of_bounds()
                    game_map.check_if_next_round()
                    model.endless_modifier()
                    game_map.check_is_game_over()
            case Window.LEADERBOARD:
                ...

    def draw(self):
        model = self._model
        game_map = model.map
        view = self._view

        view.reset_screen()
        self.draw_menu()
   
    def start_game(self):
        model = self._model
        view = self._view

        view.start_game(model.map.width, model.map.height)
        pyxel.run(self.update, self.draw_menu)

    def draw_campaign(self):
        model = self._model
        game_map = model.map
        view = self._view

        view.reset_screen()

        if self._game_state == GameState.END_SCREEN:
            won = (game_map.current_round == game_map.rounds) and (len(game_map.displayed_enemies) == 0) and (len(game_map.enemies[game_map.current_round - 1])) == 0
            view.display_end_screen(game_map.width, game_map.height, won, "UbuntuMono-Regular.ttf", 30)
            return

        if self._game_state == GameState.NAME_INPUT:
            view.display_name_input(game_map.width, game_map.height, self._name_buffer, "UbuntuMono-Regular.ttf", 25)
            return
        
        if self._game_state == GameState.LEADERBOARD:
            view.display_leaderboard(game_map.width, game_map.height, self._last_name, self._last_round, "UbuntuMono-Regular.ttf", 25)
            return

        view.display_map(
            game_map.VERT_OFFSET, 
            game_map.dimensions[1], 
            game_map.dimensions[0], 
            game_map.cell_size)
        
        view.draw_tilemap(game_map.height, game_map.total_grid_height, game_map.dimensions[1], game_map.dimensions[0], game_map.cell_size, game_map.paths)
        view.display_border_panels(game_map.height, game_map.total_grid_height)

        view.display_enemies(
            game_map.VERT_OFFSET, 
            game_map.dimensions[1], 
            game_map.dimensions[0], 
            game_map.cell_size,
            game_map.displayed_enemies)
        
        view.display_shield_tiles(game_map.VERT_OFFSET, game_map.cell_size, game_map.tunnel_paths)

        view.display_gun(
            game_map.transformed_gun_coords[0],
            game_map.transformed_gun_coords[1],
            game_map.cell_size
        )

        view.display_placed_towers(
            game_map.height, 
            game_map.total_grid_height, 
            game_map.cell_size, 
            game_map.towers_locs)

        view.display_bullets(
            game_map.VERT_OFFSET, 
            game_map.dimensions[1], 
            game_map.dimensions[0], 
            game_map.cell_size, 
            game_map.displayed_bullets)


        view.display_stats_text(
            game_map.current_round, 
            game_map.rounds, 
            game_map.hp, 
            game_map.exp, 
            "UbuntuMono-Regular.ttf", 
            25)
        
        view.display_keybinds_text(game_map.height, "UbuntuMono-Regular.ttf", 15)
        

        if game_map.waiting_for_start:
            view.display_start_button(game_map.width, game_map.height, game_map.current_round, "UbuntuMono-Regular.ttf", 17)
            view.display_tower_selection(game_map.width, game_map.height, AVAILABLE_TOWERS, self._tower_placement.selected_tower, game_map.cell_size, "UbuntuMono-Regular.ttf", 20)
        # temp until model implemented
        # view.display_tower_selection(model.width, model.height, AVAILABLE_TOWERS, model.selected_tower, model.cell_size)

        if game_map.is_game_over:
            won = (game_map.current_round == game_map.rounds) and len(game_map.displayed_enemies) == 0 and len(game_map.enemies[game_map.current_round - 1]) == 0
            view.display_end_screen(game_map.width, game_map.height, won, "UbuntuMono-Regular.ttf", 30)

        view.display_cursor(game_map.next_color)
    def draw_menu(self):
        model = self._model
        game_map = model.map
        view = self._view
        menu = self._menu

        view.reset_screen()
        menu.draw()