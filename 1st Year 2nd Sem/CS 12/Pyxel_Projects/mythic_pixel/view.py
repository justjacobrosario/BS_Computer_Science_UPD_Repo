import pyxel
from constants import Key_Input
class Button:
    def __init__(self, name, text, x, y, width, height, is_left_clicked):
        self.name = name
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_left_clicked = is_left_clicked


class View:
    def __init__(self):
        self._title_font = None
        self._font = None

    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="cargo_pixel")
        pyxel.fullscreen(True)
        pyxel.load("audio_visuals.pyxres")
        pyxel.mouse(True)
        self._title_font = pyxel.Font("BreatheFire.ttf", 30)
        self._subhead_font = pyxel.Font("unispace.ttf", 20)
        self._body_font = pyxel.Font("UbuntuMono-Regular.ttf", 13)

    # MENU DISPLAY

    def draw_menu(self, screen_width, screen_height, stage_access, curs_x, curs_y, is_left_clicked):

        #pyxel.rect(screen_height//2 - 200, screen_width//2 - 200, 400, 200, 7)
        
        # TITLE

        title_text = "Mythic Pixel"
        title_w = self._title_font.text_width(title_text)
        x = (screen_width - title_w)//2
        y = 10
        pyxel.text(x, y, title_text, 7, self._title_font)

        # STAGE OPTION
        play_btn_w =  40
        play_btn_h = 13
        play_btn_y = screen_height - 50
        play_btn = Button("play", "PLAY", (screen_width - play_btn_w)//2, play_btn_y, play_btn_w, play_btn_h, False)

        button = [play_btn]

        

        for btn in button:
            if (btn.x <= curs_x <= btn.x + btn.width) and (btn.y <= curs_y <= btn.y + btn.height) and is_left_clicked:
                color = 7
                text_col = 0
            else:
                color = 0
                text_col = 7

            hor_padding = btn.width-  self._title_font.text_width(btn.text) // 2

            pyxel.rect(btn.x, btn.y, btn.width, btn.height, color)
            pyxel.text(btn.x + hor_padding, btn.y, btn.text, text_col, self._body_font)


    # INGAME DISPLAY

    def get_cursor_coords(self):
        return (pyxel.mouse_x, pyxel.mouse_y)


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
        if pyxel.btnp(pyxel.KEY_EQUALS):
            keys.add(Key_Input.ZOOM_IN)
        if pyxel.btnp(pyxel.KEY_MINUS):
            keys.add(Key_Input.ZOOM_OUT)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            keys.add(Key_Input.LEFT_CLICK)
        else:
            keys.add(Key_Input.NONE)
        return keys

    def draw_grid_map(self, screen_width, screen_height, row_count, col_count, cell_px_size, map_matrix, player_x, player_y, zoom=1.0):
        center_x = screen_width // 2
        center_y = screen_height // 2

        cam_offset_x = (center_x - player_x)
        cam_offset_y = (center_y - player_y)

        pyxel.cls(1)

        tile_sprites = {
        -1 : (0, 0), # blank
        0 : (16, 0), # grass
        1 : (32, 16), # bush
        2 : (32, 0), # rock
        3 : (0, 0), # none
        }
        
        draw_size= cell_px_size * zoom

        for row in range(row_count):
            for col in range(col_count):
                world_x = col * cell_px_size
                world_y = row * cell_px_size

                x = center_x + (world_x - player_x) * zoom
                y = center_y + (world_y - player_y) * zoom
                
                if x < -draw_size or x > screen_width or y < -draw_size or y > screen_height:
                    continue
                tile_id = map_matrix[row][col]
                u, v = tile_sprites.get(tile_id, tile_sprites[-1])  # Default to blank if tile_id not found

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, scale = zoom)
        
    def draw_player(self, screen_width, screen_height, row_count, col_count, cell_px_size, curr_keys, zoom=1.0):
        draw_size = cell_px_size * zoom
        x = screen_width//2 - (draw_size/2)
        y = screen_height//2 - (draw_size/2)

        
        u, v = (0, 32)

        pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, 1, scale=zoom)  


    def clear(self):
        pyxel.cls(0)