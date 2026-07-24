import pyxel
from constants import Key_Input

class View:
    def __init__(self):
        self.custom_ttf = "UbuntuMono-Regular.ttf"

    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="cargo_pixel")
        pyxel.fullscreen(True)
        pyxel.load("audio_visuals.pyxres")


    def get_key_input(self):
        keys = set()
        if pyxel.btn(pyxel.KEY_Q):
            keys.add(Key_Input.QUIT)
        if pyxel.btn(pyxel.KEY_W):
            keys.add(Key_Input.GO_UP)
        if pyxel.btn(pyxel.KEY_S):
            keys.add(Key_Input.GO_DOWN)
        if pyxel.btn(pyxel.KEY_A):
            keys.add(Key_Input.GO_LEFT)
        if pyxel.btn(pyxel.KEY_D):
            keys.add(Key_Input.GO_RIGHT)
        if pyxel.btn(pyxel.KEY_UP):
            keys.add(Key_Input.GO_UP_2)
        if pyxel.btn(pyxel.KEY_DOWN):
            keys.add(Key_Input.GO_DOWN_2)
        if pyxel.btn(pyxel.KEY_LEFT):
            keys.add(Key_Input.GO_LEFT_2)
        if pyxel.btn(pyxel.KEY_RIGHT):
            keys.add(Key_Input.GO_RIGHT_2)
        else:
            keys.add(Key_Input.NONE)
        return keys

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
        4 : (40, 0), # snow
        5 : (48, 0) # port
        }

        ports = []
        for row in range(row_count):
            for col in range(col_count):
                x = (col * cell_px_size) + cam_offset_x
                y = (row * cell_px_size) + cam_offset_y
                
                tile_id = map_matrix[row][col]
                if tile_id == 5:
                    ports.append((row, col))
                    u, v = tile_sprites[-1]

                #if the tile is fully off-screen, skip drawing it
                if x < -cell_px_size or x > screen_width or y < -cell_px_size or y > screen_height:
                    continue
                if tile_id in {0, 1, 2,3, 4}:
                    u, v = tile_sprites[tile_id]
                else:
                    u, v  = tile_sprites[-1]

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size)
        for row, col in ports:
            x = (col * cell_px_size) + cam_offset_x - (cell_px_size//2)
            y = (row * cell_px_size) + cam_offset_y - (cell_px_size//2)
            u,v = tile_sprites[5]
            pyxel.blt(x, y, 0, u, v, cell_px_size * 2, cell_px_size * 2, 1)

    def draw_player(self, screen_width, screen_height, row_count, col_count, cell_px_size, curr_keys, ship):

        x = screen_width//2 - (cell_px_size // 2)
        y = screen_height//2 - (cell_px_size // 2)

        if (Key_Input.GO_UP in curr_keys) or (Key_Input.GO_DOWN in curr_keys): # same sprite for horizontal movements
            u, v = (16, 8)

            pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size*2, 1)
        else:
            u, v = (0, 8)

            pyxel.blt(x, y, 0, u, v, cell_px_size*2, cell_px_size, 1)  

    def draw_ship_trail(self, screen_width, screen_height, row_count, col_count, cell_px_size, prev_ship_locs, player_x, player_y):
        center_x = screen_width // 2
        center_y = screen_height // 2

        cam_offset_x = (center_x - player_x)
        cam_offset_y = (center_y - player_y)

        
        for prev_x, prev_y in prev_ship_locs:
            x = prev_x + cam_offset_x
            y = prev_y + cam_offset_y
            
            u, v = (72, 0) # trail sprite top left coord
            pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, 1)



    def clear(self):
        pyxel.cls(0)