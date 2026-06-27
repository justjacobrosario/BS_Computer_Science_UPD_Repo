import pyxel
from constants import Key_Input

class View:
    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="cargo_pixel", fullscreen=True)
        pyxel.load("audio_visuals.pyxres")

    def get_key_input(self):
        if pyxel.btn(pyxel.KEY_Q):
            return Key_Input.QUIT
        elif pyxel.btn(pyxel.KEY_W):
            return Key_Input.GO_UP
        elif pyxel.btn(pyxel.KEY_S):
            return Key_Input.GO_DOWN
        elif pyxel.btn(pyxel.KEY_A):
            return Key_Input.GO_LEFT
        elif pyxel.btn(pyxel.KEY_D):
            return Key_Input.GO_RIGHT
        elif pyxel.btn(pyxel.KEY_UP):
            return Key_Input.GO_UP_2
        elif pyxel.btn(pyxel.KEY_DOWN):
            return Key_Input.GO_DOWN_2
        elif pyxel.btn(pyxel.KEY_LEFT):
            return Key_Input.GO_LEFT_2
        elif pyxel.btn(pyxel.KEY_RIGHT):
            return Key_Input.GO_RIGHT_2
        else:
            return Key_Input.NONE

    def draw_grid_map(self, screen_width, screen_height, row_count, col_count, cell_px_size, map_matrix, player_x, player_y):
        center_x = screen_width // 2
        center_y = screen_height // 2

        cam_offset_x = (center_x - player_x)
        cam_offset_y = (center_y - player_y)

        pyxel.cls(0)

        tile_sprites = {
        -1 : (0, 0), # blank
        0 : (8, 0), # grass
        1 : (16, 0), # ocean
        2 : (24, 0), # sea
        3 : (32, 0), # sand
        4 : (40, 0) # snow
        }


        for row in range(row_count):
            for col in range(col_count):

                x = (col * cell_px_size) + cam_offset_x
                y = (row * cell_px_size) + cam_offset_y

                #if the tile is fully off-screen, skip drawing it
                if x < -cell_px_size or x > screen_width or y < -cell_px_size or y > screen_height:
                    continue
                tile_id = map_matrix[row][col]
                if tile_id in {0, 1, 2,3, 4}:
                    u, v = tile_sprites[tile_id]
                else:
                    u, v  = tile_sprites[-1]

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size)

    def clear(self):
        pyxel.cls(0)