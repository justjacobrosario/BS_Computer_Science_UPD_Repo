import pyxel
from constants import Key_Input, Tile, PORT_BOX_SPRITE_UV, PORT_SPRITE_UV, PORT_SPRITE_SIZE, CARGO_SPRITE_UV, CARGO_SPRITE_SIZE, CARGO_SPRITE_ORDER, Cargo, LOAD_BAR_EMPTY_U, LOAD_BAR_START_U, LOAD_BAR_U_STEP

class View:
    def __init__(self):
        self.custom_ttf = "UbuntuMono-Regular.ttf"
        self._font = None

    def start(self, screen_width, screen_height):
        pyxel.init(screen_width, screen_height, title="cargo_pixel")
        pyxel.fullscreen(True)
        pyxel.load("audio_visuals.pyxres")
        self._font = pyxel.Font(self.custom_ttf, 14)


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

                x = center_x + (world_x - player_x) * zoom
                y = center_y + (world_y - player_y) * zoom
                
                if x < -draw_size or x > screen_width or y < -draw_size or y > screen_height:
                    continue
                tile_id = map_matrix[row][col]
                u, v = tile_sprites.get(tile_id, tile_sprites[-1])  # Default to blank if tile_id not found

                pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, scale = zoom)
        
    def draw_player(self, screen_width, screen_height, row_count, col_count, cell_px_size, curr_keys, ship, zoom=1.0):
        draw_size = cell_px_size * zoom
        x = screen_width//2 - (draw_size/2)
        y = screen_height//2 - (draw_size/2)

        if (Key_Input.GO_UP in curr_keys) or (Key_Input.GO_DOWN in curr_keys): # same sprite for horizontal movements
            u, v = (16, 8)

            pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size*2, 1, scale=zoom)
        else:
            u, v = (0, 8)

            pyxel.blt(x, y, 0, u, v, cell_px_size*2, cell_px_size, 1, scale=zoom)  

    def draw_ship_trail(self, screen_width, screen_height, row_count, col_count, cell_px_size, prev_ship_locs, player_x, player_y, zoom=1.0):
        center_x = screen_width // 2
        center_y = screen_height // 2

        
        for prev_x, prev_y in prev_ship_locs:
            x = center_x + (prev_x - player_x)*zoom
            y = center_y + (prev_y - player_y)*zoom
            
            u, v = (72, 0) # trail sprite top left coord
            pyxel.blt(x, y, 0, u, v, cell_px_size, cell_px_size, 1, scale=zoom)

    def draw_ports(self, screen_width, screen_height, ports, cell_px_size, player_x, player_y, zoom=1.0):
        center_x = screen_width // 2
        center_y = screen_height // 2

        _, box_v = PORT_BOX_SPRITE_UV
        port_u, port_v = PORT_SPRITE_UV
        cargo_u0, cargo_v = CARGO_SPRITE_UV

        draw_port_size =PORT_SPRITE_SIZE*zoom
        draw_cell_size = cell_px_size*zoom
        draw_cargo_size = CARGO_SPRITE_SIZE*zoom

        for port in ports:

            
            world_x = port.x * cell_px_size
            world_y = port.y * cell_px_size
            
            tile_x = center_x + (world_x - player_x)*zoom
            tile_y = center_y + (world_y - player_y)*zoom

            if tile_x < -draw_port_size or tile_x > screen_width or tile_y < -draw_port_size or tile_y > screen_height:
                continue

            port_x = tile_x - (draw_port_size - draw_cell_size) // 2
            port_y = tile_y - (draw_port_size - draw_cell_size) // 2
            box_x = port_x
            box_y = port_y - draw_port_size - 1 # 1 for spacing

            bucket = round(port.progress * 10)
            if bucket <= 0:
                box_u = LOAD_BAR_EMPTY_U
            else:
                box_u = LOAD_BAR_START_U + (min(bucket, 10) - 1) * LOAD_BAR_U_STEP


            pyxel.blt(box_x, box_y, 0, box_u, box_v, PORT_SPRITE_SIZE, PORT_SPRITE_SIZE, 1, scale=zoom)
            pyxel.blt(port_x, port_y, 0, port_u, port_v, PORT_SPRITE_SIZE, PORT_SPRITE_SIZE, 1, scale=zoom)

            for i, cargo in enumerate(port.cargos_to_ship[:4]):
                cargo_index= CARGO_SPRITE_ORDER.index(cargo)
                cu = cargo_u0 + (cargo_index * CARGO_SPRITE_SIZE)
                cx = box_x +  (i%2) * CARGO_SPRITE_SIZE
                cy = box_y +  (i//2) * CARGO_SPRITE_SIZE
                pyxel.blt(cx, cy, 0, cu, cargo_v, CARGO_SPRITE_SIZE, CARGO_SPRITE_SIZE, 1, scale=zoom)

    def draw_ship_hud(self, screen_width, screen_height, curr_cargo, total_cargo, max_cargo):
        cargo_labels = {
            Cargo.RED: "R",
            Cargo.ORANGE: "O",
            Cargo.YELLOW: "Y",
            Cargo.GREEN: "G",
            Cargo.BLUE: "B"
        }

        text = " ".join(f"{cargo_labels[c]}: {curr_cargo[c]}" for c in CARGO_SPRITE_ORDER)
        text += f" | Total: {total_cargo}/{max_cargo}"

        pad_x, pad_y = 5, 5
        text_w = self._font.text_width(text)
        text_h = 8
        
        rect_w = text_w + 2 * pad_x
        rect_h = text_h + 2 * pad_y + 10

        rect_x = (screen_width - rect_w) // 2
        rect_y = screen_height - rect_h - 10

        pyxel.rect(rect_x, rect_y, rect_w, rect_h, 0)
        pyxel.text(rect_x + pad_x, rect_y + pad_y, text, 7, self._font)


    def clear(self):
        pyxel.cls(0)