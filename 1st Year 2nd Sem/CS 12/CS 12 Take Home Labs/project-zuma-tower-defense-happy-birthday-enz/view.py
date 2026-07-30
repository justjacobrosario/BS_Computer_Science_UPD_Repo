from collections.abc import Sequence
from typing import List, Protocol
import pyxel
from random import randint
from enum import Enum

from enemies import Color, Enemy
from bullets import Bullet
from towers import Tower, TowerType
from player import Dir
import sounds

class View:
    def __init__(self) -> None:
        ...
        
    def start_game(self, width, height) -> None:
        pyxel.init(width, height, title="zuma", fps=30)
        pyxel.mouse(False)
        pyxel.load("tilemap_sprites.pyxres")
        sounds.play_menu_music()

    def switch_music(self):
        if pyxel.btnp(pyxel.KEY_M):
            if pyxel.play_pos(0) is not None:  # if music is currently playing
                sounds.stop_music()
            else:
                sounds.play_music()
    
    def display_map(self, vert_offset, row_count, col_count, cell_size):
        for r in range(row_count):
            for c in range(col_count):
                # grid coor to pixel
                x = c * cell_size
                y = vert_offset + (r * cell_size)
                
                color = 10 if (r + c) % 2 == 0 else 11
                pyxel.rect(x, y, cell_size, cell_size, color)


    def display_enemies(self, vert_offset, row_count, 
                        col_count, cell_size, enemies: list[Enemy]):
        if enemies:
            for enemy in enemies:
                if enemy.current_health > 0:
                    x = enemy.col * cell_size
                    y = vert_offset + (enemy.row * cell_size)

                    mid_x = x + (cell_size//2)
                    mid_y = y + (cell_size//2)
                    pyxel.circ(mid_x, mid_y, cell_size // 3, enemy.color.value)

    def is_left_clicked(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return Dir.UP
        return None
    
    def cursor_coords(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x, y = pyxel.mouse_x, pyxel.mouse_y
            return x, y

    def is_gun_wasd_clicked(self):
        if pyxel.btnp(pyxel.KEY_W):
            return Dir.UP
        elif pyxel.btnp(pyxel.KEY_S):
            return Dir.DOWN
        elif pyxel.btnp(pyxel.KEY_A):
            return Dir.LEFT
        elif pyxel.btnp(pyxel.KEY_D):
            return Dir.RIGHT
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return Dir.CURSOR
        
        return None
    
    def display_bullets(self, vert_offset, row_count, col_count, 
                        cell_size, bullets: list[Bullet]):
        for bullet in bullets:
            if not bullet.is_used:
                pyxel.circ(bullet.x, bullet.y, bullet.radius, bullet.color.value)

    def display_gun(self, x, y, cell_size):
        tile_side = 16
        scale = cell_size // tile_side + 1 

        u, v = 48, 32  # gun sprite coords

        pyxel.blt(x, y, 0, u, v, tile_side, tile_side, scale=scale, colkey=1)

    def display_stats_text(self, current_round, rounds, hp, exp, font_addrss, size):
        font = pyxel.Font(font_addrss, size)

        pyxel.rect(40, 15, 520, 40, 0) # background for text
        pyxel.text(50, 20, f"ROUND: {current_round}/{rounds}", 7, font)
        pyxel.text(250, 20, f"Health: {hp}", 7, font)
        pyxel.text(450, 20, f"EXP: {exp}", 7, font)

    def display_keybinds_text(self, height, font_addrss, size):
        font = pyxel.Font(font_addrss, size)

        y = height - 90

        pyxel.rect(10, y - 10, 200, 90, 0) # background for text

        pyxel.text(20, y, "KEYBINDS:", 7, font)
        pyxel.text(20, y + 15, "SPACE: Start Round", 7, font)
        pyxel.text(20, y + 30, "M: Toggle Music", 7, font)
        pyxel.text(20, y + 45, "WASD or Click: Move Gun", 7, font)
        pyxel.text(20, y + 60, "Q: Quit Game", 7, font)

    def display_start_button(self, width, height, current_round, font_addrss, size):
        btn_w, btn_h = 150, 50
        x = width - btn_w - 25
        y = height - btn_h - 40

        font = pyxel.Font(font_addrss, size)

        pyxel.rect(x, y, btn_w, btn_h, 0)
        pyxel.text(x + 10, y + 11, f"PRESS SPACE TO", 7, font)
        pyxel.text(x + 10, y + 25, f"START ROUND {current_round}", 7, font)

    def display_tower_selection(self, width, height, tower_options: List[type[Tower]], selected_tower, cell_size, font_addrss, size):
        btn_size = cell_size
        padding = 30
        total_width = len(tower_options) * (btn_size + padding)
        start_x = (width - total_width) // 2  # center buttons horizontally
        btn_y = height - btn_size - padding   # anchor to bottom

        tile_side = 16
        scale = cell_size // tile_side
        offset = (cell_size - tile_side) // 2

        font = pyxel.Font(font_addrss, size)

        for i, tower_class in enumerate(tower_options):
            btn_x = start_x + i * (btn_size + padding)
            
            if tower_class == selected_tower: # highlight selected tower
                border_color = 7
                back_color = 12
            else:
                border_color = 10
                back_color = 8


            pyxel.rect(btn_x, btn_y, btn_size, btn_size, border_color) 

            #pyxel.rect(btn_x + 2, btn_y + 2, btn_size - 4, btn_size - 4, back_color)
            pyxel.blt(btn_x + offset, btn_y + offset, 0, 16 * i, 96, tile_side, tile_side, scale=scale) # tower sprite coords

            pyxel.text(btn_x + 7, btn_y + 6, tower_class.__name__[:5], 7, font) # tower name
            pyxel.text(btn_x + 7, btn_y + 25, f"{tower_class._exp_cost} EXP", 10, font) # tower cost

    def get_tower_selection(self, width, height, tower_options: List[type[Tower]], cell_size):
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return None
        
        btn_size = cell_size
        padding = 30
        total_width = len(tower_options) * (btn_size + padding)
        start_x = (width - total_width) // 2  # center buttons horizontally
        btn_y = height - btn_size - padding   # anchor to bottom

        for i, tower_class in enumerate(tower_options):
            btn_x = start_x + i * (btn_size + padding)
            if (btn_x <= pyxel.mouse_x <= btn_x + btn_size) and (btn_y <= pyxel.mouse_y <= btn_y + btn_size):
                return tower_class # this tower was clicked

    def display_placed_towers(self, height, total_grid_height, cell_size, towers: list[Tower]):
        vert_offset = (height - total_grid_height) // 2

        tile_side = 16
        scale = cell_size // tile_side
        sprite_offset = 25 # to make sprites centered


        for tower in towers:
            x = int(tower.col * cell_size)
            y = vert_offset + int(tower.row * cell_size)

            mid_x = x + (cell_size//2) - 1
            mid_y = y + (cell_size//2) - 1

            if tower.upgraded:
                pyxel.circ(mid_x, mid_y, cell_size // 2 - 2, 10)
                pyxel.circ(mid_x, mid_y, cell_size // 2 - 7, 3)
                pyxel.circ(mid_x, mid_y, cell_size // 2 - 14, 10)
            

            match tower.tower_type:
                case TowerType.BASIC:
                    u, v = 48, 48  # gun sprite coords
                    pyxel.blt(x + sprite_offset, y + sprite_offset, 0, u, v, tile_side, tile_side, scale=scale, colkey=1)
                    
                case TowerType.SNIPER:
                    u, v = 16, 64  # sniper sprite coords
                    pyxel.blt(x + sprite_offset, y + sprite_offset, 0, u, v, tile_side, tile_side, scale=scale, colkey=1)
                case TowerType.SPLITTER:
                    u, v = 0, 64  # splitter sprite coords
                    pyxel.blt(x + sprite_offset, y + sprite_offset, 0, u, v, tile_side, tile_side, scale=scale, colkey=1)
                case TowerType.MEDIC:
                    u, v = 32, 64  # medic sprite coords
                    pyxel.blt(x + sprite_offset, y + sprite_offset, 0, u, v, tile_side, tile_side, scale=scale, colkey=1)


    def get_clicked_cell(self, height, total_grid_height, cell_size):
        # use for placing down towers
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            vert_offset = (height - total_grid_height) // 2
            mouse_x, mouse_y = pyxel.mouse_x, pyxel.mouse_y
            col = mouse_x // cell_size
            row = (mouse_y - vert_offset) // cell_size
            return col, row
        return None

    def is_start_pressed(self, width, height):
        return pyxel.btnp(pyxel.KEY_SPACE)

    def display_cursor(self, next_color):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

        pyxel.circ(x, y, 10, next_color)
        pyxel.circb(x, y, 10, 7)

    def reset_screen(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)

    def draw_tilemap(self, height, total_grid_height, row_count, col_count, cell_size, paths):
            # same vert_offset
            vert_offset = (height - total_grid_height) // 2
    
            tile_side_length = 16          # tile pixel side length
            tile_scale = cell_size // tile_side_length + 1  # since cell_size is 72 and tile_side_length is 16, it will be 5x bigger
    
            # Calculate the offset to counteract the center-based scaling of blt()
            offset = (cell_size - tile_side_length) // 2

            all_path_info = {} # checks the direction of the path based on its prev and next neighbors (prev_cel, next_cell)

            for path in paths:
                for i, cell in enumerate(path):
                    prev_cell = path[i - 1] if i > 0 else None
                    next_cell = path[i + 1] if i < len(path) - 1 else None
                    all_path_info[cell] = (prev_cell, next_cell)

            for r in range(row_count):
                for c in range(col_count):
                    # Topleft corner of each cell
                    tl_x = c * cell_size
                    tl_y = vert_offset + (r * cell_size)
                    

                    if (r, c) not in all_path_info:
                        # checkerboard style
                        if (r+c) % 2 == 0:
                            u = 16
                            v = 0
                        else:
                            u = 32
                            v = 80
                    else:
                        prev_cell, next_cell = all_path_info[(r, c)]

                        neighbors = set()
                        for nb in [prev_cell, next_cell]:
                            if nb is None:
                                continue
                            dr = nb[0] - r
                            dc = nb[1] - c

                            if dr == -1:
                                neighbors.add(Dir.UP)
                            elif dr == 1:
                                neighbors.add(Dir.DOWN)
                            elif dc == -1:
                                neighbors.add(Dir.LEFT)
                            elif dc == 1:
                                neighbors.add(Dir.RIGHT)

                            if neighbors == {Dir.LEFT, Dir.RIGHT}:
                                u, v = 32, 0
                            elif neighbors == {Dir.UP, Dir.DOWN}:
                                u, v = 48, 0
                            elif neighbors == {Dir.UP, Dir.RIGHT}:
                                u, v = 0, 32
                            elif neighbors == {Dir.RIGHT, Dir.DOWN}:
                                u, v = 0, 16
                            elif neighbors == {Dir.DOWN, Dir.LEFT}:
                                u, v = 16, 16
                            elif neighbors == {Dir.LEFT, Dir.UP}:
                                u, v = 16, 32
                            else: #endpoints
                                if Dir.LEFT in neighbors or Dir.RIGHT in neighbors:
                                    u, v = 32, 0
                                else:
                                    u, v = 48, 0


                    pyxel.blt(tl_x + offset, tl_y + offset, 0, u, v, tile_side_length, tile_side_length, scale=tile_scale)

    def display_shield_tiles(self, vert_offset, cell_size, tunnel_paths):

        tile_side_length = 16          # tile pixel side length
        tile_scale = cell_size // tile_side_length + 1  # since cell_size is 72 and tile_side_length is 16, it will be 5x bigger
    
        # Calculate the offset to counteract the center-based scaling of blt()
        offset = (cell_size - tile_side_length) // 2

        for tunnel_path in tunnel_paths:
            for idx, (r, c) in enumerate(tunnel_path):
                x = c * cell_size
                y = vert_offset + (r * cell_size)

                u = 48
                v = 64

                pyxel.blt(x + offset, y + offset, 0, u, v, tile_side_length, tile_side_length, scale=tile_scale, colkey=1) # shield sprite coords
                #pyxel.rect(x, y, cell_size, cell_size, 13)

    def display_border_panels(self, height, total_grid_height):
        vert_offset = (height - total_grid_height) // 2  + 45
        tile_side = 16
        scale = 7  # bigger tiless

        u, v = 32, 48  # sprite coords

        tiles_needed = (1080 // (tile_side * scale)) + 2

        for i in range(tiles_needed):
            x = i * tile_side * scale

            # top line
            pyxel.blt(x, 0 + 45, 0, u, v, tile_side, tile_side, scale=scale)

            # bottom line
            pyxel.blt(x, vert_offset + total_grid_height, 0, u, v, tile_side, tile_side, scale=scale)

    def display_leaderboard(self, width, height, highlight_nickname, highlight_rounds, font_address, size):
        from leaderboard import load_leaderboard

        font = pyxel.Font(font_address, size)
        entries = load_leaderboard()

        col_x = width // 2
        pyxel.rect(0, 0, width, height, 0)

        # header
        pyxel.text(col_x - 70, 60, "LEADERBOARD", 10, font)
        pyxel.line(col_x - 250, 85, col_x + 250, 85, 7)

        # col headers
        col_rank = col_x - 280
        col_name = col_x - 210
        col_rounds = col_x + 130
        row_start = 110
        row_gap = 35

        pyxel.text(col_rank, row_start - 25, '#', 13, font)
        pyxel.text(col_name, row_start - 25, "NAME", 13, font)
        pyxel.text(col_rounds, row_start - 25, "ROUNDS", 13, font)

        # rows
        for i, entry in enumerate(entries):
            y = row_start + i * row_gap

            is_highlight = (entry["name"] == highlight_nickname and
                            entry["rounds"] == highlight_rounds)
            color = 10 if is_highlight else 7 # cyan? for new

            rank = {1: "FIRST", 2: "2ND", 3: "3RD"}.get(i + 1, f"{i + 1}TH")
            pyxel.text(col_rank, y, rank, color, font)
            pyxel.text(col_name, y, entry["name"][:15], color, font)
            pyxel.text(col_rounds, y, str(entry["rounds"]), color, font)

        pyxel.text(col_x - 150, height - 60, "SPACE: play again    Q: quit", 13, font)

    def display_name_input(self, width, height, name_buffer, font_address, size):
        font = pyxel.Font(font_address, size)

        panel_w, panel_h = 500, 200
        panel_x = (width - panel_w) // 2
        panel_y = (height - panel_h) // 2

        pyxel.rect(panel_x, panel_y, panel_w, panel_h, 0)
        pyxel.text(panel_x + 20, panel_y + 20, "ENTER YOUR NAME:", 7, font)

        # input box
        box_x = panel_x + 20
        box_y = panel_y + 60
        box_w, box_h = panel_w - 40, 40
        pyxel.rectb(box_x, box_y, box_w, box_h, 7)
        pyxel.rect(box_x + 1, box_y + 1, box_w - 2, box_h - 2, 1)

        pyxel.text(box_x + 10, box_y + 12, name_buffer, 7, font)
        pyxel.text(panel_x + 20, panel_y + 130, "ENTER: confirm", 13, font)
        pyxel.text(panel_x + 20, panel_y + 155, "BACKSPACE: delete", 13, font)

    def handle_name_input(self, name_buffer: str, max_length: int = 15):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_KP_ENTER):
            return name_buffer, True

        if pyxel.btnp(pyxel.KEY_BACKSPACE) and name_buffer:
            return name_buffer[:-1], False

        for code in range(32, 127):
            if pyxel.btnp(code):
                if len(name_buffer) < max_length:
                    shifted = pyxel.btn(pyxel.KEY_LSHIFT) or pyxel.btn(pyxel.KEY_RSHIFT)
                    char = chr(code) if shifted else chr(code).lower()
                    return name_buffer + char, False
                break
        return name_buffer, False

    def is_leaderboard_replay_pressed(self):
        return pyxel.btnp(pyxel.KEY_SPACE)

    def display_end_screen(self, width, height, won:bool, font_addr, size):
        font = pyxel.Font(font_addr, size)

        panel_w, panel_h = 500, 160
        panel_x = (width - panel_w) // 2
        panel_y = (height - panel_h) // 2

        pyxel.rect(panel_x, panel_y, panel_w, panel_h, 0)

        if won:
            line1, line2, color = "YOU WIN!", "CONGRATS!", 11
        else:
            line1, line2, color = "GAME OVER", "BETTER LUCK NEXT TIME!", 8

        pyxel.text(panel_x + 20, panel_y + 30, line1, color, font)
        pyxel.text(panel_x + 20, panel_y + 70, line2, color, font)
        pyxel.text(panel_x + 20, panel_y + 110, "Q: Quit", 6, font)
        pyxel.text(panel_x + 20, panel_y + 150, "SPACE: Leaderboard", 6, font)
