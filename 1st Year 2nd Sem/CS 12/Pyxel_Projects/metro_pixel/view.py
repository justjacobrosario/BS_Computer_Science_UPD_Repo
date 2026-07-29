import pyxel
from constants import Key_Input, Tile

class View:

    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="cargo_pixel")
        pyxel.load("audio_visuals.pyxres")
        pyxel.fullscreen(True)
        pyxel.mouse(True)
        

    def get_key_input(self):
        keys = set()
        if pyxel.btn(pyxel.KEY_Q):
            keys.add(Key_Input.QUIT)
        if pyxel.btnp(pyxel.KEY_EQUALS) or (pyxel.mouse_wheel > 0):
            keys.add(Key_Input.ZOOM_IN)
        if pyxel.btnp(pyxel.KEY_MINUS) or (pyxel.mouse_wheel < 0):
            keys.add(Key_Input.ZOOM_OUT)
        else:
            keys.add(Key_Input.NONE)
        return keys

    def get_mouse_state(self):
        is_dragging = pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
        return is_dragging, pyxel.mouse_x, pyxel.mouse_y
    

    def draw_grid_map(self, screen_width, screen_height, row_count, col_count, cell_px_size, map_matrix, camera_x, camera_y, zoom=1.0):
        center_x = screen_width // 2
        center_y = screen_height // 2

        pyxel.cls(1)

        tile_sprites = {
        -1 : (0, 0), # blank
        0 : (8, 0), # grass
        1 : (16, 0), # ocean
        2 : (24, 0), # sea
        3 : (32, 0), # sand
        4 : (40, 0), # snow
        }
        
        draw_size= cell_px_size * zoom

        for row in range(row_count):
            for col in range(col_count):
                world_x = col * cell_px_size
                world_y = row * cell_px_size

                x = center_x + (world_x - camera_x) * zoom
                y = center_y + (world_y - camera_y) * zoom
                
                if x < -draw_size or x > screen_width or y < -draw_size or y > screen_height:
                    continue
                tile_id = map_matrix[row][col]
                u, v = tile_sprites.get(tile_id, tile_sprites[-1])  # Default to blank if tile_id not found

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, scale = zoom)
        

    def clear(self):
        pyxel.cls(0)